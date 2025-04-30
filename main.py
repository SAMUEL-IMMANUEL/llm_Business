from data_search import load_data, search_business_info, interpret_query
from response_generator import generate_response
from typing import NoReturn

def main() -> NoReturn:
    print("🌟 Business Advisor (Ollama-Powered) 💼\n")
    
    # Load all data
    city_df, business_df, competitor_df, license_df, bank_loans_df = load_data()
    
    while True:
        try:
            query = input("\nQuery (e.g., 'Open a gym in Chennai'): ").strip()
            if query.lower() == 'exit':
                break
            
            # Parse query with Ollama
            parsed = interpret_query(query)
            if not parsed["business_type"] or not parsed["city"]:
                print("❌ Could not understand. Try: 'Coffee shop in Bangalore'")
                continue
            
            # Search data
            city = parsed["city"].lower()
            business_type = parsed["business_type"].lower()
            results = search_business_info(
                city, business_type, 
                city_df, business_df, 
                competitor_df, license_df, 
                bank_loans_df
            )
            location_data, business_info, competitor_list, license_list, loan_list, _ = results
            
            # Generate response
            print("\n" + generate_response(
                city, business_type, 
                location_data, business_info, 
                competitor_list, license_list, 
                loan_list
            ))
            print("\n" + "="*60)
            
        except Exception as e:
            print(f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    main()
