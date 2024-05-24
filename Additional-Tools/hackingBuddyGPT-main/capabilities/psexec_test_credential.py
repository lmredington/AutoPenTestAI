import warnings
from dataclasses import dataclass
from typing import Tuple

from utils import PSExecConnection
from .capability import Capability


@dataclass
class PSExecTestCredential(Capability):
    conn: PSExecConnection

    def describe(self, name: str = None) -> str:
        return f"give credentials to be tested by stating `{name} username password`"

    def __call__(self, username: str, password: str) -> Tuple[str, bool]:
        try:
            test_conn = self.conn.new_with(username=username, password=password)
            test_conn.init()
            warnings.warn("full credential testing is not implemented yet for psexec, we have logged in, but do not know who we are, returning True for now")
            return "Login as root was successful\n", True
        except Exception:
            return "Authentication error, credentials are wrong\n", False
