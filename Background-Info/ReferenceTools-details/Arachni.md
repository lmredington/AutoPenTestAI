# Arachni

<br> 

## [7] SAT

**Arachni (Open-Source Scanner):**
	
| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
|Precision (CSS & SQLi) 	| 81.32%		| 8 	|

| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| 28 		| 115 	| 7 	|
| Broken Authentication (A2) 				| 0 		| 3		| least |
| Excessive Data Exposure (A3) 				| 15  		| 145 	| 10	|
| Lack of Resources and Rate Limiting (A4) 	| 1 		| 11	| 3 	|
| Broken Function Level Authorization (A5)	| 17 		| 51	| 5	 	|
| Mass Assignment (A6) 						| 27 		| 27	| most	|
| Security Misconfiguration (A7) 			| 180 		| 743 	| 5		|
| Injection (A8) 							| 8 		| 133	| least	|
| Improper Assets Management (A9) 			| 13 		| 15	| 2		|
| Insufficient Logging and Monitoring (A10) | 25 		| 95	| least	|

	Pros:
		
		Higher detection of:
			- Mass Assignment

	Con: 
		
		Lower detection of: 
		
			- Broken Authentication
			- Injection
			- Insufficient Logging and Monitoring
	
	Additional Info:
	
		Based on modular and Ruby languages
		
		Trains itself by learning from HTTP responses received during the scanning and testing during assessment
		

<br>