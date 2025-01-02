# To run this code have ton create a function app with timer trigger.
# Corn time will be */30 * * * * * (every 30 secs).

# Do not modify the function app code
# Add this code inside to the function app code

from azure.identity import DefaultAzureCredential
from azure.eventhub import EventHubProducerClient, EventData
import json
import requests
from azure.keyvault.secrets import SecretClient

EVENT_HUB_NAME='' # Add your eventhub name
EVENT_HUB_NAMESPACE='' # Add your evenhub host name

credential = DefaultAzureCredential()

producer = EventHubProducerClient(
    fully_qualified_namespace=EVENT_HUB_NAMESPACE,
    eventhub_name=EVENT_HUB_NAME,
    credential=credential
)

def send_event(event):
    event_data_batch = producer.create_batch()
    event_data_batch.add(EventData(json.dumps(event)))
    producer.send_batch(event_data_batch)

def get_current_weather(base_url, api_key, location):
    current_weather_url = f"{base_url}/current.json"
    params = {
        'key': api_key,
        'q': location,
        "aqi": 'yes'
    }
    response = requests.get(current_weather_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"

def get_secret_from_keyvault(vault_url, secret_name):
    credential = DefaultAzureCredential()
    secret_client = SecretClient(vault_url=vault_url, credential=credential)
    retrieved_secret = secret_client.get_secret(secret_name)
    return retrieved_secret.value

def fetch_weather_data():
    base_url = "http://api.weatherapi.com/v1/" # weatherapi endpoint
    location = "Bangalore" # you can change the city

    VAULT_URL = "" # Add your Azure Vault url
    API_KEY_SECRET_NAME = "" # Add your Azure Vault Secret name
    weatherapikey = get_secret_from_keyvault(VAULT_URL, API_KEY_SECRET_NAME)

    current_weather = get_current_weather(base_url, weatherapikey, location)

    send_event(current_weather)

fetch_weather_data() 