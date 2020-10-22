# DS

### Product Vision Document:

https://www.notion.so/Product-Vision-Document-a66d0df2767949cea3b37d65e9c04155


### What is MedCab?

This medcab webapp is a microservice API that allows users to describe their ailments and preferences for marijuana use,
and using an NLP model, gives 5 recommended straings of marijuana.

This NLP model uses keywords passed to it from the website front end, runs it through a prediction algorithm that yields a result of the top 5 strains for their needs. The model was trained on a dataset of over 2000 unique strains of marijuana, their type, flavor profiles, descriptions, and known effects. 

### How does the API work?

The API is a microservice, so while -it- doesnt have a functioning front end, it utilizes app routes to monitor the address bar for information.
Using the routes supplied can access different functions of the API framework, allowing users to choose which parts of the microservice to utilize.

    **Routes:**
'(/):
    This will bring the user to the home landing page, with just a generic response in json that reads:
    ![homepage response](/readme_ext/homeroute.png)'

'(/recommendation/{user_string_input}):
    This route passes the user input (string format) into the NLP model for a prediction.
    It returns a recommended list of 5 cannabis strains in JSON format:'