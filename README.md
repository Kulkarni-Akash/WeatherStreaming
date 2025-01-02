# WeatherStreaming

## Overview
This project is designed to provide nearly live updates on weather conditions such as temperature, humidity, wind direction, wind speed, and more. By leveraging Azure services, the system fetches weather data from an API and processes it in real-time, displaying the information in Power BI dashboards.

## Project Flow
- Azure Functions fetch weather data from weatherapi.com every 30 seconds.
- The data is sent to Azure Event Hubs.
- Azure Stream Analytics processes the data in real-time.
- Power BI visualizes the processed data on interactive dashboards.

## Technologies Used
- Prgramming Language: Python
- Cloud: Azure
- Azure Service: Azure Function, Azure Eventhubs, Azure Stream Analytics, Azure Key Vault, PowerBI

## Architecture

**Stream Analytics Pipeline**
![streamAnalytics-pipeline](https://github.com/user-attachments/assets/886625f9-f1ba-4bbd-bee5-f9eb4600632b)

1. **Azure Functions**
  - Purpose: To fetch weather details from [weatherapi.com](https://www.weatherapi.com/) every 30 seconds.
  - Process:
      - The Azure Function is triggered on a timer (every 30 seconds).
      - It retrieves the weather data from the API.
      - The fetched data is sent to Azure Event Hubs for further processing.

2. **Azure Event Hubs**
  - Purpose: Acts as a message broker to receive and store the data sent by Azure Functions.
  - Process:
      - Receives the weather data from Azure Functions.
      - Streams the data to Azure Stream Analytics for real-time analysis.

3. **Azure Stream Analytics**
  - Purpose: Processes the weather data in real-time.
  - Process:
      - Reads data from Azure Event Hubs.
      - Performs transformations and computations on the incoming data.
      - Sends the processed data to Power BI for visualization.
        
4. **Azure Key Vault**
- purpose: To store the API Key/secret creds
        
4. **Power BI**
  - Purpose: Provides an interactive dashboard for visualizing the live weather data.
  - Process:
      - Displays all the metrics related to weather(temp, humidity, windspeed, wind direction, feels_like, and so on...)
      - Automatically refreshes to reflect the latest data.

## How to Run
- Clone this repository.
- Set up an Azure Function to fetch data from [weatherapi.com](https://www.weatherapi.com/).
- Configure Azure Event Hubs to receive the data.
- Create a Stream Analytics job to process the data and send it to Power BI.
- Use Power BI to design and publish a dashboard for visualization.

## Prerequisites
- Azure Subscription
- API key from [weatherapi.com](https://www.weatherapi.com/)
- Power BI account
