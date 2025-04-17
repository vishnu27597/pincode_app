import streamlit as st
import pandas as pd

# List of metro cities
metro_cities = [
    "DELHI", "MUMBAI", "BENGALURU", "CHENNAI", 
    "KOLKATA", "HYDERABAD", "AHMEDABAD", "PUNE"
]

# List of special regions
special_regions = [
    "Jammu and Kashmir", "Kerala", "Arunachal Pradesh", "Assam", "Manipur", 
    "Meghalaya", "Mizoram", "Nagaland", "Tripura", "Sikkim", "Andaman and Nicobar",
    "Lakshadweep"
]

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("pincodes.csv")
    df['Pincode'] = df['Pincode'].astype(str).str.zfill(6)  # Ensure pincodes are 6-digit strings
    return df

df = load_data()

st.title("Indian Pincode Classifier")

# User input for pincode
input_pincode = st.text_input("Enter a 6-digit Indian Pickup Pincode:")

if input_pincode:
    if input_pincode in df['Pincode'].values:
        # Retrieve the district and state for the input pincode
        input_row = df[df['Pincode'] == input_pincode].iloc[0]
        input_district = input_row['District']
        input_state = input_row['State']

        # Classify pincodes
        def classify(row):
            if row['District'] == input_district and row['State'] == input_state:
                return "INTRA CITY"
            elif row['State'] == input_state:
                return "INTRA STATE"
            elif row['District'] in metro_cities and input_district in metro_cities: 
                return "METRO TO METRO"
            elif row['State'] in special_regions:
                return "SPECIAL REGION"
            else:
                return "REST OF INDIA"

        df['Category'] = df.apply(classify, axis=1)

        # Display results
        st.subheader("Classification Results")
        st.dataframe(df[['Pincode', 'District', 'State', 'Category']])

        # Download option
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='classified_pincodes.csv',
            mime='text/csv',
        )
    else:
        st.error("Pincode not found in the dataset.")
