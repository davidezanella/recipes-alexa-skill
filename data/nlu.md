## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:search_recipe
- I want to cook something using [carrots](search_ingredients)
- I want to cook using [potatoes](search_ingredients) and [chicken](search_ingredients)
- I have some [peppers](search_ingredients) what can i cook?
- I have some [eggs](search_ingredients) what can i prepare?

- I would like to prepare a [dessert](search_text)
- find the recipe of the [strudel](search_text)
- i want to cook the [angel pie](search_text)
- the recipe of the [carrots pie](search_text)?
- i would like to cook the [spaghetti](search_text)

- I have [30](max_minutes) minutes what can I prepare?
- I have [50](max_minutes) minutes what can I prepare?
- I have only [40](max_minutes) minutes what can I cook?
- I want to cook something but I have only [40](max_minutes) minutes
- what can i cook in [60](max_minutes) minutes?
- what can i cook in [30](max_minutes) minutes?
- what can i cook in [thirty](max_minutes) minutes?
- what can i cook in [fifty](max_minutes) minutes?
- find a recipe that i can prepare in [45](max_minutes) minutes
- find a recipe ready in [45](max_minutes) minutes
- find a recipe ready in maximum [60](max_minutes) minutes

- I am looking for [gluten free]{"entity": "gluten_free", "value": "true"} recipe"
- Tell me some recipe for a dish [without gluten]{"entity": "gluten_free", "value": "true"}
- What can you suggest me to cook for [celiac]{"entity": "gluten_free", "value": "true"}?
- What can you suggest me to prepare [without gluten]{"entity": "gluten_free", "value": "true"}?
- What can I cook [gluten-free]{"entity": "gluten_free", "value": "true"}?
- What can I prepare [gluten free]{"entity": "gluten_free", "value": "true"}?

- What can you suggest me to cook for [vegetarian]{"entity": "vegetarian", "value": "true"}?
- i want to cook [vegetarian]{"entity": "vegetarian", "value": "true"}
- find some [vegetarian]{"entity": "vegetarian", "value": "true"} recipes
- find some recipes for [vegetarians]{"entity": "vegetarian", "value": "true"}
- i need a [vegetarian]{"entity": "vegetarian", "value": "true"} recipe

- What can you suggest me to cook for [vegan]{"entity": "vegan", "value": "true"}?
- i want to cook [vegan]{"entity": "vegan", "value": "true"}
- find some [vegan]{"entity": "vegan", "value": "true"} recipes
- fid some recipes for [vegan]{"entity": "vegan", "value": "true"}
- i need a [vegan]{"entity": "vegan", "value": "true"} recipe

- I want to cook something with maximum [200](max_calories) calories
- What can I cook with only [100](max_calories) calories?
- i should assume only [150](max_calories) calories
- find a recipe with maximum [170](max_calories) calories
- What can I cook with maximum [150](max_calories) calories?
- i need a recipe with only [150](max_calories) calories
- i need a recipe with maximum [150](max_calories) calories

- I want something without [peppers](avoid_ingredients)
- I don't have any [eggs](avoid_ingredients)
- I don't like [eggs](avoid_ingredients)
- I don't want [eggs](avoid_ingredients) and [chicken](avoid_ingredients)
- what can i cook without [eggs](avoid_ingredients)?
- what can i cook without using [lemons](avoid_ingredients)?
- what can i cook without using [carrots](avoid_ingredients) and [potatoes](avoid_ingredients)?
- find a recipe without [cucumber](avoid_ingredients)

- what can i cook in [60](max_minutes) minutes and maximum [200](max_calories) calories
- what can i cook in [60](max_minutes) minutes with [200](max_calories) calories
- i need a recipe ready in [70](max_minutes) minutes with maximum [140](max_calories) calories
- i need some recipes ready in [30](max_minutes) minutes and maximum [20](max_calories) calories
- i want a recipe with maximum [300](max_calories) calories but i have only [25](max_minutes) minutes

- find a recipe for a [dessert](search_text) with [strawberries](search_ingredients)
- find a recipe for a [cake](search_text) where i can use [raspberries](search_ingredients)

- find a recipe for a [dessert](search_text) without [strawberries](avoid_ingredients)

- find a recipe [without gluten]{"entity": "gluten_free", "value": "true"} where i can use [salad](search_ingredients)

- find a recipe for [vegetarians]{"entity": "vegetarian", "value": "true"} where i can use [salad](search_ingredients)

- find a recipe for [vegan]{"entity": "vegan", "value": "true"} where i can use [salad](search_ingredients)

## intent:choose_recipe
- I want to cook the first one
- I like the first recipe
- I like the second recipe
- I like the second one
- the first one
- the second one
- the third one
- the last one
- the first recipe

## intent:get_recipe_info
- Tell me the details
- Explain it better
- Describe it
- Tell me about the first one
- Describe the second recipe

## intent:get_recipe_ingredients
- Tell me the ingredients
- Explain the ingredients
- Ingredients needed?
- What are the ingredients?
- Its ingredients?
- tell me the ingredients of the third one
- the ingredients for the second one?

## intent:get_recipe_nutrition
- Tell me the nutrition info of the first one
- What about the nutrition info of the second recipe?
- Talk about the nutrition
- What are the nutrition values?
- Tell me its nutrition

## intent:get_recipe_steps
- Can you explain to me the steps
- Tell me the steps needed
- Tell me the steps required
- Explain the procedure
- Tell me about the steps
- What are the steps?
- What is the procedure?
- Tell me how can I make it

## intent:start_cooking
- OK, I'm ready to start
- Let's start!
- Let's cook it
- Let's prepare it
- OK go on
- I'm ready
- I decided to make it
- I decided to prepare the second recipe
- I want to do the first one
- I want to do the first recipe
- I want to cook the first of the list

## intent:next_step
- I've done
- Go on
- Next step
- I'm ready
- What's next?
- Next one
