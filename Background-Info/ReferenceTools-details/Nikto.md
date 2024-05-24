# Nikto

<br> 

## [1] Footholder

<br> 

## [7] SAT

**Nikto (Open-Source Scanner):**
	
Use: Execute and scan for multiple items including malicious files/ programs, and outdated versions in both software libraries and web servers.

| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
|Precision (CSS & SQLi) 	| 71.4%			| 9 	|

| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| 18 		| 115 	| 10 	|
| Broken Authentication (A2) 				| 0 		| 3		| least	|
| Excessive Data Exposure (A3) 				| 18  		| 145 	| 9		|
| Lack of Resources and Rate Limiting (A4) 	| 0 		| 11	| least |
| Broken Function Level Authorization (A5)	| 4 		| 51	| least |
| Mass Assignment (A6) 						| 10 		| 27	| 9		|
| Security Misconfiguration (A7) 			| 545 		| 743 	| 2		|
| Injection (A8) 							| 8 		| 133	| least	|
| Improper Assets Management (A9) 			| 6 		| 15	| 9		|
| Insufficient Logging and Monitoring (A10) | 43 		| 95	| 7		|

	Provides: 
	- scan configuration files of web servers (ex: multiple index files, server fingerprinting, and HTTP calls settings)

	Pros:
		
		Higher detection of:
			- Security Misconfiguration

	Con: 
		
		Lower detection of: 
		
			- Broken Authentication
			- Lack of Resources and Rate Limiting
			- Broken Function Level Authorization
			- Injection
			-  Broken Object Level Authorization

<br>