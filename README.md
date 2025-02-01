# Ethiopian Medical Businesses Data Warehouse

## Overview
This project involves building a robust and scalable data warehouse to store and analyze data on Ethiopian medical businesses scraped from the web and Telegram channels. Additionally, the project integrates object detection capabilities using YOLO (You Only Look Once) to enhance data analysis. 

The data warehouse will enable centralized data storage, allowing comprehensive analyses to identify trends, patterns, and correlations in Ethiopian medical businesses. The implementation of ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) frameworks ensures clean, consistent, and actionable data.

## Features
- **Data Scraping and Collection Pipeline**: Extracts data from websites and Telegram channels.
- **Data Cleaning and Transformation Pipeline**: Ensures data consistency, deduplication, and formatting.
- **Object Detection using YOLO**: Analyzes images to detect relevant objects in the medical domain.
- **Data Warehouse Design and Implementation**: Centralized storage optimized for queries and reporting.
- **Data Integration and Enrichment**: Combines various datasets for enhanced insights.

## Architecture
The project follows a modular approach with the following components:
1. **Data Ingestion**
   - Web Scraping using `Scrapy`, `BeautifulSoup`
   - Telegram Data Extraction using `telethon`
   - APIs and external data sources
2. **ETL/ELT Pipelines**
   - Data Extraction
   - Data Cleaning using `pandas`
   - Data Transformation
   - Data Loading into the Data Warehouse
3. **Object Detection**
   - Image Processing using `OpenCV`
   - YOLO Model for detecting medical-related objects
4. **Data Storage and Querying**
   - PostgreSQL / BigQuery / Snowflake for data warehousing
   - Indexing and partitioning for efficient querying
5. **Visualization and Reporting**
   - Streamlit dashboards for real-time insights
   - BI tools for deeper analytics

## Technologies Used
- **Programming Languages**: Python
- **Libraries & Frameworks**: Scrapy, BeautifulSoup, pandas, OpenCV, telethon, YOLOv5
- **Databases**: PostgreSQL, Snowflake, BigQuery
- **Data Pipelines**: Airflow, Apache Kafka
- **Infrastructure**: Docker, Kubernetes

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
MIT License

## Contact
For inquiries, reach out at [samuelgashu11@gmail.com](mailto:samuelgashu11@gmail.com)
