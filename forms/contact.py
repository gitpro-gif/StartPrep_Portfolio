import streamlit as st
import re
import requests



WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Adress")
        message = st.text_area("your Message")
        submit_button = st.form_submit_button("Submit")
    
        if submit_button:
            if not WEBHOOK_URL:
                st.error("Webhook URL is not configured.")
                return

            if not name.strip() or not email.strip() or not message.strip():
                st.error("Please fill out all the fields.")
                return

            if not is_valid_email(email):
                st.error("Please enter a valid email address.")
                return

            # Prepare payload
            payload = {
                "name": name,
                "email": email,
                "message": message,
            }

            try:
                response = requests.post(WEBHOOK_URL, json=payload)
                if response.status_code == 200:
                    st.success("✅ Your message has been sent successfully!")
                else:
                    st.error(f"Something went wrong. Status code: {response.status_code}")
            except Exception as e:
                st.error(f"Error sending message: {e}")