## greet
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## 1
* search_recipe{"gluten_free": "celiac"}
  - slot{"gluten_free": true}
  - action_search_recipe
* choose_recipe{"chosen_recipe": "first"}
  - slot{"chosen_recipe": 0}
  - action_choose_recipe
* get_recipe_info
  - action_get_recipe_info
* start_cooking
  - action_start_cooking
* next_step
  - action_next_step
* next_step
  - action_next_step
* next_step
  - action_next_step
* next_step
  - action_next_step