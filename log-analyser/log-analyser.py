import pandas as pd # for data manipulation and analysis
import re # for regular expressions
import matplotlib.pyplot as plt #for plotting graphs

# Path to my log file
LOG_FILE = "logs/nginx_logs.txt"

# Regex pattern for standard Nginx log format
pattern = re.compile(
    r'(?P<ip>\S+) - - \[(?P<date>.*?)\] "(?P<method>\S+) (?P<path>\S+) (?P<protocol>.*?)" (?P<status>\d{3}) (?P<size>\S+)'
)

# Initialise an empty list to store log data
data = []

# Read log file line by line
with open(LOG_FILE, "r", encoding="utf-8") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            data.append(match.groupdict())

# Create a dataframe from the parsed data
df = pd.DataFrame(data)
df["status"] = df["status"].astype(int)

# Display summary stats
print("Top 5 IP addresses by request count:")
top_ips = df["ip"].value_counts().head(5)
print(top_ips)

print("\nTop 5 requested paths:")
top_paths = df["path"].value_counts().head(5)
print(top_paths)

print("\nHTTP Status codes:")
status_counts = df["status"].value_counts()
print(status_counts)

print("\nTotal number of requests:", len(df))
total_no_of_IPs = df["ip"].nunique()
print("Total number of unique IPs:", total_no_of_IPs)

#Plotting the top 5 IPs
top_ips = df["ip"].value_counts().head(5)
top_ips.plot(kind="bar", title="Top 5 IP Addresses")
plt.xlabel("IP Address")
plt.ylabel("Number of Requests")
plt.tight_layout()
plt.savefig("docs/top_ips.png")
plt.show()

# Plot HTTP status codes
df["status"].value_counts().sort_index().plot(
    kind="bar", title="HTTP Status Code Distribution", color="skyblue"
)
plt.xlabel("Status Code")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("docs/status_codes.png")
plt.show()

print("\nCharts saved: docs/top_ips.png, docs/status_codes.png")