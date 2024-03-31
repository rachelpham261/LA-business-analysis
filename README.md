# LA Business Profitability and Sales Growth Analysis

## Project Overview
This study leverages extensive datasets to explore the profitability and predictors of sales growth among businesses in Los Angeles. By segmenting the market, identifying optimal locations for new ventures, and predicting sales growth, the project aims to provide actionable insights for business owners in the LA area.

## Motivation
Given the high rate of new business failures, understanding and predicting factors contributing to sustained revenue and profitability is essential. This project aims to uncover these factors within the LA business landscape, focusing on location and demographic influences on sales growth.

## Contents
- `report.pdf`: A comprehensive report detailing the study's objectives, methodology, analysis, and conclusions.
- `presentation.pptx`: Slides summarizing the project's key insights and findings.
- `clustering.py`: Python script for performing cluster analysis on demographic data to identify distinct customer groups in Los Angeles.
- `linear.ipynb`: Python notebook for conducting linear regression to select the best ZIP code for opening a new business, targeting each customer cluster identified in the cluster analysis.

## Methodology and Insights
- **Cluster Analysis (`clustering.py`)**: Segments LA's market into six customer clusters based on demographic factors. This script uses K-Means clustering to organize locations into groups with similar demographic characteristics, facilitating market segmentation and targeted business strategies.
  
- **Linear Regression (`linear.ipynb`)**: Identifies the optimal ZIP codes for new businesses by predicting sales growth within each demographic cluster. This notebook runs linear regression and ranks ZIP codes to recommend the most promising locations for each customer cluster.

## Data Sources
The analysis employs datasets from the National Establishment Time-Series (NETS) Database and the US Census Bureau. These datasets provide a rich overview of LA's business landscape, including sales growth, demographics, business types, and owner demographics. Access the data [here](https://drive.google.com/drive/folders/1Lyi41lCyKckC5rGJWTYF9v9PkRiSy_n7?usp=sharing).

<!-- ## Key Skills and Tools
- **Python for Data Science**: Demonstrated proficiency in data cleaning, preprocessing, and analysis using Python, with libraries such as pandas, sklearn, and statsmodels.
- **Statistical Analysis**: Applied cluster analysis and linear regression techniques to uncover patterns and predict sales growth, showcasing the ability to derive actionable insights from complex datasets.
- **Visualization**: Utilized PCA for cluster visualization and seaborn for plotting, enhancing the interpretability of the clustering results. -->

## Getting Started
Begin by examining the `report.pdf` for a thorough understanding of the research and findings. The `presentation.pptx` offers a visual summary suitable for stakeholders. The `clustering.py` script and `linear.ipynb` notebook detail the analytical processes used to segment the market and identify optimal business locations.

## Acknowledgments
This project is a collaborative effort with Herat Devisha, Diego Estuar, Yannick Angouo Lopes, Andrew Morris, and Riley Nickel.