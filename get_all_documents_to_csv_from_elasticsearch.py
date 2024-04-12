import json
import csv
import requests

# Elasticsearch endpoint URL
elasticsearch_url = "http://0.0.0.0:9210/products/_search?size=10000"

# Send GET request to Elasticsearch endpoint
response = requests.get(elasticsearch_url)

# Check if request was successful
if response.status_code == 200:
    # Load JSON data from response
    data = response.json()

    # Extract SKU, name, and price from each item
    rows = []
    for item in data['hits']['hits']:
        source = item.get('_source')
        if source:
            sku = source.get('sku')
            name = source.get('name')
            price = source.get('price')
            regular_price = source.get('regular_price')
            
            rows.append([sku, name, price, regular_price])

    # Write to CSV file
    with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['SKU', 'Name', 'Price', 'regular_price'])
        csv_writer.writerows(rows)

    print("CSV file exported successfully.")
else:
    print("Failed to retrieve data from Elasticsearch. Status code:", response.status_code)
