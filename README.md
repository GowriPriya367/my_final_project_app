# my_final_project_app
This is my final project for UNC Charlotte's DSBA-5122 - Visual Analytics course!

### Streamlit Link
[View my streamlit app here](https://gowri-final-project-app.streamlit.app/ "Click to view the dashboard")
### Data Link
[Kaggle](https://www.kaggle.com/datasets/patelris/crop-yield-prediction-dataset?resource=download)

## Introduction
This project provides an interactive Crop Protection and Pesticide Usage Trends to analyze global pesticide consumption patterns. Using a structured dataset, the app visualizes pesticide usage across different regions and years, offering insights into agricultural chemical consumption trends. The project leverages Streamlit for an intuitive user interface and Plotly for dynamic data visualizations.

## Data Operations / Abstraction Design
The dataset includes key attributes like Area (regions), Year (time period), and Value (pesticide usage in tonnes). The data is cleaned by handling missing values, removing unnecessary entries, and converting columns to appropriate formats. Users can filter the data by country and year range to explore trends. For Country-Specific Analysis, line charts display usage patterns over time, while Global Trends use choropleth maps for regional comparisons. The project combines Streamlit for the interface, Pandas for data handling, and Plotly for visualizations.

## Future Work
Future enhancements include adding crop-specific data, predictive models, geospatial analysis, and sustainability metrics to provide deeper insights and assess environmental impacts.
