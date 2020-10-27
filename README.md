# DS

## Product Vision Document:

https://www.notion.so/Product-Vision-Document-a66d0df2767949cea3b37d65e9c04155


## API Documentation:

https://greengardenapi.herokuapp.com/docs


### What is MedCab?

This medcab webapp is a microservice API that allows users to describe their ailments and preferences for marijuana use,
and using an NLP model, gives 5 recommended straings of cannabis.

This NLP model uses keywords passed to it from the website front end, runs it through a prediction algorithm that yields a result of the top 5 strains for their needs. The model was trained on a dataset of over 2000 unique strains of cannabis: their type, flavor profiles, descriptions, and known effects. 

### How does the API work?

The API is a microservice, so while -it- doesnt have a functioning front end, it utilizes app routes to monitor the address bar for information.
Using the routes supplied can access different functions of the API framework, allowing users to choose which parts of the microservice to utilize.

    Routes:
        ( / ):
            This will bring the user to the home landing page, with just a generic response in json that reads:
        
![homepage response](/readme_ext/homeroute.png)

        ( /recommendation/{user_string_input} ):
            This route passes the user input (string format) into the NLP model for a prediction.
            It returns a recommended list of 5 cannabis strains in JSON format:

        [
  {
    "Strain": "Bakerstreet",
    "Type": "indica",
    "Effects": "Euphoric,Relaxed,Giggly,Happy,Sleepy",
    "Flavor": "Earthy,Diesel,Sweet",
    "Description": "Bakerstreet is a variety of Hindu Kush grown by Canadian LP Tweed. It is a pure indica with origins in the Hindu Kush mountain range. The subtle sweet and earthy sandalwood aroma of Bakerstreet induces a deep sense of calm that helps bring relief to those suffering pain, nausea, and stress disorders. Its heavy body effects make it a top strain to help you relax and unwind at the end of a long day. "
  },
  {
    "Strain": "Chocolate-Drop",
    "Type": "hybrid",
    "Effects": "Uplifted,Euphoric,Giggly,Happy,Relaxed",
    "Flavor": "Earthy,Vanilla",
    "Description": "Chocolate Drop is the supposed cross of Chocolate Kush and Lowryder. This indica-dominant hybrid produces squat plants with tree-shaped buds that reek of incense, cocoa, pungent earth, and citrus. The effects are relaxing but not overly sedative and offer a kind, uplifting euphoria. Enjoy Chocolate Drop throughout the day to help relieve stress, improve mood, and manage anxiety."
  },
  {
    "Strain": "Lak-Federal-Reserve",
    "Type": "indica",
    "Effects": "Relaxed,Tingly,Hungry,Uplifted,Creative",
    "Flavor": "Lemon,Earthy,Sweet",
    "Description": "Federal Reserve by Los Angeles Kush is another heavy indica cut out of Southern California. Created by crossing SFV OG with a special Los Angeles Kush phenotype, this strain offers deep relaxation and sedation. Federal Reserve's terpene profile is strong and pungent, smelling of pine, gas, and skunk. Its body effects can help sooth minor physical pain and help nullify stress and anxiety.   "
  },
  {
    "Strain": "K2",
    "Type": "hybrid",
    "Effects": "Relaxed,Happy,Giggly,Hungry,Sleepy",
    "Flavor": "Earthy,Citrus,Sweet",
    "Description": "Named for Earth's second highest mountain peak, K2 is sure to leave you at a higher elevation. The mellow flavor is accented with hints of fruit and spice, and the captivating aroma helped to make it a staple at coffee shops in Amsterdam. A cross between White Widow and Hindu Kush, this dependable Dutch hybrid first attracted growers for its compact stature, while the relaxing indica effects have kept consumers who battle anxiety and insomnia asking for more."
  },
  {
    "Strain": "White-Lotus",
    "Type": "hybrid",
    "Effects": "Relaxed,Euphoric,Focused,Happy,Sleepy",
    "Flavor": "Earthy,Citrus,Sweet",
    "Description": "White Lotus by Bodhi Seed gets its frosting of trichomes from its mother, The White, while the father, Snow Lotus, works to increase size, cannabinoid profile, and overall potency of this strain. The tart, citrus aroma and flavors of lemon and hash draw you in while the relaxing indica effects will help to curb bouts of depression and insomnia."
  }
]