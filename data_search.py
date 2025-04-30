import pandas as pd
import re
import ollama
import json
from typing import Tuple

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()
    return df

def load_data() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Load all CSV files and return DataFrames"""
    city_df = pd.read_csv('data/city_locations(1).csv')
    business_df = pd.read_csv('data/business_categories(1).csv')
    competitor_df = pd.read_csv('data/competitors(1).csv')
    license_df = pd.read_csv('data/licenses(1).csv')
    bank_loans_df = pd.read_csv('data/bank_loans(1).csv')
    
    return (
        normalize_columns(city_df),
        normalize_columns(business_df),
        normalize_columns(competitor_df),
        normalize_columns(license_df),
        normalize_columns(bank_loans_df)
    )

def interpret_query(query: str) -> dict:
    """Use Ollama to extract business type and city"""
    try:
        response = ollama.generate(
            model="mistral",  # updated to mistral
            prompt=f"""
You are a helpful assistant. Extract ONLY the business type and city from this query: "{query}".
Return ONLY a JSON object like this:
{{
    "business_type": "business type here",
    "city": "city name here"
}}
No extra words, just the JSON.
"""
        )
        raw_text = response["response"]
        print("\n🔵 Ollama Raw Response:", raw_text)

        # Extract JSON from the response
        json_match = re.search(r'\{.*\}', raw_text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        else:
            raise ValueError("No JSON object found in model response.")
    except Exception as e:
        print(f"⚠️ Parsing Error: {e}")
        return {"business_type": None, "city": None}

def search_business_info(
    city: str, 
    business_type: str,
    city_df: pd.DataFrame,
    business_df: pd.DataFrame,
    competitor_df: pd.DataFrame,
    license_df: pd.DataFrame,
    bank_loans_df: pd.DataFrame
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, list, str]:
    """Search business information across all datasets"""
    city = city.strip().lower()
    business_type = business_type.strip().lower()

    location_data = city_df[city_df['city'].str.lower() == city]
    business_info = business_df[business_df['business'].str.lower() == business_type]
    competitor_list = competitor_df[
        (competitor_df['business'].str.lower() == business_type) &
        (competitor_df['city'].str.lower() == city)
    ]
    license_list = license_df[license_df['business'].str.lower() == business_type]
    
    loan_options = bank_loans_df[bank_loans_df['business'].str.lower() == business_type]
    loan_list = []
    if not loan_options.empty:
        loans = loan_options.iloc[0]['eligible_loans'].split(';')
        loan_list = [{"Loan Name": loan.strip()} for loan in loans]

    return location_data, business_info, competitor_list, license_list, loan_list, business_type
