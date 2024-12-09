import streamlit as st
import pandas as pd
import plotly.express as px

# App Configuration
st.set_page_config(page_title="Pesticides Use Dashboard", page_icon="🌾", layout="wide")

# Load Data Function
@st.cache_data
def load_data():
    return pd.read_csv("pesticides.csv")

# Load Dataset
data = load_data()

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Country Analysis", "Global Trends"])

# Home Page
# Home Page
if page == "Home":
    st.title("🌍 Crop Protection and Pesticide Usage Trends")
    st.write("""
    Welcome to the **Pesticides Use Dashboard**. This app allows you to explore global pesticide usage data.
    """)

    # Overview of the Data
    st.header("📊 Overview of the Data")
    st.dataframe(data.head(10))

    # Key Statistics
    st.header("🔍 Key Statistics")
    st.write("Summary of pesticide usage data:")
    st.table(data[['Year', 'Value']].describe().applymap('{:.2f}'.format))

    # Top 10 Countries by Pesticide Usage
    st.header("🌍 Top 10 Countries by Pesticide Usage")
    top_countries = data.groupby('Area')['Value'].sum().sort_values(ascending=False).head(10)
    
    # Plotly Bar Chart
    fig = px.bar(
        top_countries, 
        x=top_countries.index, 
        y=top_countries.values,
        labels={'x': "Country", 'y': "Total Pesticide Use (tonnes)"},
        title="Top 10 Countries by Total Pesticide Use"
    )
    st.plotly_chart(fig)


# Country-Specific Analysis Page
elif page == "Country Analysis":
    st.title("🌍 Country-Specific Analysis")
    st.write("Explore pesticide usage trends for specific countries over time.")

    # Country Selection
    country = st.selectbox("Select a Country", data['Area'].unique())

    # Add Year Range Slider
    min_year = int(data['Year'].min())
    max_year = int(data['Year'].max())
    year_range = st.slider(
        "Select Year Range", 
        min_value=min_year, 
        max_value=max_year, 
        value=(min_year, max_year)  # Default range
    )

    # Filter Data by Country and Year Range
    filtered_data = data[
        (data['Area'] == country) & 
        (data['Year'] >= year_range[0]) & 
        (data['Year'] <= year_range[1])
    ]

    # Display Filtered Data and Visualization
    if not filtered_data.empty:
        st.subheader(f"Pesticide Usage in {country} ({year_range[0]} - {year_range[1]})")
        fig = px.line(
            filtered_data, 
            x="Year", 
            y="Value", 
            title=f"Pesticide Usage Trends in {country}",
            labels={"Value": "Pesticide Use (tonnes)", "Year": "Year"}
        )
        st.plotly_chart(fig)
    else:
        st.warning("No data available for the selected year range.")

# Global Trends Page
elif page == "Global Trends":
    st.title("📈 Global Trends")
    st.write("Explore global pesticide usage trends with an interactive map.")

    # Add Year Range Slider for Global Trends
    year = st.slider(
        "Select a Year", 
        int(data['Year'].min()), 
        int(data['Year'].max()), 
        int(data['Year'].min())
    )

    # Filter Data for Selected Year
    filtered_global_data = data[data['Year'] == year]

    # Global Choropleth Map
    if not filtered_global_data.empty:
        fig = px.choropleth(
            filtered_global_data, 
            locations="Area", 
            locationmode="country names", 
            color="Value",
            hover_name="Area",
            title=f"Global Pesticide Usage in {year}"
        )
        st.plotly_chart(fig)
    else:
        st.warning("No data available for the selected year.")
