from fhirclient.models.observation import Observation
from fhirclient.models.patient import Patient
from fhirclient.models.bundle import Bundle
from datetime import datetime
from fhirclient import client
import requests

# Access FHIR API
settings = {
    'app_id': 'my_web_app',
    'api_base': 'http://localhost:8090/fhir'
}
smart = client.FHIRClient(settings=settings)
search = Observation.where(struct={'code': 'http://loinc.org|8302-2'})


# Run through obsevations to find 'patientLimit' amount of patients and print heights
patientLimit = 10

observations = {}
patient_counter = 0
reached_limit = False
bundle = search.perform(smart.server)

while bundle is not None:
    # Add the current page's entries to the list
    if bundle.entry is not None:
        for entry in bundle.entry:
            patient_ref = entry.resource.subject.reference
            patient_id = patient_ref.replace('Patient/', '')
            if patient_id not in observations:
                patient_counter += 1
                observations[patient_id] = entry
            if patient_counter >= patientLimit:
                reached_limit = True
                break

    # Get the next page
    if not reached_limit:
        next_link = [link for link in bundle.link if link.relation == 'next']
        if next_link:
            response = requests.get(next_link[0].url)
            bundle = Bundle(response.json())
        else:
            bundle = None
    else:
        break

# Loop through the latest observations
for patient_id, obs in observations.items():

    patient = Patient.read(patient_id, smart.server)

    patient_name = patient.name[0].given[0] + ' ' + patient.name[0].family

    obs_value = obs.resource.valueQuantity.value

    birth_date = patient.birthDate.date
    age = datetime.now().year - birth_date.year

    print(f"Patient: {patient_name}, Age: {age}, Latest Height: {obs_value}")