# Appscan

[1] Footholder

[2] CyberCheck

[3] An Analysis of Vulnerability Scanners in Web Applications for VAPT

[4] AI

[5] Security Vulnerability Analysis using Penetration Testing Execution Standard (PTES): Case Study of Government’s Website

[6] Scanning of Web-Applications: Algorithms and Software for Search of Vulnerabilities “Code Injection” and “Insecure Design” (Sept 2023)

[7] SAT

[TryHackMe - OffSec Box]

To find potentially hidden pages on FakeBank's website
	
	gobuster -u http://fakebank.com -w wordlist.txt dir
	
| Flag 	| Description 	|
|-------|---------------|
| -u 	|  The target URL |
| -w 	|  Path to your wordlist 	|
| -e 	| Print the full URLs in your console 	|
| -U and -P 	| Username and Password for Basic Auth |
| -p <x> 	| Proxy to use for requests 	| 
| -c <http cookies> 	| Specify a cookie for simulating your auth 	|

this is an exercise you’d perform for companies to test for vulnerabilities in their web applications; find hidden pages to investigate for vulnerabilities.

**Vulniversity**

 is a tool used to brute-force URIs (directories and files), DNS subdomains, and virtual host names.
 
 you can find many wordlists under /usr/share/wordlists
 
 gobuster dir -u http://10.10.130.21:3333 -w <word list location>