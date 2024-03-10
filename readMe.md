# OPTI-FHIR: Ergonomics in the Workspace 

Working from a desk for extended periods of time can lead to various health issues, especially if proper posture is not maintained. Bad posture positions, such as slouching or hunching over, can cause strain on the neck, back, and shoulders, leading to discomfort, pain, and even long-term musculoskeletal problems.

OPTI-FHIR aims to address these issues by optimizing the posture of individuals in the workspace. With OPTI-FHIR, users can receive personalized recommendations tailored to their specific needs. The system takes into account factors such as desk height, chair position, monitor placement, and keyboard and mouse ergonomics. By optimizing these elements, OPTI-FHIR ensures that users maintain a healthy and ergonomic posture throughout their workday.

NOTE: This program is currently a prototype

## How to Opti-Fhir Works

Opti-Fhir works by integrating patient records using the Fhir standard to access crucial information like height and previous neck or back related issues the patient might have faced. In combination with user inputted data like lower body height, the program calculates optimal working positions and generates 3D models that demonstrate the optimal working conditions.

Opti-Fhir will have the ability to scan the surroundings and overlay the models using AR, albeit missing from the prototype.

## How to run the current version

1. Clone the repository 
2. Run the command  ```docker-compose up``` 
3. Run  ```loadData.py```

```main.py``` contains the FHIR data access functions while ```3dModel.py``` contains the modelling functionality.