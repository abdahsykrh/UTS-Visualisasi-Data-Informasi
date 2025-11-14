import pandas as pd

# Load dataset
df = pd.read_csv("earthquakes_cleaned_100.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Create Year and Month columns
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

# Display summary info
print("Jumlah data:", len(df))
print("5 data teratas:")
print(df.head())

# Save final cleaned dataset
df.to_csv("earthquakes_cleaned_final.csv", index=False)

print("Preprocessing selesai! File disimpan sebagai earthquakes_cleaned_final.csv")
