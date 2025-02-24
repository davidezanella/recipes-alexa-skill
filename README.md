# Recipes Alexa skill

Final project for the **Language understanding systems** course @ UniTN A.Y. 2019-2020

Dataset used to search recipes: [Food.com recipes and user interactions](https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions?select=RAW_recipes.csv)

## Initialization
In order to run the Alexa skill from your local machine follow this steps:
- Install the necessary python packages:
```shell script
pip3 install -r requirements.txt
```

- *[Optional]* Update the sqlite3 db (the version in the repo is a lighter one)
    * insert the `RAW_recipe.csv` file into the `recipes_db` folder
    * run the `create_db_from_csv.py` script file to populate a db file
    * run the `scrape_ingredients_quantity.py` script if you want to take the right ingredients quantity from the web
- Install the `ngrok` program
- Create an Alexa developer account

## Start the Alexa skill
- run ```rasa run actions```
- in another shell run ```rasa run -m models --endpoints endpoints.yml```
- in another shell run ```ngrok http 5005```
- copy the resulting url of ngrok (like "https://123abc4d.ngrok.io")
- go to the Alexa Developer Console
- choose "Endpoint" from the "Skill Builder Checklist"
- select HTTPS
- as SSL certificate, choose "My development endpoint is a subdomain of a domain that has a wildcard certificate from a certificate authority"
- copy the ngrok url concatenated with ```webhooks/alexa_assistant/webhook```
- save your endpoints configuration
- go to the "test" tab and start testing it by saying ```recipes assistant```

## Test different configurations
To test different nlu pipelines over the training nlu, create some configuration files in the `NLU_pipelines` folder and then type:
```shell script
make test-nlu
```
In the `NLU_results` folder you will find the obtained results.

To test different core policies over the test stories, create some configuration files in the `CORE_policies` folder and then type:
```shell script
make test-core
```
In the `CORE_results` folder you will find the obtained results.

To test different nlu pipelines and core policies over the end-to-end test stories, create some configuration files in the `END2END_configs` folder and then type:
```shell script
make test-e2e
```
In the `END2END_results` folder you will find the obtained results.


