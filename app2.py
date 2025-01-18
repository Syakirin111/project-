import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "AGE_GROUP": ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90-100"],
    "DIABETES": [1614, 3131, 20485, 35386, 36445, 30453, 18604, 9519, 3568, 559],
    "COPD": [1200, 2200, 18800, 29000, 34000, 29000, 17000, 8500, 3300, 500],
    "ICU": [800, 1800, 15000, 25000, 30000, 25000, 14000, 7000, 2900, 400],
    "OUTCOME": ["RECOVERED", "RECOVERED", "DECEASED", "DECEASED", "RECOVERED", "RECOVERED", "DECEASED", "DECEASED", "RECOVERED", "RECOVERED"]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Set page layout to wide
st.set_page_config(page_title="Interactive Data Visualization", 
                   layout="wide", initial_sidebar_state="collapsed")

# Create two columns: one for inputs, one for visualization
col1, col2 = st.columns([1, 3])

# Column 1: Inputs (Left container)
with col1:
    # Title of the Streamlit App
    st.title(''' :red[Welcome to] :orange[Interactive] :green[Data Visualization]''')

    # Add a radio button to switch between charts (simulating tabs)
    chart_selection = st.radio("Select a Chart to Display", ["Bar Chart by Age Group", "Outcome Distribution (Pie Chart)", "Line Chart for Disease and ICU Correlation"])

    # Dropdown to Select Disease
    disease = st.selectbox("Select a Disease to Show Data", ["DIABETES", "COPD", "ICU"])

    # Age Group Selection Slider
    age_group = st.slider("Select Age Group", 0,10, value=5)

# Column 2: Visualization (Right container)
with col2:
    # 1. Bar chart for selected disease by age group
    if chart_selection == "Bar Chart by Age Group":
        st.subheader(f"Bar Chart of {disease} by Age Group")
        chart, ax = plt.subplots(figsize=(6, 3))
        sns.barplot(x="AGE_GROUP", y=disease, data=df, ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        ax.set_title(f"{disease} by Age Group")
        st.pyplot(chart)

    # 2. Pie chart of Outcome for the selected disease
    elif chart_selection == "Outcome Distribution (Pie Chart)":
        st.subheader(f"Outcome Distribution for {disease}")
        outcome_dist = df.groupby("OUTCOME")[disease].sum()
        chart, ax = plt.subplots(figsize=(6, 6))
        outcome_dist.plot(kind="pie", autopct="%1.1f%%", startangle=90, ax=ax, colors=["#66b3ff", "#ff6666"])
        ax.set_title(f"Outcome Distribution for {disease}")
        st.pyplot(chart)

    # 3. Line chart for ICU and selected disease correlation
    elif chart_selection == "Line Chart for Disease and ICU Correlation":
        st.subheader(f"Line Chart for {disease} and ICU Correlation")
        chart, ax = plt.subplots(figsize=(6, 3))
        sns.lineplot(x="AGE_GROUP", y=disease, data=df, ax=ax, label=disease)
        sns.lineplot(x="AGE_GROUP", y="ICU", data=df, ax=ax, label="ICU")
        ax.set_title(f"Correlation of {disease} and ICU Admission by Age Group")
        ax.legend()
        st.pyplot(chart)