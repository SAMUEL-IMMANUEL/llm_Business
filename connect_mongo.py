import pandas as pd

# Load the generated dataset
df = pd.read_csv("generated_business_data.csv")

# Take user input
user_input = input("Enter your query (example: Bangalore coffee shop): ")
user_input = user_input.strip().lower()

# Function to check if user_input matches any row
def is_match(row, user_query):
    combined_text = f"{row['Business_Name']} {row['Address_City']} {row['Business_Category']} {row['Business_SubCategory']} {row['Address_Area_Locality']}"
    return user_query in combined_text.lower()

# Filter matching rows
matching_rows = df[df.apply(lambda row: is_match(row, user_input), axis=1)]

# Display results
print("\nMatching Places:")
if not matching_rows.empty:
    for idx, row in matching_rows.iterrows():
        print(f"Business: {row['Business_Name']}")
        print(f"City: {row['Address_City']}")
        print(f"Category: {row['Business_Category']}")
        print(f"Sub-Category: {row['Business_SubCategory']}")
        print(f"Foot Traffic: {row['Approx_Foot_Traffic_Level']}")
        print(f"Competitors: {row['Example_Competitor_Names']}")
        print(f"Locality: {row['Address_Area_Locality']}")
        print("------")
else:
    print("No matching places found.")
