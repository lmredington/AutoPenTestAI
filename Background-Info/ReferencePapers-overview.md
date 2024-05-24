# General Ideas:

## New/Prototype Tools:
- CyberCheck
- AutoGPT
- BabyAGI
- HackingBuddyGPT
- Footholder
- SAT

[SAT]

Used **Arachni crawler** for generating URL lists with the OAuth authentication framework. These URLs are provided as a seed value to other open-source scanners (ZAP, W3af, and Wapiti), and their vulnerabilities, detection have been improved.

**Effectiveness of a tool** depends upon its capability to efficiently crawl various web pages


## Literature

### FOOTHOLDER: Collection of tools and scripts used to learn and experiment the exploitation of vulnerable machines (Apr. 2023)
[Database:](https://doi-org.ezproxy.semo.edu:2443/10.1109/ICNWC57852.2023.10127486) DOI: 10.1109/ICNWC57852.2023.10127486

**Relevance:** Medium

**Overview:** Tool to educate users about tools and how to use them


### Kali Linux based Empirical Investigation on Vulnerability Evaluation using Pen-Testing tools (July 2023)
[Database:](https://ieeexplore-ieee-org.ezproxy.semo.edu:2443/document/10235163) DOI: 10.1109/WCONF58270.2023.10235163

**Relevance:** HIGH

**Overview:** Describes the foundations of penetration testing, tools and methodologies for penetration testing using Kali Linux


### Cybercheck – OSINT & Web Vulnerability Scanner (2023)
[Database:](https://doi-org.ezproxy.semo.edu:2443/10.1109/ICECAA58104.2023.10212207) DOI: 10.1109/ICECAA58104.2023.10212207

**Relevance:** HIGH

**Overview:** Open-Source Intelligence (OSINT) and Web Vulnerability Scanning


## Getting pwn’d by AI: Penetration Testing with Large Language Models (Dec. 2023)
[Database:](https://dl-acm-org.ezproxy.semo.edu:2443/doi/10.1145/3611643.3613083) DOI: 10.1145/3611643.3613083

**Relevance:** High

**Overview:** Uses of large-language models, such as GPT3.5, to augment penetration testers with AI sparring partners. 


## An Analysis of Vulnerability Scanners in Web Applications for VAPT (May 2022)
[Database:](https://doi-org.ezproxy.semo.edu:2443/10.1109/CISES54857.2022.9844365) DOI: 10.1109/CISES54857.2022.9844365

**Relevance:** HIGH

**Overview:** focus on various vulnerability analysis tools forming basis for VAPT and try to analyze the various impact with respect to stages of penetration testing.


## Security Vulnerability Analysis using Penetration Testing Execution Standard (PTES): Case Study of Government’s Website (Mar. 2023)
[Database:](https://doi-org.ezproxy.semo.edu:2443/10.1145/3592307.3592329) DOI: 10.1145/3592307.3592329

**Relevance:** High

**Overview:** Testing utilized Kali Linux and tools (ex: OWASP ZAP, Acunetix, Nmap, Paros, and others)


## Scanning of Web-Applications: Algorithms and Software for Search of Vulnerabilities “Code Injection” and “Insecure Design” (Sept 2023)
[Database:](https://doi-org.ezproxy.semo.edu:2443/10.1109/IDAACS58523.2023.10348918) DOI: 10.1109/IDAACS58523.2023.10348918

[PDF](https://ieeexplore-ieee-org.ezproxy.semo.edu:2443/stamp/stamp.jsp?tp=&arnumber=10348918) 

**Relevance:** High

**Overview:** Analysis of existing algorithms and software capable of automatically scanning web applications (SQLMap, Blisqy, jSQL Injection, Checkov, Trivy, Snyk)

## SAT: Integrated Multi-agent Blackbox Security Assessment Tool using Machine Learning (March 2022)
[Database:](https://doi-org.ezproxy.semo.edu:2443/10.1109/ICAI55435.2022.9773750) DOI: 10.1109/ICAI55435.2022.9773750

**Relevance:** HIGH

**Overview:** Evaluated publicly available web vulnerability scanners and proposed an Integrated Multi-Agent Blackbox Security Assessment Tool (SAT) which uses a scanning engine, vulnerability database, and knowledgebase


## Ethical Hacking: A Technique to Enhance Information Security (May 2022)
[Database:](https://doi.org/10.1109/COM-IT-CON54601.2022.9850601) DOI: 10.1109/COM-IT-CON54601.2022.9850601

**Relevance:** Low

**Overview:** Hacking phases, general tools, types of attacks

<br>

# Referenced Tools

| Tools				| Phases Used																|  Interface 					| Features 																																											| 	Example Commands						| Referenced Material 									|
|-------------------|---------------------------------------------------------------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|-------------------------------------------------------|
| Acunetix			| Exploit																	| --- 							| exploits XSS, SQL injections, Host Header Injection, and over 3000 other web vulnerabilities 																						| ---										| Analysis: [7]; Mentioned: [5]							| 
| APPSCAN			|																			| --- 							| + Advanced application scanning <br> + Remediation capabilities <br> + Enterprise application security status metrics 															| ---										| Analysis: [7]											| 
| Arachni			|																			| --- 							| Crawler, good for detecting mass assignment vuln																																	| ---										| Analysis: [7]											| 
| AutoGPT			| Reconnaissance & Planning[4]												| --- 							| + Devise an external penetration testing plan <br> + identify potential phishing targets (on Web page) 																			| --- 										| Mentioned: [4]										| 
| Blisqy			| + Scanning <br> + Exploitation											| --- 							| Find and exploit Time-based Blind SQL injection vulnerabilities in HTTP headers 																									| --- 										| Analysis: [6]											| 
| Burp Suite		| Exploitation[3]															| --- 							| Verify attack vectors and detect vuln (authentication, injection, and security misconfigurations) <br> + track request and response between server and clients 					| ---										| Analysis: [3], [7]; Mentioned: [2],[8]				| 
| Censys			|																			| --- 							| Vulnerability detection and filtering 																																			| --- 										| Used: [2]												| 
| Checkov			| Scanning																	| --- 							| Scanning IaC templates													 																										| --- 										| Mentioned: [6]										| 
| CyberCheck		| + Reconnaissance & Planning <br> + Scanning								| --- 							| Open-Source usercustomizable OSINT and Web Vulnerability scanner 																													| --- 										| Used: [2]												| 
| dig				| Reconnaissance)[5]														| Command line 					| DNS name servers information; Troubleshoot DNS problems 																															| --- 										| Analysis: [5]											| 
| Dirbuster			| Exploitation[3]															| --- 							| Directory Enumeration													 																											| --- 										| Used: [1]												| 
| Enum4linux		|																			| --- 							| 																																													| --- 										| Used: [1]												| 
| FFUF				|																			| --- 							| 																																													| --- 										| Used: [1]												| 
| Footholder		|																			| --- 							| + Access tools <br> + Tool operation instruction 																																	| --- 										| Used: [1]												| 
| FTP				| Service Enumeration														| --- 							| 																																													| --- 										| Used: [1]												| 
| Gobuster			| Exploitation																| --- 							| Directory Enumeration													 																											| --- 										| Used: [1]												| 
| hackingBuddyGPT	| + Gaining Access[4] <br> + Retaining Access[4] <br> + Exploitation[4] 	| --- 							| + Gain root privileges in VM (produce commands) <br> + identify potential security vulnerabilities <br> + provide exploitation examples											| --- 										| Used: [4]												| 
| HP Web Inspect	|																			| --- 							| Launch attacks on web systems													 																									| ---										| Analysis: [7]											| 
| Hydra				| Exploitation[3]															| --- 							| Brute Forcing													 																													| --- 										| Used: [1]; Mentioned: [3]								| 
| jSQL Injection	| + Scanning <br> + Exploitation											| --- 							| Detect and exploit SQL injection vulnerabilities in web applications that use SQL databases 																						| --- 										| Analysis: [6]											| 
| Linux				|																			| Command-line 					| OS that manages a system's hardware and resources 																																| --- 										| Mentioned: [8]										| 
| Maltego			| Reconnaissance															| + GUI <br> + Command-line 	| OSINT tool for reconnaissance, graphical link analysis for connection related information (terms of email, phone numbers)															| --- 										| Analysis: [3]; Used: [2]								|
| Metasploit 		| + Gaining Access[3] <br> + Exploitation[3]								| + GUI <br> + Command-line 	| + Discovery, exploitation, and validation of vulnerabilities [6] <br> + Leverge known exploits and techniques, simulate real-world attacks 										| 											| Used: [1]; Mentioned: [3],[6],[8]						|
| MySQL				|																			| --- 							| 																																													|  											| Used: [1]												| 
| Nessus			| Scanning[3]																| GUI 							| Detect multiple security vulnerabilities in the OS of targeted hosts, software patches, and services <br> + generate security recommendations <br> + show vulnerability category 	| ---										| Analysis: [7]; Used: [9]; Mentioned: [3]				| 
| NetDiscover 		| + Reconnaissance & Planning[1] <br> + Network Enumeration[1] 				| --- 							| target IP													 																														| 											| Used: [1]												|
| NetSparker		|																			| --- 							| + Web scanner <br> + discover web vulnerabilities													 																				| ---										| Analysis: [7]											| 
| Nexpose			| Scanning[3]																| --- 							| Explore software level network level vulnerabilities [3]													 																		|  											| Mentioned: [3]										| 
| Nikto				| Scanning[3]																| --- 							| Execute and scan for multiple items including malicious files/ programs, and outdated versions in both software libraries and web servers.										| ---										| Analysis: [7]; Used: [1]								| 
| Nmap 				| + Reconnaissance & Planning[1, 5] <br> + Network Enumeration[1] 			| Command line 					| ports, services, OS, fundamental vulnerabilities, host detection 																													| "nmap disperindag.xxxprov.id"[5] 			| Analysis: [3],[5]; Used:[2],[3],[9]; Mentioned: [6],[8] 	|
| nslookup			| Reconnaissance[5]															| Command line 					| + DNS lookup <br> + server and address information of website 																													| "nslookup disperindog.xxxprov.go.id"[5] 	| Analysis: [5]											| 
| Open VAS			| Scanning[3]																| GUI 							| Vulnerability Scanner - produces report, denoting severity 																														| 											| Analysis: [3]											| 
| OWASP ZAP			| Vulnerability Analysis[5]													| GUI 							| Identify Vulnerabilities on target website													 																					| ---										| Analysis: [7]; Mentioned: [5]							| 
| Paros				|																			| --- 							| 																																													| 											| Mentioned: [5]										| 
| SAT				| + Reconnaissance & Planning <br> + Scanning <br> + (Analysis) Report 					| --- 							| host discovery and initialization --> scanning of the input web application (Scanning Engine, Vulnerabilities Database, Knowledgebase) --> generate report 			| ---  										| Analysis: [7]											| 
| Shodan			|																			| --- 							| + IoT device search engine <br> + vulnerability scanner <br> + port scanning 																										|  											| Used: [2]												| 
| SQLMap			| Scanning																	| --- 							| Automated detection of SQL injection vulnerabilities 																																|  											| Analysis: [6]											| 
| Snyk				| + Scanning <br> + Vuln Analysis											| --- 							| + (in Containers and IaC:) <br> Scan and prioritize information security <br> + Detect and identify vulnerabilities in modules 													| ---										| Mentioned: [6]										| 
| SSH				|																			| --- 							| 																																													| ---										| Used: [1]												| 
| Telnet			| Service Enumeration														| --- 							| 																																													| ---										| Used: [1]												| 
| Trivy				| Scanning [6]																| --- 							| + Analyzes layers and dependencies within a container image to identify potential security issues <br> + returns detailed report													| ---										| Mentioned: [6]										| 
| Wapiti			|																			| Command-line 					| Detects Injection, CSS, Command Execution Attacks, CRLF Injection, and File Disclosure																							| ---										| Analysis: [7]											| 
| Wireshark			| Exploitation[3]															| GUI 							| Capture network packets													 																										| ---										| Mentioned: [3]										| 
| W3af				|																			| + GUI <br> + Command-line 	| Detect and exploit web application vulnerabilities 													 																			| ---										| Analysis: [7]											| 
| ZapBurp			| Access (Vuln. Analysis Phase)[3]											| --- 							| + Perform vulnerability scan <br> + Provide mitigation measures 																													| ---										| Analysis: [3]											| 
| Netcraft			| Info Gathering (Planning and reconnaissance) [3] 							| GUI 							| hosting/network details and background 																																			| ---										| Analysis: [3]											| 
| Whois				| Info Gathering (Planning and reconnaissance)[3] 							| GUI 							| websites, and IP owner info 																																						| ---										| Analysis: [3]											| 
| Zenmap			| Info Gathering (Planning and reconnaissance)[3] 							| GUI 							| + Operating system and version <br> + List of open ports <br> + Services <br> + Monitoring <br> + Network inventory kind of tasks													| ---										| Analysis: [3]											| 

<br> 

[1] Footholder

[2] CyberCheck

[3] An Analysis of Vulnerability Scanners in Web Applications for VAPT

[4] AI

[5] Security Vulnerability Analysis using Penetration Testing Execution Standard (PTES): Case Study of Government’s Website

[6] Scanning of Web-Applications: Algorithms and Software for Search of Vulnerabilities “Code Injection” and “Insecure Design” (Sept 2023)

[7] SAT

[8] Ethical Hacking: A Technique to Enhance Information Security

[9] Security Vulnerability Analysis and Recommendations for Open Media Vault Cloud Server on Raspberry Pi