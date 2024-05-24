# OWASP

<br> 

## [5] Security Vulnerability Analysis using Penetration Testing Execution Standard (PTES): Case Study of Government’s Website


<br> 

## [7] SAT

**ZAP (Open-Source Scanner):**
	
Definition: web security assessment tool	

| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
|Precision (CSS & SQLi) 	| 100%			| most 	|

| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| 26 		| 115 	| 8 	|
| Broken Authentication (A2) 				| 0 		| 3		| least |
| Excessive Data Exposure (A3) 				| 11  		| 145 	| least	|
| Lack of Resources and Rate Limiting (A4) 	| 11 		| 11	| most 	|
| Broken Function Level Authorization (A5)	| 8 		| 51	| 9	 	|
| Mass Assignment (A6) 						| 0 		| 27	| least	|
| Security Misconfiguration (A7) 			| 743 		| 743 	| most	|
| Injection (A8) 							| 13 		| 133	| 8		|
| Improper Assets Management (A9) 			| 4 		| 15	| 10	|
| Insufficient Logging and Monitoring (A10) | 36 		| 95	| 9		|

	
	Pros:
		
		Good to detect security configurations
		
		Ranked 1st for open-source tools in detecting low severity vulnerabilities
		
		Higher detection of:
		
			- Security Misconfiguration
			- Lack of Resources and Rate Limiting
	
	Cons:
	
		Lower detection of CSS, File Injection, and Insecure Communication	
		
		Lower detection of: 
		
			- Mass Assignment
			- Excessive Data Exposure
			- Broken Authentication