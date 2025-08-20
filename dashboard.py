import pandas as pd

# Step 1: Load the cleaned CSV
df = pd.read_csv("cleaned_output.csv",encoding='ISO-8859-1')

# Step 2: Show the full data
print("📄 All Court Cases Data:\n")
print(df)

# Step 3: Show summary info
print("\n🔢 Total Cases:", len(df))
print("🏛️ Unique Courts:", df['Court'].nunique())
print("👨‍⚖️ Unique Attorneys:", df['Attorney'].nunique())