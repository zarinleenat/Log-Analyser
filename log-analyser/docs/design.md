About:
The Log Analyser is a Python-based tool designed to parse web server logs (Apache/Nginx) and generate actionable insights.

Objectives:
- Parse large log files using Python and regex
- Provide statistics for network traffic analysis
- Visualise key metrics as charts 

Flow Description:
1. User runs log-analyser.py
2. Python reads the access.log file line by line
3. Regex parses log lines into structured fields (IP, date, method, path, status, size)
4. Data stored in a pandas DataFrame
5. Statistics computed:
6. Charts generated using matplotlib and saved to docs/

Components:
analyzer.py	--> Main script. Parses logs, computes stats, generates charts
logs/access.log	--> Sample log file input (Nginx/Apache)
docs/ --> Folder to store generated charts (PNG images)
Libraries --> pandas (data handling), matplotlib (visualization), re (regex parsing)

Log Format:
The tool currently supports standard Nginx/Apache log format as below.
127.0.0.1 - - [29/Oct/2025:10:00:00 +1000] "GET /index.html HTTP/1.1" 200 1024

Parsed Fields:
ip: client IP address
date: timestamp of the request
method: HTTP method (GET/POST/etc.)
path: requested path
protocol: HTTP protocol version
status: HTTP response status code
size: response size in bytes

Future Enhancements:
Detect anomalies: repeated failed logins, spikes in traffic