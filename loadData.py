import requests
import json
import os

server_url = 'http://localhost:8090/fhir'

folder_path = './SyntheticData' # Replace with absolute path

headers = {
    'Content-Type': 'application/fhir+json',
}

for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith('.json'):
            with open(os.path.join(root, filename), 'r') as file:
                resource_data = json.load(file)

            # Get the resource type from the resource data
            resource_type = resource_data['resourceType']

            # Convert the resource data to a JSON string
            resource_data_json = json.dumps(resource_data)

            # Determine the URL to post to
            if resource_type == 'Bundle' and resource_data.get('type') == 'transaction':
                post_url = server_url  # Post to the base URL for transaction Bundles
            else:
                post_url = f'{server_url}/{resource_type}'  # Post to the resource-specific endpoint for other resources

            # Send a POST request to the server
            response = requests.post(post_url, headers=headers, data=resource_data_json)

            print(f'Response for {filename}: {response.status_code}')