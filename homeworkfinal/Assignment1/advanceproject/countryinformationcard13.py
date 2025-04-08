import streamlit as st
import requests

def country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            country_info = data[0]
            name = country_info["name"]["common"]
            capital = country_info["capital"][0]
            region = country_info["region"]
            population = country_info["population"]
            area = country_info["area"]
            languages = ", ".join(country_info["languages"].values())
            currency = ", ".join([f"{v['name']} ({k})" for k, v in country_info["currencies"].items()])
            return name, capital, region, population, area, languages, currency
    else:
        st.error("Country not found. Please check the name and try again.")
        return None

def main():
    st.title("Country Information Card")
    country_name = st.text_input("Enter the country name:")
    
    if st.button("Get Country Info"):
        if country_name:
            info = country_data(country_name)
            if info:
                name, capital, region, population, area, languages, currency = info
                st.subheader(f"Information for {name}")
                st.write(f"**Capital:** {capital}")
                st.write(f"**Region:** {region}")
                st.write(f"**Population:** {population}")
                st.write(f"**Area:** {area} km²")
                st.write(f"**Languages:** {languages}")
                st.write(f"**Currency:** {currency}")
        else:
            st.warning("Please enter a country name.")

if __name__ == "__main__":
    main()
