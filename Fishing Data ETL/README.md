# Fishing Data Entry ETL

## 1. Introduction

### Overview
I initiated this project when I was working for a canned sardine manufacturer. This project focuses on automating the extraction, transformation, and loading (ETL) of manually entered data from Google Sheets into a centralized database. The purpose is to eliminate manual data extraction processes, reduce errors, and improve efficiency in data management.

### Key Objectives
- Automate the extraction of data from multiple Google Sheets.
- Transform the data into a consistent format suitable for database storage.
- Load the transformed data into a relational database for easy access and analysis.
- Ensure scalability and maintainability of the ETL pipeline.
- Centralize data source for analytics.

### Technologies and Tools
- **Python**: For scripting the ETL process.
- **Google Sheets API**: To extract data from Google Sheets.
- **Pandas**: For data transformation and cleaning.
- **SQLAlchemy**: For database interaction and loading.
- **PostgreSQL**: As the target database for storing the data.

---

## 2. Problem Statement

### Challenge
The business relied on manual data entry in Google Sheets, which led to:
- **Inefficiencies**: Time-consuming manual extraction and consolidation of data.
- **Errors**: Human errors during data entry and extraction.
- **Lack of Centralization**: Data scattered across multiple sheets, making it difficult to analyze.

### Impact
- Delayed decision-making due to slow data processing.
- Increased operational costs from manual labor.
- Inconsistent data quality affecting business insights.

### Why Solving This Problem Was Critical
Automating the ETL process was essential to streamline operations, improve data accuracy, and enable real-time access to centralized data for better decision-making.

---

## 3. Design Process

### Steps Taken
1. **Data Collection**: Identified all Google Sheets containing manual data entries.
2. **Data Extraction**: Used the Google Sheets API to programmatically extract data.
3. **Data Transformation**: Cleaned and standardized data using Pandas (e.g., handling missing values, formatting dates).
4. **Pipeline Design**: Designed a modular ETL pipeline to handle multiple sheets and tables.
5. **Database Schema Design**: Created a relational database schema to store the transformed data.
6. **Stakeholder Collaboration**: Worked with stakeholders to validate requirements and ensure the solution met business needs.

### Tools and Methodologies
- **ETL Processes**: Automated extraction, transformation, and loading.
- **Data Modeling**: Designed a normalized database schema.
- **Agile Methodology**: Iterative development with regular feedback from stakeholders.

---

## 4. Implementation

### Development and Deployment
- Developed Python scripts to extract data from Google Sheets using the Google Sheets API.
- Used Pandas for data cleaning and transformation (e.g., removing duplicates, standardizing formats).
- Loaded the transformed data into a PostgreSQL database using SQLAlchemy.
- Deployed the ETL pipeline on the company's on-premise server for automated daily execution.

### Key Features
- **Automated Extraction**: Scheduled daily extraction of data from Google Sheets.
- **Interactive Logs**: Detailed logs for tracking pipeline execution and errors.
- **Scalable Design**: Modular pipeline to handle additional sheets or tables in the future.

### Challenges and Resolutions
- **Challenge**: API rate limits when extracting large datasets.
  - **Resolution**: Implemented pagination and rate-limiting mechanisms by extracting chunks of data.
- **Challenge**: Inconsistent data formats across sheets.
  - **Resolution**: Added robust data validation and transformation logic.

---

## 5. Results

### Outcomes and Benefits
- **Improved Efficiency**: Reduced data processing time from hours to minutes.
- **Cost Savings**: Eliminated manual labor costs associated with data extraction.
- **Better Decision-Making**: Centralized and up-to-date data enabled faster insights.

### Metrics Impacted
- **Data Processing Time**: Reduced by 90%.
- **Error Rate**: Decreased by 95%.
- **Stakeholder Satisfaction**: Positive feedback on data accessibility and accuracy.

### Feedback
- Stakeholders appreciated the automated solution and the ability to access real-time data.
- End-users reported fewer errors and improved usability.

---

## 6. Lessons Learned

### Key Takeaways
- Automation significantly improves efficiency and reduces errors.
- Collaboration with stakeholders is crucial for aligning the solution with business needs.
- Robust error handling and logging are essential for maintaining pipeline reliability.

### Areas for Improvement
- Implement real-time data synchronization instead of daily batches.
- Add data quality checks to ensure long-term reliability.

### Skills Gained
- Proficiency in Python for ETL processes.
- Experience with Google Sheets API and SQLAlchemy.
- Improved understanding of database design and data modeling.

