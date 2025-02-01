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

## Task 1 - Data Scraping and Collection Pipeline
### Telegram Scraping
Utilize the Telegram API or write custom scripts to extract data from public Telegram channels relevant to Ethiopian medical businesses. Use the following channels:
- [DoctorsET](https://t.me/DoctorsET)
- Chemed Telegram Channel
- [Lobelia Cosmetics](https://t.me/lobelia4cosmetics)
- [Yetenaweg](https://t.me/yetenaweg)
- [EAHCI](https://t.me/EAHCI)
- And many more from [Telegram Medicine Directory](https://et.tgstat.com/medicine)

### Image and Scraping
Collect images from the following Telegram channels for object detection:
- Chemed Telegram Channel
- [Lobelia Cosmetics](https://t.me/lobelia4cosmetics)

### Steps
1. **Use Python Packages:**
   - For Telegram scraping: `telethon`
2. **Developing Telegram Data Extraction Scripts:**
   - Write custom scripts to extract messages, images, and relevant metadata.
   - Alternatively, export content using the Telegram application.
3. **Storing Raw Data:**
   - **Initial Storage:** Store the raw scraped data in a temporary storage location, such as a local database or files, before processing it further.
4. **Monitoring and Logging:**
   - **Logging:** Implement logging to track the scraping process, capture errors, and monitor progress.