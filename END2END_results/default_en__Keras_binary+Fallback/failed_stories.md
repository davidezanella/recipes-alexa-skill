## search text (tests/conversation_tests.md)
* greet: hello there!
    - utter_greet
* search_recipe: what should i do to cook the [pastiera](search_text)?   <!-- predicted: search_recipe: what should i do to cook the pasti[era](search_ingredients)? -->
    - slot{"search_ingredients": ["era"]}
    - action_form_search_recipe
    - form{"name": "action_form_search_recipe"}
    - slot{"search_text": "pastiera"}
    - form{"name": null}
* goodbye: bye-bye!
    - utter_goodbye


## complex: max_minutes + vegetarian + search_ingredients (tests/conversation_tests.md)
* greet: hello there!
    - utter_greet
* search_recipe: i need a recipe ready in [60](max_minutes) minutes for [vegetarians]{"entity": "vegetarian", "value": "true"} where i can use [rosemary](search_ingredients)
    - slot{"max_minutes": "60"}
    - slot{"search_ingredients": ["rosemary"]}
    - slot{"vegetarian": "true"}
    - action_form_search_recipe
    - form{"name": "action_form_search_recipe"}
    - slot{"max_minutes": 60}
    - slot{"vegetarian": true}
    - slot{"search_ingredients": ["rosemary"]}
    - form{"name": null}
* get_recipe_info: Describe the [first]{"entity": "ordinal", "value": "1"} one
    - slot{"ordinal": 1}
    - action_choose_recipe
    - slot{"chosen_recipe": 1}
    - action_get_recipe_info
* get_recipe_steps: What should i do in the [third]{"entity": "ordinal", "value": "3"} recipe?   <!-- predicted: get_recipe_ingredients: What should i do in the [third]{"entity": "ordinal", "value": "3"} recipe? -->
    - slot{"ordinal": 3}
    - action_choose_recipe
    - slot{"chosen_recipe": 3}
    - action_get_recipe_steps   <!-- predicted: action_get_recipe_ingredients -->
* get_recipe_nutrition: how many calories?
    - action_get_recipe_nutrition
* start_cooking: let's cook the [second]{"entity": "ordinal", "value": "2"} one
    - slot{"ordinal": 2}
    - action_choose_recipe
    - slot{"chosen_recipe": 2}
    - action_start_cooking
    - slot{"step_index": 0}
* affirm: Sure, let's start!   <!-- predicted: start_cooking: Sure, let's start! -->
    - action_next_step   <!-- predicted: action_start_cooking -->
    - slot{"step_index": 1}
* next_step: done
    - action_next_step
    - slot{"step_index": 2}
* goodbye: bye-bye!
    - utter_goodbye


## complex: max_calories + avoid_ingredients + search_ingredients (tests/conversation_tests.md)
* greet: hello there!
    - utter_greet
* search_recipe: i can eat at maximum [175](max_calories) calories, find a recipe where i can use [pineapple](search_ingredients) but without [rosemary](avoid_ingredients)   <!-- predicted: search_recipe: i can eat at maximum [175](max_calories) calories, find a recipe where i can use [pineapple](avoid_ingredients) but without [rosemary](search_ingredients) -->
    - slot{"avoid_ingredients": ["pineapple"]}
    - slot{"max_calories": "175"}
    - slot{"search_ingredients": ["rosemary"]}
    - action_form_search_recipe
    - form{"name": "action_form_search_recipe"}
    - slot{"max_calories": 175}
    - slot{"search_ingredients": ["pineapple"]}
    - slot{"avoid_ingredients": ["rosemary"]}
    - form{"name": null}
* get_recipe_info: Tell me more about the [third]{"entity": "ordinal", "value": "3"} one
    - slot{"ordinal": 3}
    - action_choose_recipe
    - slot{"chosen_recipe": 3}
    - action_get_recipe_info
* search_recipe: please find some [without gluten]{"entity": "gluten_free", "value": "true"}
    - slot{"gluten_free": "true"}
    - action_form_search_recipe
    - form{"name": "action_form_search_recipe"}
    - slot{"gluten_free": true}
    - form{"name": null}
* get_recipe_nutrition: how many calories are there in the [second]{"entity": "ordinal", "value": "2"} one?
    - slot{"ordinal": 2}
    - action_get_recipe_nutrition   <!-- predicted: action_choose_recipe -->
    - action_listen   <!-- predicted: utter_rephrase -->
* next_page: fine some alternatives please
    - action_next_page
    - slot{"page": 2}
    - action_form_search_recipe
    - form{"name": "action_form_search_recipe"}
    - form{"name": null}
* start_cooking: ok I want to cook the [sixth]{"entity": "ordinal", "value": "6"} one
    - slot{"ordinal": 6}
    - action_choose_recipe
    - slot{"chosen_recipe": 6}
    - action_start_cooking
    - slot{"step_index": 0}
* deny: No, I changed my mind
    - utter_deny
* goodbye: bye-bye!
    - utter_goodbye


## complex: max_minutes + max_calories + vegan (tests/conversation_tests.md)
* greet: hello there!
    - utter_greet
* search_recipe: i need a recipe with maximum [120](max_calories) calories, that takes maximum [70](max_minutes) minutes for [vegans]{"entity": "vegan", "value": "true"}
    - slot{"max_calories": "120"}
    - slot{"max_minutes": "70"}
    - slot{"vegan": "true"}
    - action_form_search_recipe
    - form{"name": "action_form_search_recipe"}
    - slot{"max_calories": 120}
    - slot{"max_minutes": 70}
    - slot{"vegan": true}
    - form{"name": null}
* get_recipe_nutrition: Describe the nutrition of the [third]{"entity": "ordinal", "value": "3"} one
    - slot{"ordinal": 3}
    - action_choose_recipe
    - slot{"chosen_recipe": 3}
    - action_get_recipe_nutrition
* get_recipe_ingredients: What do I need for that recipe?
    - action_get_recipe_ingredients   <!-- predicted: action_get_recipe_info -->
* start_cooking: fine, let's try to cook it!
    - action_start_cooking
    - slot{"step_index": 0}
* affirm: Yes, I'm ready
    - action_next_step
    - slot{"step_index": 1}
* next_step: already done
    - action_next_step
    - slot{"step_index": 2}
* goodbye: bye-bye!
    - utter_goodbye


## get_recipe_ingredients (tests/conversation_tests.md)
* greet: hello there!
    - utter_greet
* search_recipe: i need a recipe ready in [80](max_minutes) minutes
    - slot{"max_minutes": "80"}
    - action_form_search_recipe
    - form{"name": "action_form_search_recipe"}
    - slot{"max_minutes": 70}
    - form{"name": null}
* get_recipe_ingredients: Explain the ingredients needed by the [third]{"entity": "ordinal", "value": "3"} recipe
    - slot{"ordinal": 3}
    - action_choose_recipe
    - slot{"chosen_recipe": 3}
    - action_get_recipe_ingredients
* start_cooking: ok, i want to cook it!   <!-- predicted: affirm: ok, i want to cook it! -->
    - action_start_cooking   <!-- predicted: utter_rephrase -->
    - slot{"step_index": 0}
* affirm: Yes, go on
    - action_next_step
    - slot{"step_index": 1}
* next_step: what's the next step?
    - action_next_step
    - slot{"step_index": 2}
* goodbye: bye-bye!
    - utter_goodbye


## get_recipe_steps (tests/conversation_tests.md)
* greet: hello there!
    - utter_greet
* search_recipe: i need a recipe ready in [80](max_minutes) minutes
    - slot{"max_minutes": "80"}
    - action_form_search_recipe
    - form{"name": "action_form_search_recipe"}
    - slot{"max_minutes": 70}
    - form{"name": null}
* get_recipe_steps: Explain the steps needed for the [third]{"entity": "ordinal", "value": "3"} recipe
    - slot{"ordinal": 3}
    - action_choose_recipe
    - slot{"chosen_recipe": 3}
    - action_get_recipe_steps
* start_cooking: ok, i want to cook it!   <!-- predicted: affirm: ok, i want to cook it! -->
    - action_start_cooking   <!-- predicted: utter_rephrase -->
    - slot{"step_index": 0}
* affirm: Yes, go on
    - action_next_step
    - slot{"step_index": 1}
* next_step: what's the next step?
    - action_next_step
    - slot{"step_index": 2}
* goodbye: bye-bye!
    - utter_goodbye


## search 2 ingredients (tests/conversation_tests.md)
* greet: hello there!
    - utter_greet
* search_recipe: i would like to cook something using [rosemary](search_ingredients) and [meat](search_ingredients)   <!-- predicted: search_recipe: i would like to cook something using [rosemary](search_ingredients) and [meat](avoid_ingredients) -->
    - slot{"avoid_ingredients": ["meat"]}
    - slot{"search_ingredients": ["rosemary"]}
    - action_form_search_recipe
    - form{"name": "action_form_search_recipe"}
    - slot{"search_ingredients": ["rosemary", "meat"]}
    - form{"name": null}
* goodbye: bye-bye!
    - utter_goodbye


## search 3 ingredients (tests/conversation_tests.md)
* greet: hello there!
    - utter_greet
* search_recipe: i would like to cook using [rosemary](search_ingredients), [meat](search_ingredients) and [carrots](search_ingredients)   <!-- predicted: search_recipe: i would like to cook using [rosemar](search_ingredients)y, meat and [carrots](search_ingredients) -->
    - slot{"search_ingredients": ["rosemar", "carrots"]}
    - action_form_search_recipe
    - form{"name": "action_form_search_recipe"}
    - slot{"search_ingredients": ["rosemary", "meat", "carrots"]}
    - form{"name": null}
* goodbye: bye-bye!
    - utter_goodbye


## avoid 3 ingredients (tests/conversation_tests.md)
* greet: hello there!
    - utter_greet
* search_recipe: i would like to cook something without using [pineapple](avoid_ingredients), [pears](avoid_ingredients) or [carrots](avoid_ingredients)   <!-- predicted: search_recipe: i would like to cook something without using [pineapple, pears](avoid_ingredients) or [carrots](avoid_ingredients) -->
    - slot{"avoid_ingredients": ["pineapple, pears", "carrots"]}
    - action_form_search_recipe
    - form{"name": "action_form_search_recipe"}
    - slot{"avoid_ingredients": ["pineapple", "pears", "carrots"]}
    - form{"name": null}
* goodbye: bye-bye!
    - utter_goodbye


