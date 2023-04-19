import streamlit as st
import pandas as pd
from faker import Faker
fake = Faker()

def generate_random_data(faker_function, num_rows):
    result = []
    for _ in range(num_rows):
        result.append(faker_function())
    return result

def create_fake_data_df(fields_to_generate, num_rows):
    data = {}
    for field_name, faker_function in fields_to_generate.items():
        data[field_name] = generate_random_data(field_mapping[faker_function], num_rows)
    return pd.DataFrame(data)

def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

field_mapping = {
    'Name': fake.name,
    'Email': fake.email,
    'Phone Number': fake.phone_number,
    'Date of Birth': fake.date_of_birth,
    "Suffix": fake.suffix,
    'SSN': fake.ssn,
    'EIN': fake.ein,
    'IBAN': fake.iban,
    'ISBN': fake.isbn13,
    'Job': fake.job,
    'Company': fake.company,
    'Address': fake.address,
    'Building Number': fake.building_number,
    'Street Address': fake.street_address,
    'Street Name': fake.street_name,
    'State': fake.state,
    'Country': fake.country,
    'City': fake.city,
    'Postal Code': fake.postcode,
    'Text': fake.text,
    'Username': fake.user_name,
    'Password': fake.password,
    'URL': fake.url,
    'Domain Name': fake.domain_name,
    'Currency': fake.currency,
    'Credit Card Number': fake.credit_card_number,
    'Credit Card Expiration': fake.credit_card_expire,
    'Credit Card Provider': fake.credit_card_provider,
    'Credit Card Security Code': fake.credit_card_security_code,
    'IPv4 Address': fake.ipv4,
    'IPv6 Address': fake.ipv6,
    'User Agent': fake.user_agent,
    'File Name': fake.file_name,
    'Longitude': fake.longitude,
    'Latitude': fake.latitude,
    'Timezone': fake.timezone,
    'Language': fake.language_name,
    'Crypto Currency': fake.cryptocurrency_name,
    'Crypto Currency Code': fake.cryptocurrency_code,
    'Catchphrase': fake.catch_phrase,
    }

st.title("Synthetic Data Generator")

# generator_type = st.selectbox("Choose the generator type:", ("Table-based", "Network Graph"))

# if generator_type == "Table-based":
st.subheader("Define Fields to Generate Data For")
num_fields = st.number_input("Number of fields:", min_value=0, max_value=100, step=1, value=5)
num_rows = st.number_input("Number of rows to generate:", min_value=0, max_value=100000, step=1, value=100)
fields_to_generate = {}
for idx in range(num_fields):

    st.markdown(f"### Field {idx + 1}")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        field_name = st.text_input(f"Field {idx + 1} Name:")
    with col2:
        field_type = st.selectbox(f"Field {idx + 1} Type:", field_mapping.keys())
    with col3:
        st.write(f"Example Data: ", str((field_mapping[field_type]())))
    fields_to_generate[field_name] = field_type

def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

if st.button("Generate Table"):
    table = create_fake_data_df(fields_to_generate, num_rows)
    csv = convert_df(table)
    st.download_button("Download csv file", csv,
                       file_name=f"Synthetic Data Table.csv",
                       mime="text/csv")
    st.write(table.head())

# elif generator_type == "Network Graph":
#     st.warning("Network Graph generation is not implemented.")

