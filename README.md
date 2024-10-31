# is477-fa24-Team_HouseCrime
This project investigates how crime rates impact housing rents/price in different Chicago neighborhoods over time. By analyzing data on crime incidents and housing rents, this study seeks to answer the question: Do crime rates in specific areas influence rental prices, and if so, how?

# Relationship Between Crime Rates and Housing Rents / price in Chicago

This project investigates how crime rates impact housing rents in different Chicago neighborhoods over time. By analyzing data on crime incidents and housing rents, this study seeks to answer the question: _Do crime rates in specific areas influence rental prices, and if so, how?_

## Table of Contents

- [Overview](#overview)
- [Datasets](#datasets)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Methodology](#methodology)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project explores the relationship between crime rates and housing rents across various regions of Chicago over time. The primary objective is to answer the question:

**"Do crime rates in different city areas influence housing rents?"**

### Motivation

Understanding the interplay between crime rates and housing rents can offer valuable insights for city planners, policymakers, real estate investors, and residents. In urban settings, crime rates can significantly impact neighborhood desirability, influencing housing demand and rental prices. High crime rates may deter potential tenants and reduce rental values, while low crime rates might attract renters, driving up demand and, consequently, rents.

### Research Questions

The analysis is structured around the following key questions:
1. **Primary Question**: Do crime rates in different areas of a city impact housing rents over time?
2. **Sub-Questions**:
   - How does the relationship between crime rates and housing rents vary across different geographic regions?
   - Are there particular types of crimes (e.g., violent crimes vs. property crimes) that have a more pronounced impact on housing rents?
   - Does the influence of crime rates on housing rents change over time?

### Methodology

To answer these questions, this project involves the following steps:
1. **Data Collection**: Collecting extensive crime data from the City of Chicago Data Portal and housing rent data from Zillow. Due to data size constraints, these datasets are stored externally and are processed locally.
2. **Data Cleaning and Preprocessing**: Cleaning, standardizing, and aligning the datasets by time and geographic location (zipcode level) to create a unified dataset suitable for time-series and geographic analysis.
3. **Exploratory Data Analysis (EDA)**: Visualizing trends in crime rates and housing rents, examining correlations, and identifying any temporal and regional patterns.
4. **Statistical Analysis and Modeling**: Using statistical techniques to quantify the relationship between crime rates and housing rents, with a focus on both general and region-specific trends.
5. **Insights and Recommendations**: Deriving insights that may guide urban planning, policy decisions, and real estate investments in Chicago.

### Expected Impact

This study aims to provide stakeholders with data-driven insights into how crime impacts housing markets in urban settings. By shedding light on the socio-economic dynamics between crime rates and housing rents, this research can support more informed decisions in urban planning, real estate investment, and public policy, ultimately contributing to community development and improved quality of life for city residents.


## Datasets

This project relies on two primary datasets: the **Chicago Crime Data** and the **Zillow Housing Rent Data**. These datasets were carefully collected, cleaned, and prepared to analyze the relationship between crime rates and housing rents across different regions of Chicago.

### 1. Chicago Crime Data (2001 - 2024)

- **Source**: The crime data was obtained from the [City of Chicago Data Portal](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data). This open-access platform provides detailed records of crime incidents reported to the Chicago Police Department, spanning from 2001 to the present. The data is updated frequently, making it a comprehensive source for exploring crime trends over time.
  
- **Access Method**: The dataset was exported using the **API endpoint**:
  - **API URL**: [https://data.cityofchicago.org/resource/ijzp-q8t2.json](https://data.cityofchicago.org/resource/ijzp-q8t2.json)
  - To retrieve the data, the following approach was used:
    1. **Exporting via Portal**: Initially, the dataset was accessed through the "Export Dataset" feature available on the portal. This allowed for a preview and sampling of the data.
    2. **API Retrieval**: To automate the process, the API endpoint was used to pull the data. Both **CSV** and **JSON** formats are available, but **CSV** was selected for ease of integration with other data sources.
    3. **API Query Configuration**: The API call parameters were configured to extract data spanning from 2001 to 2024, ensuring comprehensive coverage for the analysis.
  
- **Data Fields**:
  - The dataset includes numerous fields, but the key ones used for this study are:
    - **`ID`**: Unique identifier for each crime incident.
    - **`Case Number`**: Case number assigned by the Chicago Police Department.
    - **`Date`**: Timestamp of when the incident was reported.
    - **`Primary Type` and `Description`**: Types of crimes (e.g., theft, assault) and specific descriptions.
    - **`Arrest`**: Indicates whether an arrest was made.
    - **`Domestic`**: Indicates whether the incident was domestic in nature.
    - **`Location Description`, `Latitude`, and `Longitude`**: Geospatial information, including where the incident occurred.
    - **`Community Area`**: Numeric code representing the community area of Chicago.

- **Data Preprocessing**:
  - **Handling Missing Values**: Rows with missing values in essential fields (e.g., `Latitude`, `Longitude`) were removed, ensuring data integrity for spatial analysis.
  - **Date Formatting**: The `Date` column was initially in a timestamp format (e.g., `05/07/2020 10:24:00 AM`). This field was reformatted to a standard date format (`YYYY-MM-DD`) to facilitate time-series analysis. Additional columns for `Year` and `Month` were created to support temporal aggregation.
  - **Spatial Mapping**: To map crime incidents to specific zip codes, a **spatial join** was conducted using the `Latitude` and `Longitude` fields. A **shapefile** of Chicago's zip code boundaries was used to associate each crime with a corresponding `ZCTA5CE20` (zipcode). This involved:
    - **Shapefile Use**: A Chicago zipcode-level shapefile was downloaded from a reliable GIS source. The shapefile contained polygon boundaries for each zipcode, and a spatial join was conducted using the `sf` library in R to assign zipcodes to crime records.
    - **Third-Party API**: For incidents where `Latitude` and `Longitude` did not match directly with the shapefile, a third-party geocoding API was used to infer the zipcode.
  - **Aggregation**: The crime data was aggregated by `Year`, `Month`, and `ZCTA5CE20` to create monthly summaries. Key aggregated fields include:
    - `crime_count`: Total number of crime incidents.
    - `arrest_count`: Total number of arrests made.
    - `domestic_count`: Total number of domestic violence incidents.

### 2. Zillow Housing Rent Data (2000 - 2024)

- **Source**: The housing rent data was collected from [Zillow Research Data](https://www.zillow.com/research/data/). Zillow offers housing metrics across the U.S., including rent price data at different geographic levels. For this study, we focused specifically on zip code-level rent data for the Chicago area.

- **Access Method**: The dataset was downloaded directly from the Zillow Research website:
  - **Format**: Data was available in CSV format, containing monthly average rental prices for properties in Chicago, at the zipcode level, from **2000** to **2024**.
  - **Selection**: We selected the **zipcode-level rent data** to align geographically with the crime data.

- **Data Fields**:
  - **`RegionID`**: Unique identifier for each geographic area.
  - **`RegionName`**: Represents the zip code (e.g., `60614`).
  - **`City`, `CountyName`**: Identifies the city (`Chicago`) and county (`Cook County`).
  - **Monthly Rent Columns**: The dataset originally provided monthly rent information in a wide format, with each month from January 2000 to September 2024 represented as a separate column.

- **Data Preprocessing**:
  - **Wide-to-Long Transformation**: Since the dataset was originally in a wide format, it was transformed into a long format using R’s `pivot_longer()` function. This transformation allowed each row to represent a single month of rent data for a specific zipcode, with the following columns: `RegionName` (zipcode), `Year`, `Month`, and `price`.
  - **Date Parsing**: The original monthly columns (e.g., `2000-01-31`) were parsed to extract `Year` and `Month`, aligning with the temporal structure of the crime data.
  - **Column Selection**: Essential columns, such as `RegionName` (zipcode), `City`, and `CountyName`, were retained for analysis, while unnecessary columns (`SizeRank`) were dropped to streamline the dataset.
  - **Handling Missing Values**: Rows with missing rental data were either imputed (using historical averages for that zipcode) or removed to ensure that each region had consistent time series coverage.

### Summary

Both datasets underwent detailed preprocessing to ensure consistency and enable effective integration. By transforming both datasets into a common structure—centered on `Year`, `Month`, and `ZCTA5CE20` (zipcode)—they were merged to create a unified dataset. This integrated dataset serves as the foundation for exploring whether and how crime rates influence housing rents in different Chicago neighborhoods over time.

The preprocessing involved:
- **Aligning Time Frames**: Ensuring both datasets cover a consistent time frame (2000-2024).
- **Standardizing Geographic Levels**: Using zipcodes to enable a regional analysis of the relationship between crime rates and housing rents.
- **Temporal and Spatial Aggregation**: Aggregating the crime data by `Year`, `Month`, and zipcode, and transforming housing rent data into a comparable long format.

The resulting combined dataset is ready for detailed time-series analysis, helping us uncover the dynamics between crime rates and housing rents in Chicago.

## Installation

To replicate the analysis in this project, you’ll need to set up your environment with the necessary tools, dependencies, and data. Follow the steps below to get started.

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/repository-name.git
cd repository-name
```

### 2. Install Required Software

Make sure you have the following software installed on your machine:

R (version 4.0 or higher)
RStudio (optional but recommended for running R scripts)
Python (if any Python scripts are used, e.g., for API calls or additional data processing)
Git (for version control and repository management)

### 3. Install R Packages

Open R or RStudio, and install the required R packages by running the following commands. This project uses R packages for data manipulation, visualization, and spatial analysis.

```bash
# Install necessary packages
install.packages(c("tidyverse", "sf", "lubridate", "jsonlite"))
```

#### Explanation of Required R Packages
tidyverse: For data manipulation and visualization (includes ggplot2, dplyr, and tidyr).
sf: For spatial operations and handling shapefiles, which are used to map crime data to zipcodes.
lubridate: For handling and manipulating date-time objects.
jsonlite: For working with JSON data in case any data is pulled in JSON format.

### 4. Access the Datasets

Due to the large size of the datasets, they are not stored directly in this repository. Follow the instructions below to download each dataset:

#### Chicago Crime Data (2001 - 2024)  (https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data)
Go to the City of Chicago Data Portal.
Click on Export and select CSV format to download the data directly.
Save the downloaded CSV file in the data/ folder within your cloned repository.

Alternatively, if you want to use the API to retrieve the data:
Use the following API endpoint: https://data.cityofchicago.org/resource/ijzp-q8t2.json
You can use curl or a Python/R script to download and save the data in CSV format.

#### Zillow Housing Rent Data (2000 - 2024)
Go to the Zillow Research Data page.
Under the Data section, locate the Zip Code-level Rent Data for the time period 2000-2024.
Download the file in CSV format and save it in the data/ folder.

### 5. Setting Up Shapefile for Spatial Mapping
If your analysis involves mapping crime data to zipcodes, you will need a shapefile of Chicago’s zipcode boundaries. You can download this from a reliable GIS data source such as:
#### - Chicago Data Portal or TIGER/Line Shapefiles from the U.S. Census Bureau.

Save the shapefile (and its associated files like .shp, .shx, .dbf, etc.) in the data/ folder. This will allow the sf package to perform spatial joins between crime data and zipcode regions.


### 6. Run the Project
Once all dependencies and datasets are in place, you can run the analysis scripts:

Open RStudio.
Load the main R script for preprocessing and analysis (e.g., scripts/data_analysis.R).
Execute the script to reproduce the analysis and generate visualizations.

## Usage

Once the environment is set up and the necessary datasets are downloaded, follow the instructions below to run the analysis.

### 1. Data Preprocessing

Before conducting the main analysis, you’ll need to preprocess the data. The preprocessing scripts clean, structure, and merge the datasets to create a unified dataset for analysis.

1. **Open the preprocessing script**:
   - Open `scripts/data_preprocessing.R` in RStudio or your preferred R editor.
2. **Run the preprocessing code**:
   - Execute the script line by line or as a whole to clean and prepare the data. This will:
     - Standardize date formats and extract `Year` and `Month`.
     - Filter and remove rows with missing values in essential columns.
     - Perform spatial mapping to align crime data with zipcode regions using shapefiles.
     - Merge the crime and housing datasets by `ZCTA5CE20` (zipcode), `Year`, and `Month`.
3. **Output**:
   - The processed and merged dataset will be saved in the `output/` directory as `Combined_Housing_Crime_Data.csv` for use in the analysis.

### 2. Exploratory Data Analysis (EDA)

With the cleaned dataset, you can now explore the data to understand trends and relationships between crime rates and housing rents.

1. **Open the EDA script**:
   - Open `scripts/data_analysis.R`.
2. **Run EDA code**:
   - This script contains code for generating initial visualizations and summaries, including:
     - **Time-Series Plots**: Showing trends in housing rents and crime rates over time.
     - **Correlation Analysis**: Assessing relationships between crime and rent variables.
     - **Geographic Visualizations**: Mapping crime rates and rent levels by zipcode.

3. **Output**:
   - Visualizations and summary tables will be saved in the `output/` folder for review.

### 3. Main Analysis

Once EDA is complete, the main analysis script can be run to answer the primary research question: **Do crime rates in different city areas influence housing rents?**

1. **Open the main analysis script**:
   - Open `scripts/main_analysis.R`.
2. **Run the analysis code**:
   - This script contains statistical models and tests designed to quantify the impact of crime rates on housing rents over time and across regions. Methods may include:
     - **Regression Analysis**: Exploring the relationship between crime rates and housing rents.
     - **Time-Series Analysis**: Assessing the temporal dynamics of crime and housing rents.
     - **Region-Specific Analysis**: Analyzing how the relationship varies by different Chicago neighborhoods.

3. **Output**:
   - Results from the statistical models, including coefficients and p-values, will be saved in the `output/` directory.
   - Final visualizations, such as overlay plots of crime and rent trends, will also be generated in the `output/` folder.

### 4. Viewing Results

All generated outputs, including cleaned datasets, plots, and statistical summaries, will be available in the `output/` directory.

1. **Access visualizations**:
   - Review the PNG or PDF files in the `output/visualizations/` subfolder for insights on trends and patterns.
2. **Examine data summaries**:
   - Check `output/summary_tables/` for CSV files containing descriptive statistics and model summaries.
3. **Interpretation**:
   - Use the insights gained from the visualizations and statistical summaries to interpret the relationship between crime rates and housing rents. Key results can guide urban planning, real estate investment, and policy decisions.


## License

This project relies on data from external sources with distinct licensing terms:

### 1. Chicago Crime Data (2001 - 2024)

The **Chicago Crime Data** is sourced from the [City of Chicago Data Portal](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data) and is typically provided under a **Public Domain Dedication**.

- **License**: This data is generally available under the **Open Data Commons Public Domain Dedication and License (PDDL)** or a similar public domain license, allowing free use, modification, and distribution without restrictions.
- **Attribution**: While not required by the license, it is good practice to attribute the **City of Chicago** as the data provider.

**Suggested Attribution**:
> Data sourced from the City of Chicago Data Portal. Available at: [https://data.cityofchicago.org/](https://data.cityofchicago.org/).

Please review the City of Chicago’s data portal terms to confirm any updates to their licensing or use terms.

### 2. Zillow Housing Rent Data (2000 - 2024)

The **Zillow Housing Rent Data** is obtained from [Zillow Research Data](https://www.zillow.com/research/data/). This data is subject to Zillow's data usage terms, typically restricted to non-commercial, research, and personal use only.

- **License**: The data is available under **Zillow’s Data Licensing Agreement**, which limits its use to non-commercial and personal research. Redistribution or commercial use requires Zillow’s explicit permission.
- **Attribution**: Proper attribution to **Zillow Research** is required for public use or referencing of their data.

**Suggested Attribution**:
> Housing rent data provided by Zillow Research. Available at: [https://www.zillow.com/research/data/](https://www.zillow.com/research/data/).

For exact usage terms and potential updates, please review Zillow’s licensing agreement on their website.



