# Nmap

[1] Footholder

[2] CyberCheck

[3] An Analysis of Vulnerability Scanners in Web Applications for VAPT

[4] AI

[5] Security Vulnerability Analysis using Penetration Testing Execution Standard (PTES): Case Study of Government’s Website

[6] Scanning of Web-Applications: Algorithms and Software for Search of Vulnerabilities “Code Injection” and “Insecure Design” (Sept 2023)

[7] SAT

<br>

## [8] Ethical Hacking: A Technique to Enhance Information Security

**Nmap:** open-source tool for network discovery

<br>

## [9] Security Vulnerability Analysis and Recommendations for Open Media Vault Cloud Server on Raspberry Pi

- **Nmap**: detect active hosts on a network and identify open ports
	- show ports
	
<br>

## [TryHackMe] Vulnversity

| Flag 	| Description 	|
|-------|---------------|
| -sV 				| Attempts to determine the version of the services running  							|
| -p <x> or -p- 	| Port scan for port <x> or scan all ports  											|
| -Pn 				| Disable host discovery and scan for open ports 										|
| -A 				| Enables OS and version detection, executes in-build scripts for further enumeration  	|
| -sC 				| Scan with the default Nmap scripts 													| 
| -v 				| Verbose mode 																			|
| -sU 				| UDP port scan 																		|
| -sS 				| TCP SYN port scan 																	|

 don't forget that ports on a higher range might be open, so constantly scan ports after 1000 (even if you leave checking in the background)