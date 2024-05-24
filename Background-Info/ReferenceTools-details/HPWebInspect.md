# HP WebInspect

<br> 

## [7] SAT

| Rate 						| Percentage 	| Rank 	|
|---------------------------|---------------|-------|
|Precision (CSS & SQLi) 	| 44.1%			| low 	|

| OWASP Top 10 								| Detected 	| Most 	| Rank 	|
|-------------------------------------------|-----------|-------|-------|
| Broken Object Level Authorization (A1) 	| 67 		| 115 	| 2 	|
| Broken Authentication (A2) 				| 0 		| 3		| least |
| Excessive Data Exposure (A3) 				| 90  		| 145 	| 3		|
| Lack of Resources and Rate Limiting (A4) 	| 2 		| 11	| 2 	|
| Broken Function Level Authorization (A5)	| 30 		| 51	| 2	 	|
| Mass Assignment (A6) 						| 27 		| 27	| most	|
| Security Misconfiguration (A7) 			| 180 		| 743 	| 5		|
| Injection (A8) 							| 52 		| 133	| 5		|
| Improper Assets Management (A9) 			| 15 		| 15	| most	|
| Insufficient Logging and Monitoring (A10) | 85 		| 95	| most	|
	
	Definition: launch attacks on web systems
	
	Pros:
		
		Higher detection of:
			- Mass Assignment
			- Improper Assets Management
			- Insufficient Logging and Monitoring

	Con: 
		
		Lower detection of: 
		
			- Broken Authentication