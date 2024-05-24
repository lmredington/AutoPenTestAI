# Burp Suite

<br> 

## [2] CyberCheck


<br> 

## [3] An Analysis of Vulnerability Scanners in Web Applications for VAPT


<br> 

## [7] SAT

**BurpSuite (Open-Source Scanner):**
	
Definition: Penetration testing toolkit

| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
|Precision (CSS & SQLi) 	| 98.5%			| 3 	|

| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| 29 		| 115 	| 6 	|
| Broken Authentication (A2) 				| 0 		| 3		| least |
| Excessive Data Exposure (A3) 				| 90  		| 145 	| 3		|
| Lack of Resources and Rate Limiting (A4) 	| 1 		| 11	| 3 	|
| Broken Function Level Authorization (A5)	| 12 		| 51	| 6	 	|
| Mass Assignment (A6) 						| 27 		| 27	| most	|
| Security Misconfiguration (A7) 			| 179 		| 743 	| 7		|
| Injection (A8) 							| 55 		| 133	| 4		|
| Improper Assets Management (A9) 			| 6 		| 15	| 9		|
| Insufficient Logging and Monitoring (A10) | 52 		| 95	| 4		|
	

	Goal: verify attack vectors and detect vuln (authentication, injection, and security misconfigurations)

	Pros:
		
		Higher detection of:
			- Mass Assignment

	Cons:
	
		Ranked last for open-source tools in detecting low severity vulnerabilities
	
		Lower detection of: 
		
			- Broken Authentication
			
	Additional Info:
	
		Java-based
		
	

<br>

## [8] Ethical Hacking: A Technique to Enhance Information Security

**Burp Suite:** mainly to track request and response between server and clients

<br>

## [A] TryHackMe - Burp Suite Basics

**Burp Suite**
- Java-based framework 
- Designed to serve as a comprehensive solution for conducting web application penetration testing
- Industry standard tool for hands-on **security assessments of web and mobile applications**, including those that rely on application programming interfaces (APIs).
- Invaluable tool for manual web application testing.
- Extensions can be written in Java, Python (using the Java Jython interpreter), or Ruby (using the Java JRuby interpreter)

| Features 																					| Attack Example 	|
|-------------------------------------------------------------------------------------------|-------------------|
| Captures and enables manipulation of all the HTTP/HTTPS traffic between a browser and a 
web server.		|
| Intercept requests and route them to various components within the Burp Suite framework 	|
| Ability to intercept, view, and modify web requests before they reach the target server	|
| Manipulate responses before they are received by our browser								|
| **Proxy:** enables interception and modification of requests and responses while 
interacting with web applications 															|
| **Repeater:** <br> 
-  allows for capturing, modifying, and resending the same request multiple times
<br> - useful when crafting payloads through trial and error (e.g., in SQLi)
<br> - testing the functionality of an endpoint for vulnerabilities 						|
| **Intruder:** allows for spraying endpoints with requests.
<br> Used for: brute-force attacks or fuzzing endpoints 									|
| **Decoder:** 
<br> - decode captured information
<br> - encode payloads before sending them to the target 									|
| **Comparer:** enables the comparison of two pieces of data at either the word or byte level 	|
| **Sequencer:** assesses the randomness of tokens (e.g. session cookie values or other supposedly randomly generated data). 	|


<br> 

**Burp Suite Professional** - unrestricted version of Burp Suite Community

| Features 	|
|-----------|
| An automated vulnerability scanner.											|
| A fuzzer/brute-forcer that isn't rate limited.								|
| Saving projects for future use and report generation.							|
| A built-in API to allow integration with other tools.							|
| Unrestricted access to add new extensions for greater functionality. 			|
| Access to the Burp Suite Collaborator (effectively providing a unique request 
catcher self-hosted or running on a Portswigger-owned server).					|

<br> 

**Burp Suite Enterprise**

| Features 	|
|-----------|
| Runs on a server and provides constant scanning for target web apps			|