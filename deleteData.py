import requests

base_url = 'http://localhost:8090/fhir' 


response = requests.get(f'{base_url}/metadata')

if response.status_code == 200:
    metadata = response.json()

    # Get the list of all resource types
    resource_types = [resource['type'] for resource in metadata['rest'][0]['resource']]

    for resource_type in resource_types:
        # Send a GET request to the server to get all resources of the current type
        response = requests.get(f'{base_url}/{resource_type}')

        if response.status_code == 200:
            # Parse the response as JSON
            resources = response.json()

            if 'entry' in resources:
                for resource in resources['entry']:
                    resource_id = resource['resource']['id']

                    # Send a DELETE request to the server to delete the current resource
                    requests.delete(f'{base_url}/{resource_type}/{resource_id}')