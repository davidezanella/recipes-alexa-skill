## greet
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## 1
* search_recipe{"gluten_free": "true"}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"gluten_free": true}
  - form{"name": null}
* choose_recipe{"ordinal": "1"}
  - action_choose_recipe
  - slot{"chosen_recipe": 1}
* get_recipe_info
  - action_get_recipe_info
* start_cooking
  - action_start_cooking
  - slot{"step_index": 0}
* next_step
  - action_next_step
  - slot{"step_index": 1}
* next_step
  - action_next_step
  - slot{"step_index": 2}
* next_step
  - action_next_step
  - slot{"step_index": 3}
* next_step
  - action_next_step
  - slot{"step_index": null}