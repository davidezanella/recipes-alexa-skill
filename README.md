# Recipes Alexa skill

Final project for the **Language understanding systems** course @ UniTN A.Y. 2019-2020

Dataset used to search recipes: [Food.com recipes and user interactions](https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions?select=RAW_recipes.csv)

## Initialization
In order to run the Alexa skill from your local machine follow this steps:
- Install the necessary python packages:
```shell script
pip3 install -r requirements.txt
```

- *[Optional]* Update the sqlite3 db 
    * insert the `RAW_recipe.csv` file into the `recipes_db` folder
    * run the `create_db_from_csv.py` script file to populate a db file
    * run the `scrape_ingredients_quantity.py` script if you want to take the right ingredients quantity from the web
- Install the `ngrok` program
- Create an Alexa developer account

## Test different configurations
To test different nlu pipelines over the training nlu, create some configuration files in the `NLU_pipelines` folder and then type:
```shell script
make test-nlu
```

To test different core policies over the test stories, create some configuration files in the `CORE_policies` folder and then type:
```shell script
make test-core
```
