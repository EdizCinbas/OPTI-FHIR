import requests

# Base URL of your HAPI FHIR server
base_url = 'http://localhost:8090/fhir' 

# Send a GET request to the server's metadata endpoint
response = requests.get(f'{base_url}/metadata')

# Check if the request was successful
if response.status_code == 200:
    # Parse the response as JSON
    metadata = response.json()

    # Get the list of all resource types
    resource_types = [resource['type'] for resource in metadata['rest'][0]['resource']]

    # Loop through all resource types
    for resource_type in resource_types:
        # Send a GET request to the server to get all resources of the current type
        response = requests.get(f'{base_url}/{resource_type}')

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response as JSON
            resources = response.json()

            # Check if 'entry' is in resources
            if 'entry' in resources:
                # Loop through all resources
                for resource in resources['entry']:
                    # Get the resource ID
                    resource_id = resource['resource']['id']

                    # Send a DELETE request to the server to delete the current resource
                    requests.delete(f'{base_url}/{resource_type}/{resource_id}')