# Logs guven

logs = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

# Initialize counters

counts = {"ERROR": 0, "INFO": 0, "WARNING": 0}

# Process logs (Ignore case sensitivity)

for log in logs:
    upper_log = log.upper()
    if "ERROR" in upper_log:
        counts["ERROR"] += 1
    elif "INFO" in upper_log:
        counts["INFO"] += 1
    elif "WARNING" in upper_log:
        counts["WARNING"] += 1

# Results

print("Log Counts:", counts)

# Bonus: Find most frequent log type

most_frequent = max(counts, key=counts.get)
print(f"Most Frequent: {most_frequent}")