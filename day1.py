data = [10, None, 20, 10, "", 30, None, 40]

# Remove invalid values
filtered = [x for x in data if x not in (None, "")]

# Remove duplicates using set
unique = list(set(filtered))

# Sort
unique.sort()

removed_count = len(data) - len(unique)

print("Cleaned List:", unique)
print("Total Removed Values:", removed_count)