import re
from dataclasses import dataclass
from typing import Tuple

from invoke import Responder

from utils import SSHConnection
from .capability import Capability


GOT_ROOT_REXEXPs = [
    re.compile("^# $"),
    re.compile("^bash-[0-9]+.[0-9]# $")
]


@dataclass
class SSHRunCommand(Capability):
    conn: SSHConnection

    def describe(self, name: str = None) -> str:
        return f"give a command to be executed on the shell and I will respond with the terminal output when running this command on the linux server. The given command must not require user interaction. Only state the to be executed command. The command should be used for enumeration or privilege escalation."

    def __call__(self, command: str) -> Tuple[str, bool]:
        got_root = False
        sudo_pass = Responder(
            pattern=r'\[sudo\] password for ' + self.conn.username + ':',
            response=self.conn.password + '\n',
        )

        try:
            stdout, stderr, rc = self.conn.run(command, pty=True, warn=True, watchers=[sudo_pass], timeout=10)
        except Exception as e:
            print("TIMEOUT! Could we have become root?")
            stdout, stderr, rc = "", "", -1
        tmp = ""
        last_line = ""
        for line in stdout.splitlines():
            if not line.startswith('[sudo] password for ' + self.conn.username + ':'):
                last_line = line
                tmp = tmp + line

        # remove ansi shell codes
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        last_line = ansi_escape.sub('', last_line)

        for i in GOT_ROOT_REXEXPs:
            if i.fullmatch(last_line):
                got_root = True
        if last_line.startswith(f'root@{self.conn.hostname}:'):
            got_root = True
        return tmp, got_root
