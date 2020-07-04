## base: greet
* greet
  - utter_greet

## base: say goodbye
* goodbye
  - utter_goodbye

## base: search text
* search_recipe{"search_text": "sacher"}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"search_text": "sacher"}
  - form{"name": null}

## base: gluten free
* search_recipe{"gluten_free": true}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"gluten_free": true}
  - form{"name": null}

## base: vegan
* search_recipe{"vegan": true}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"vegan": true}
  - form{"name": null}

## base: vegetarian
* search_recipe{"vegetarian": true}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"vegetarian": true}
  - form{"name": null}

## base: max_calories
* search_recipe{"max_calories": 30}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"max_calories": 30}
  - form{"name": null}

## base: max_minutes
* search_recipe{"max_minutes": 30}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"max_minutes": 30}
  - form{"name": null}

## base: search_ingredients
* search_recipe{"search_ingredients": "carrot"}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"search_ingredients": ["carrot"]}
  - form{"name": null}

## base: search_ingredients 2
* search_recipe{"search_ingredients": ["carrot", "eggs"]}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"search_ingredients": ["carrot", "eggs"]}
  - form{"name": null}

## base: avoid_ingredients
* search_recipe{"avoid_ingredients": "carrot"}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"avoid_ingredients": ["carrot"]}
  - form{"name": null}

## base: avoid_ingredients 2
* search_recipe{"avoid_ingredients": ["carrot", "eggs"]}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"avoid_ingredients": ["carrot", "eggs"]}
  - form{"name": null}

## base: choose recipe
* choose_recipe{"ordinal": "1"}
  - action_choose_recipe
  - slot{"chosen_recipe": 1}
  
## base: choose recipe 2
* choose_recipe{"ordinal": "3"}
  - action_choose_recipe
  - slot{"chosen_recipe": 3}
  
## base: get_recipe_info
* get_recipe_info
  - action_get_recipe_info
  
## base: get_recipe_info 2
* get_recipe_info{"ordinal": "2"}
  - action_choose_recipe
  - slot{"chosen_recipe": 2}
  - action_get_recipe_info
  
## chain: get_recipe_info
* get_recipe_info{"ordinal": "3"}
  - action_choose_recipe
  - slot{"chosen_recipe": 3}
  - action_get_recipe_info
* choose_recipe{"ordinal": "2"}
  - action_choose_recipe
  - slot{"chosen_recipe": 2}
  - action_get_recipe_info
  
## base: get_recipe_ingredients
* get_recipe_ingredients
  - action_get_recipe_info
  
## base: get_recipe_ingredients 2
* get_recipe_ingredients{"ordinal": "3"}
  - action_choose_recipe
  - slot{"chosen_recipe": 3}
  - action_get_recipe_ingredients
  
## chain: get_recipe_ingredients
* get_recipe_ingredients{"ordinal": "3"}
  - action_choose_recipe
  - slot{"chosen_recipe": 3}
  - action_get_recipe_ingredients
* choose_recipe{"ordinal": "2"}
  - action_choose_recipe
  - slot{"chosen_recipe": 2}
  - action_get_recipe_ingredients
  
## base: get_recipe_nutrition
* get_recipe_nutrition
  - action_get_recipe_nutrition
  
## base: get_recipe_nutrition 2
* get_recipe_nutrition{"ordinal": 2}
  - action_choose_recipe
  - slot{"chosen_recipe": 2}
  - action_get_recipe_nutrition
  
## chain: get_recipe_nutrition
* get_recipe_nutrition{"ordinal": "3"}
  - action_choose_recipe
  - slot{"chosen_recipe": 3}
  - action_get_recipe_nutrition
* choose_recipe{"ordinal": "2"}
  - action_choose_recipe
  - slot{"chosen_recipe": 2}
  - action_get_recipe_nutrition
  
## base: get_recipe_steps
* get_recipe_steps
  - action_get_recipe_steps
  
## base: get_recipe_steps 2
* get_recipe_steps{"ordinal": 2}
  - action_choose_recipe
  - slot{"chosen_recipe": 2}
  - action_get_recipe_steps
  
## chain: get_recipe_steps
* get_recipe_steps{"ordinal": "3"}
  - action_choose_recipe
  - slot{"chosen_recipe": 3}
  - action_get_recipe_steps
* choose_recipe{"ordinal": "2"}
  - action_choose_recipe
  - slot{"chosen_recipe": 2}
  - action_get_recipe_steps
  
## base: start_cooking
* start_cooking
  - action_start_cooking
  - slot{"step_index": 0}
  
## base: start_cooking 2
* start_cooking{"ordinal": 2}
  - action_choose_recipe
  - slot{"chosen_recipe": 2}
  - action_start_cooking
  - slot{"step_index": 0}
  
## base: next_step
* next_step
  - action_next_step
  
## base: clear_search
* clear_search
  - action_clear_search

## gluten free + cook
* search_recipe{"gluten_free": true}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"gluten_free": true}
  - form{"name": null}
* choose_recipe{"ordinal": 1}
  - action_choose_recipe
  - slot{"chosen_recipe": 1}
  - action_get_recipe_info
* get_recipe_info
  - action_get_recipe_info
* start_cooking
  - action_start_cooking
  - slot{"step_index": 0}
* affirm
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

## avoid ingredient + cook
* search_recipe{"search_ingredients": ["potatoes", "eggs"], "avoid_ingredients": "carrot"}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"avoid_ingredients": ["carrot"]}
  - slot{"search_ingredients": ["potatoes", "eggs"]}
  - form{"name": null}
* choose_recipe{"ordinal": 1}
  - action_choose_recipe
  - slot{"chosen_recipe": 1}
  - action_get_recipe_info
* start_cooking
  - action_start_cooking
  - slot{"step_index": 0}
* affirm
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

## search_text + cook
* search_recipe{"search_text": "strudel"}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"search_text": "strudel"}
  - form{"name": null}
* choose_recipe{"ordinal": 1}
  - action_choose_recipe
  - slot{"chosen_recipe": 1}
  - action_get_recipe_info
* get_recipe_ingredients
  - action_get_recipe_ingredients
* choose_recipe{"ordinal": 2}
  - action_choose_recipe
  - slot{"chosen_recipe": 2}
  - action_get_recipe_ingredients
* start_cooking
  - action_start_cooking
  - slot{"step_index": 0}
* affirm
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

## next page
* search_recipe{"search_text": "dessert"}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"search_text": "dessert"}
  - form{"name": null}
* next_page
  - action_next_page
  - slot{"page": 2}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - form{"name": null}
* choose_recipe{"ordinal": 8}
  - action_choose_recipe
  - slot{"chosen_recipe": 8}
  - action_get_recipe_info

## affirm cooking
* start_cooking
  - action_start_cooking
  - slot{"step_index": 0}
* affirm
  - action_next_step
  - slot{"step_index": 1}
* next_step
  - action_next_step
  - slot{"step_index": 2}

## affirm cooking + ordinal
* start_cooking{"ordinal": 1}
  - action_choose_recipe
  - slot{"chosen_recipe": 1}
  - action_start_cooking
  - slot{"step_index": 0}
* affirm
  - action_next_step
  - slot{"step_index": 1}
* next_step
  - action_next_step
  - slot{"step_index": 2}
  
## deny cooking
* start_cooking
  - action_start_cooking
  - slot{"step_index": 0}
* deny
  - utter_deny

## action deny
* deny
  - utter_deny