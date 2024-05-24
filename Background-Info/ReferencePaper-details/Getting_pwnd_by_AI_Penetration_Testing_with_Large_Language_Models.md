## Getting pwn’d by AI: Penetration Testing with Large Language Models (Dec. 2023)

<br>

| Resources	|
|----------|
| [Database](https://dl-acm-org.ezproxy.semo.edu:2443/doi/10.1145/3611643.3613083) |
| DOI: 10.1145/3611643.3613083) |
| [PDF](https://dl-acm-org.ezproxy.semo.edu:2443/doi/pdf/10.1145/3611643.3613083) |

<br>

----

### Goal: This paper explores the potential use of large-language models, such as GPT3.5, to augment penetration testers with AI sparring partners. 

**Goal 1:** high-level (task planning for security testing assignments)

**Goal 2:** low level (vulnerability hunting within a vulnerable virtual machine)

<br>

### Additional Notes

<br>

**Autonomous Task Execution Agents**

Take tasks from the task queue --> execute them --> add new information to a memory store

Identifies new subsequent tasks that are pushed upon the task queue and are eventually executed

<br>

**Typical questions asked by pen-testers:**
- “what is a good attack methodology”
- “how to attack Active Directory”

<br> 

**Large language models (LLMs) - ChatCPT or GPT3.5**

Experimented asking LLM to help design penetration tests for both generic scenarios and concrete target organization

Use: help design penetration tests, generate phishing or vishing messages, automated report generation (for pen-test and red teaming)

- should be able to cover the whole TTP spectrum 
- select suitable tactics and corresponding techniques
- given an employed tactic, derive feasible techniques and procedures

<br>

----

<br>
  
<a id="approach"></a>
## Approach

(1) Task planning for security testing assignments -- High-level

(2) vulnerability hunting within a vulnerable virtual machine -- Low-level

<br>

<a id="solutions"></a>
## Solutions

Issue: lack of personnel

Solution: AI

<br>

<a id="tools"></a>
## Tools

- GPT3.5
- ChatGPT: uses prompts
- [llama.cpp](#llama)
- [AutoGPT](#autogpt): creates prompts - requires less user engineering
- [BabyAGI](#babyagi): task generation, planning, and execution
- [hackingBuddyGPT](#hackingbuddygpt) 


<br>

<a id="equipment"></a>
## Equipment (ex: Raspberry Pi)  

- Vulnerable VM with GPT3.5 integrated - allowed it to analyze the machine for vulnerabilities and suggest attack vectors

<br> 


<a id="methods"></a>
## Methods (Attacks)

**Attack Vectors:**
- Password spraying
- Kerberoasting
- AS-REP roasting
- Exploiting Active Directory Certificate Services
- Abusing unconstrained delegation
- Exploiting group policies

<br>

<a id="terminology"></a>
## Terminology

[MITRE ATT&CK](#mitre): curated database of knowledge about threat actors in the cybersecurity domain

<br>

----

## Misc

<br>

<a id="babyagi"></a>
**AutoGPT (Tools):**

[Github](https://github.com/Significant-Gravitas/Auto-GPT)

| Job																	| Result																																					|
|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| tasked to devise an external penetration testing plan for company 	| standard methods such as performing a network vulnerability scan, performing OSINT/user enumeration, and performing phishing against identified users 	|
| Further inquiry														| crawl the company’s web page and identify potential phishing targets (users and their email addresses) 													| 

- declined to perform any “real” network security scan or perform phishing operations due to its ethical filters
- auto-generating sequences of instructions by leveraging LLMs to create the prompt that is subsequently used to query the LLM
- allows users to provide concise initial questions -- less of a need for manual prompt engineering
- issue: can invent facts that seem statistically plausible
- integrates web-based queries and optional human-provided feedback during its operation
	
<br>

<a id="babyagi"></a>
**BabyAGI (Tools):**

[Website](https://github.com/yoheinakajima/babyagi)

| Job	| Result	|
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Asked AgentGPT to “Become domain admin in an Active Directory” 	| generated document contained highly realistic attack vectors such as password spraying, Kerberoasting, AS-REP roasting, exploiting Active Directory Certificate Services, abusing unconstrained delegation or exploiting group policies 	|

- provides a “pareddown” version of GPT-4
- focused on automated task generation, planning, and execution

<br>

<a id="hackingbuddygpt"></a>
**hackingBuddyGPT (Tools):**

[Github](https://github.com/ipa-lab/hackingBuddyGPT)

Purpose: allow for realistic evaluation
- Python script that uses SSH to connect to a deliberately vulnerable lin.security Linux virtual machine
- Uses GPT3.5-turbo
- uses command output to identify potential security vulnerabilities (and provide exploitation example)
- suggested system commands were based upon pattern-matching and not on a deeper understanding of the Linux system or on model building
- Ethics filter was infrequently triggered (triggered more when asking "detail additional vulnerabilities")

Use case: low-privilege user wants to become the root user
- the LLM can state a Linux shell command that will be executed over SSH on the virtual machine
- After retrieving the list of sudoers, GPT3.5 consistently suggested various vulnerable sudo commands for privilege escalation
- When given the additional subcommand of “and explain the found vulnerabilities” in the prompt, GPT3.5 was able to provide good introductory information and could thus be utilized as part of on-the-job training.

Considerations:
- singular runs were not stable
- with multiple runs, results converged
- Compared to tools such as [linpeas.sh](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS), LLMs seem to be less deterministic
- switching from OpenAI to one of the locally running LLMs would remove all server-side ethics checks
- Using LLMs to generate and optimize the prompts themselves, similar to AutoGPT, might improve their effectiveness (current is static and manual)

<br>

<a id="llmama"></a>
**llama.cpp (Tools):**
- makes use of small-scale models (up to 13b parameters) feasible on consumer-grade hardware.
- models can be run without any cloud/API costs
- are not subject to any server-side moderation or censorship.

<br>

<a id="mitre"></a>
**MITRE ATT&CK (Terminology):**

Definition: curated database of knowledge about threat actors in the cybersecurity domain
* covers different tactics, techniques, and procedures

	**T - Tactics**
	- describes high-level objectives an adversary intends to achieve (e.g. reconnaissance, privilege escalation or collection)
	
	**T - Techniques**
	- each is a way to achieve a tactic (e.g. Abuse Elevation Control Mechanism: Sudo and Sudo Caching)
	
	**P - Procedures**
	- specific details of how an adversary executes a technique

- Training a new LLM is prohibitively expensive for most researchers, but existing LLMs can be refined or fine-tuned to specific use cases for feasible costs
-  Prompts have to be carefully prepared
	
<br>

## Other Documents Referenced

[Mitre att&ck: Design and philosophy (2018)](https://www.mitre.org/news-insights/publication/mitre-attck-design-and-philosophy) 

	Blake E Strom, Andy Applebaum, Doug P Miller, Kathryn C Nickels, Adam G Pennington, and Cody B Thomas

