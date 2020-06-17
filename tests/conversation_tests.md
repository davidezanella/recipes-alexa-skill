#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## say hello
* greet: hello there!
  - utter_greet

## say goodbye
* goodbye: bye-bye!
  - utter_goodbye

## search ingredients
* greet: hello there!
  - utter_greet
* search_recipe: i would like to cook using [rosemary](search_ingredients)
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"search_ingredients": ["rosemary"]}
  - form{"name": null}
* goodbye: bye-bye!
  - utter_goodbye

## avoid ingredients
* greet: hello there!
  - utter_greet
* search_recipe: i would like to cook something but avoiding to use [pineapple](avoid_ingredients)
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"avoid_ingredients": ["pineapple"]}
  - form{"name": null}
* goodbye: bye-bye!
  - utter_goodbye

## gluten free and search text
* greet: hello there!
  - utter_greet
* search_recipe: can you find a recipe for a [gluten free]{"entity": "gluten_free", "value": "true"} [pie](search_text)
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"gluten_free": true}
  - slot{"search_text": "pie"}
  - form{"name": null}
* goodbye: bye-bye!
  - utter_goodbye

## search text
* greet: hello there!
  - utter_greet
* search_recipe: what should i do to cook the [pastiera](search_text)?
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"search_text": "pastiera"}
  - form{"name": null}
* goodbye: bye-bye!
  - utter_goodbye

## vegetarian
* greet: hello there!
  - utter_greet
* search_recipe: any recipes for [vegetarians]{"entity": "vegetarian", "value": "true"}?
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"vegetarian": true}
  - form{"name": null}
* goodbye: bye-bye!
  - utter_goodbye

## vegan
* greet: hello there!
  - utter_greet
* search_recipe: find some recipes for [vegans]{"entity": "vegan", "value": "true"}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"vegan": true}
  - form{"name": null}
* goodbye: bye-bye!
  - utter_goodbye

## max_minutes
* greet: hello there!
  - utter_greet
* search_recipe: any recipes done in [53](max_minutes) minutes?
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"max_minutes": 53}
  - form{"name": null}
* goodbye: bye-bye!
  - utter_goodbye

## max_calories
* greet: hello there!
  - utter_greet
* search_recipe: any recipes with max [53](max_calories) calories?
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"max_calories": 53}
  - form{"name": null}
* goodbye: bye-bye!
  - utter_goodbye

## complex: max_minutes + vegetarian + search_ingredients
* greet: hello there!
  - utter_greet
* search_recipe: i need a recipe ready in [60](max_minutes) minutes for [vegetarians]{"entity": "vegetarian", "value": "true"} where i can use [rosemary](search_ingredients)
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"max_minutes": 60}
  - slot{"vegetarian": true}
  - slot{"search_ingredients": ["rosemary"]}
  - form{"name": null}
* get_recipe_info: Describe the [first]{"entity": "ordinal", "value": "1"} one
  - action_choose_recipe
  - slot{"chosen_recipe": 1}
  - action_get_recipe_info
* get_recipe_steps: What should i do in the [third]{"entity": "ordinal", "value": "3"} recipe?
  - action_choose_recipe
  - slot{"chosen_recipe": 3}
  - action_get_recipe_steps
* get_recipe_nutrition: how many calories?
  - action_get_recipe_nutrition
* start_cooking: let's cook the [second]{"entity": "ordinal", "value": "2"} one
  - action_choose_recipe
  - slot{"chosen_recipe": 2}
  - action_start_cooking
  - slot{"step_index": 0}
* affirm: Sure, let's start!
  - action_next_step
  - slot{"step_index": 1}
* next_step: done
  - action_next_step
  - slot{"step_index": 2}  
* goodbye: bye-bye!
  - utter_goodbye

## complex: max_calories + avoid_ingredients + search_ingredients
* greet: hello there!
  - utter_greet
* search_recipe: i can eat at maximum [175](max_calories) calories, find a recipe where i can use [pineapple](search_ingredients) but without [rosemary](avoid_ingredients)
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"max_calories": 175}
  - slot{"search_ingredients": ["pineapple"]}
  - slot{"avoid_ingredients": ["rosemary"]}
  - form{"name": null}
* get_recipe_info: Tell me more about the [third]{"entity": "ordinal", "value": "3"} one
  - action_choose_recipe
  - slot{"chosen_recipe": 3}
  - action_get_recipe_info
* search_recipe: please find some [without gluten]{"entity": "gluten_free", "value": "true"}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - slot{"gluten_free": true}
  - form{"name": null}
* get_recipe_nutrition: how many calories are there in the [second]{"entity": "ordinal", "value": "2"} one?
  - action_get_recipe_nutrition
* next_page: fine some alternatives please
  - action_next_page
  - slot{"page": 2}
  - action_form_search_recipe
  - form{"name": "action_form_search_recipe"}
  - form{"name": null}
* start_cooking: ok I want to cook the [sixth]{"entity": "ordinal", "value": "6"} one
  - action_choose_recipe
  - slot{"chosen_recipe": 6}
  - action_start_cooking
  - slot{"step_index": 0}
* deny: No, I changed my mind
  - utter_deny
* goodbye: bye-bye!
  - utter_goodbye