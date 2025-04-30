from typing import Union
import pandas as pd

def generate_response(
    city: str,
    business_type: str,
    location_data: pd.DataFrame,
    business_info: pd.DataFrame,
    competitor_list: pd.DataFrame,
    license_list: pd.DataFrame,
    loan_list: list
) -> str:
    """Generate formatted response string"""
    response = [
        f"🚀 **Business Report: {business_type.title()} in {city.title()}**",
        "\n📍 **Best Locations**:"
    ]
    
    # Location Data
    if not location_data.empty:
        response.extend([
            f"- {row['area']} (Foot Traffic: {row['foot_traffic']})" 
            for _, row in location_data.iterrows()
        ])
    else:
        response.append("⚠️ No location data found")
    
    # Business Details
    response.append("\n📊 **Setup Guide**:")
    if not business_info.empty:
        info = business_info.iloc[0]
        response.extend([
            f"- Rental Size: {info['rental_size']}",
            f"- Staff: {info['staff']}",
            f"- Equipment: {info['equipment']}",
            f"- Budget: {info['budget']}"
        ])
    else:
        response.append("⚠️ No business details available")
    
    # Competitors
    response.append("\n🏢 **Competitors**:")
    if not competitor_list.empty:
        response.extend([
            f"- {comp.strip()}" 
            for comp in competitor_list.iloc[0]['competitor_names'].split(';')
        ])
    else:
        response.append("⚠️ No competitor data found")
    
    # Licenses
    response.append("\n📝 **Licenses Required**:")
    if not license_list.empty:
        response.extend([
            f"- {lic.strip()}" 
            for lic in license_list.iloc[0]['required_licenses'].split(';')
        ])
    else:
        response.append("⚠️ No license information available")
    
    # Loans
    response.append("\n💰 **Loan Options**:")
    if loan_list:
        response.extend([f"- {loan['Loan Name']}" for loan in loan_list])
    else:
        response.append("⚠️ No loan information available")
    
    return "\n".join(response)
