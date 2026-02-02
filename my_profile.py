# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 05:27:04 2026

@author: User
"""

import streamlit as st
import pandas as pd

# Set page title
st.set_page_config(page_title="Lindokuhle Xulu — Researcher Profile & CV", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Profile", "Curriculum Vitae", "Projects", "Contact"],
)

# Replace dummy STEM data with relevant profile tables
education_data = pd.DataFrame({
    "Qualification": [
        "BSS Honours in Geography & Environmental Management",
        "BSS in Geography & Environmental Management"
    ],
    "Institution": [
        "University of KwaZulu‑Natal",
        "University of KwaZulu‑Natal"
    ],
    "Year": ["2020", "2019"]
})

skills_data = pd.DataFrame({
    "Skill": [
        "GIS & Remote Sensing (ArcGIS Pro, QGIS, ERDAS Imagine, Google Earth Pro)",
        "Environmental Monitoring & Laboratory Work (MiniSASS, water quality, soil sampling)",
        "Data Analysis & Statistics (Python, R, SQL, SPSS)",
        "Report Writing; MS Office (Word, Excel, PowerPoint)",
        "Dart & Flutter (basic app development)"
    ],
    "Proficiency": [
        "Advanced", "Advanced", "Basic-Intermediate", "Advanced","Basic"
    ]
})

experience_data = pd.DataFrame({
    "Role": [
        "Sustainability Coordinator / Teacher — Hilton College",
        "Residential Intern Teacher — Hilton College",
        "Education Coordinator — Youth for Marine Protected Areas (Y4MPAs)",
        "Environmental Education Officer — WESSA Treasure Beach Education Centre",
        "GIS & Remote Sensing Demonstrator — University of KwaZulu‑Natal",
        "Volunteer Peer Educator — UKZN Peer Education Programme"
    ],
    "Period": [
        "2024 – 2025",
        "2023 - 2023",
        "2022 – 2023",
        "2021 – 2022",
        "2020 - 2020",
        "2018 – 2020"
    ]})

certifications_data = pd.DataFrame({
    "Certification": [
        "ISO 14001:2015 – Environmental Management Systems (Alison)",
        "Nature-based Solutions for Disaster & Climate Resilience (UNEP)",
        "First Aid & Health and Safety (BS Training Services)",
        "Spatial Data Science: The New Frontier in Analytics (Esri)"
    ],
    "Year": ["2022", "2021", "2021", "2020"]
})

# Contact details (fill your real contact details here)
EMAIL = "xululindom@gmail.com"

# Page content
if menu == "Profile":
    st.title("Profile")
    st.markdown(
        """
        **Name:** Lindokuhle Xulu  
        **Field:** Geography & Environmental Management (Specialisation : GIS and Remote Semsing)
        """
    )
    st.image("https://pixabay.com/images/download/mountains-5051149_1920.jpg", caption="Mountains (Pixabay)")
    st.subheader("Professional Summary")
    st.write(
        "Postgraduate researcher with a BSocSci Honours in Geography & Environmental Management and practical experience in "
        "GIS, remote sensing, environmental monitoring,and laboratory practicals (water and soil testing). "
            )

    st.subheader("Core Skills")
    st.dataframe(skills_data, use_container_width=True)

    st.subheader("Education")
    st.dataframe(education_data, use_container_width=True)

elif menu == "Curriculum Vitae":
    st.title("Curriculum Vitae — Key Sections")
    st.subheader("Experience")
    st.dataframe(experience_data, use_container_width=True)

    st.subheader("Certifications")
    st.dataframe(certifications_data, use_container_width=True)

    st.subheader("Skills")
    st.markdown(
        "- **GIS & Remote Sensing:** ArcGIS Pro, QGIS, ERDAS Imagine, Google Earth Pro\n"
        "- **Data & Analysis:** Python, R, SQL, SPSS\n"
        "- **Laboratory & Fieldwork:** MiniSASS water quality monitoring, soil sampling, biodiversity surveys\n"
        "- **App Prototyping:** Dart & Flutter (basic app development for geospatial prototyping)\n"
        "- **Languages:** English (Fluent), isiZulu (Fluent)"
    )

    
elif menu == "Projects":
    st.title("Projects and Practical Work")

    st.subheader("Projects and Practical Work")
    st.markdown(
            "- **Research Project:** Geodatabase development, an innovative tool for natural resources management. A case study of the Beachwood Mangroves Nature Reserve, Durban, KwaZulu-Natal, South Africa. (QGIS, PostgreSQL, and PostGIS)\n"
            "- Hydrological modelling study for a suitability model and multi-criteria analysis of a hydroelectric power station in Bergville.\n"
			"Conducted an Environmental Impact Assessment (EIA) Basic Assessment and compiled a report, for sewer line installation at Tongaat\n"
            "- Completed a Soil Erosion and Land Degradation comparative assessment with rehabilitation measures for four study areas in the Eastern Cape, using GIS and Remote Sensing techniques\n"
            "- Conducted soil sampling using an auger and laboratory analysis, including Atterberg Limit tests and the hydrometer method\n" 
            "- Researched and collected quantitative data, analysed with IBM SPSS 25, assessing informal traders' challenges and survival strategies within the informal trading sector.\n"
            )

elif menu == "Contact":
    st.header("Contact Information")
    st.write(f"**Email:** {EMAIL}")

   

