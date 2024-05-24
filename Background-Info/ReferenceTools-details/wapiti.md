# Wapiti

<br> 

## [7] SAT

**Wapiti (Open-Source Scanner):**

Def: Automates audit process
	
| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
|Precision (CSS & SQLi) 	| 53%			| 10 	|

| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| 5 		| 115 	| least	|
| Broken Authentication (A2) 				| 0 		| 3		| least |
| Excessive Data Exposure (A3) 				| 42  		| 145 	| 6		|
| Lack of Resources and Rate Limiting (A4) 	| 1 		| 11	| 3 	|
| Broken Function Level Authorization (A5)	| 18 		| 51	| 4	 	|
| Mass Assignment (A6) 						| 2 		| 27	| 10	|
| Security Misconfiguration (A7) 			| 223 		| 743 	| 4		|
| Injection (A8) 							| 10 		| 133	| 9		|
| Improper Assets Management (A9) 			| 0 		| 15	| least	|
| Insufficient Logging and Monitoring (A10) | 39 		| 95	| 8		|

	Use: detects Injection, CSS, Command Execution Attacks, CRLF Injection, and File Disclosure

	Cons: 
	
		unable to detect broken authentication and improper assets management
		
		Lower detection of: 
		
			- Improper Assets Management
			- Broken Object Level Authorization
			- Broken Authentication
			- Mass Assignment
			
* Additional Info:
	
	- generic command-line tool
		
	- requires minimum user interaction

<br>