import streamlit as st
import requests
from bs4 import BeautifulSoup
import urllib.parse

st.set_page_config(page_title="Doctor Finder - Practo.com", page_icon="🩺")


st.markdown("""
    <style>
    .main {
        background-color: #f0f4f8;
        padding: 20px;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
    }
    .subtitle {
        font-size: 20px;
        color: #34495e;
        text-align: center;
        margin-bottom: 30px;
    }
    .header-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 60%;
    }
    .doctor-card {
        background-color: white;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .doctor-name {
        font-size: 24px;
        font-weight: bold;
        color: #1abc9c;
    }
    .doctor-info {
        font-size: 16px;
        color: #2c3e50;
    }
    </style>
""", unsafe_allow_html=True)


st.image("https://t4.ftcdn.net/jpg/02/74/73/01/360_F_274730119_ht4FXz4R6RnIJgPk7WeNALxxaf524Jrb.jpg", caption='Find the Best Doctors in Your Area', use_column_width=True)

st.markdown("<div class='title'>Doctor Finder - Practo.com </div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Search for doctors by location and specialization</div>", unsafe_allow_html=True)


st.markdown(f"""
    <div style='color:#1abc9c; font-weight:bold; font-size:20px; margin-bottom:5px;'>
        Enter the location (eg. Delhi):
    </div>
""", unsafe_allow_html=True)
location = st.text_input(":")

specializations = ['Dermatologist', 'Cardiologist', 'General Physician', 'Pediatrician', 'Dentist','ENT Specialist','General Physician','Gynecologist','Rheumatologist','Neurologist','Orthopedic','Hematologist','Pediatrician','Psychiatrist','Radiologist','Urologist','Oncologist']
st.markdown(f"""
    <div style='color:#1abc9c; font-weight:bold; font-size:20px; margin-bottom:5px;'>
        Select specialization:
    </div>
""", unsafe_allow_html=True)
specialization = st.selectbox(":", specializations)


def doctors_info(location, specialization):
    encoded_specialization = urllib.parse.quote(
        f'[{{"word":"{specialization}","autocompleted":true,"category":"subspeciality"}}]')
    base_url = f"https://www.practo.com/search/doctors?results_type=doctor&q={encoded_specialization}&city={location}&page="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    profiles = []
    page_number = 1

    while True:
        response = requests.get(base_url + str(page_number), headers=headers)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, 'html.parser')

        if page_number == 1:
            total_count_element = soup.find("h1", class_="u-xx-large-font u-bold")
            total_count = total_count_element.text.strip() if total_count_element else "No data available."

        doctor_cards = soup.find_all("div", class_="info-section")
        if not doctor_cards:
            break

        for card in doctor_cards:
            profile = {
                "name": card.find("h2", {"data-qa-id": "doctor_name"}).text.strip() if card.find("h2", {"data-qa-id": "doctor_name"}) else "N/A",
                "specialization": card.find("div", class_="u-d-flex").text.strip() if card.find("div", class_="u-d-flex") else "N/A",
                "experience": card.find("div", {"data-qa-id": "doctor_experience"}).text.strip() if card.find("div", {"data-qa-id": "doctor_experience"}) else "N/A",
                "clinic_name": card.find("span", {"data-qa-id": "doctor_clinic_name"}).text.strip() if card.find("span", {"data-qa-id": "doctor_clinic_name"}) else "N/A",
                "practice_locality": card.find("span", {"data-qa-id": "practice_locality"}).text.strip() if card.find("span", {"data-qa-id": "practice_locality"}) else "N/A",
                "consultation_fees": card.find("span", {"data-qa-id": "consultation_fee"}).text.strip() if card.find("span", {"data-qa-id": "consultation_fee"}) else "N/A",
            }
            profiles.append(profile)

        page_number += 1

    return total_count, profiles

if st.button("Scrape"):
    if location and specialization:
        # Call the scraping function
        total_count, profiles = doctors_info(location, specialization)
        st.write(f"Total number of doctors available: {total_count}")
        st.markdown(f"""
    <div style='background-color:#1abc9c; padding:10px; border-radius:5px;'>
        <h3 style='color:white; text-align:center;'>Total number of doctors available: {total_count}</h3>
    </div>
""", unsafe_allow_html=True)

        
        for profile in profiles:
            st.markdown(f"""
                <div class='doctor-card'>
                    <div class='doctor-name'>{profile['name']}</div>
                    <div class='doctor-info'>Specialization: {profile['specialization']}</div>
                    <div class='doctor-info'>Experience: {profile['experience']}</div>
                    <div class='doctor-info'>Clinic: {profile['clinic_name']}</div>
                    <div class='doctor-info'>Locality: {profile['practice_locality']}</div>
                    <div class='doctor-info'>Consultation Fees: {profile['consultation_fees']}</div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.write("Please enter both location and specialization.")






