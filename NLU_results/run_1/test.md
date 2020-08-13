## intent:greet
- hey there
- good morning

## intent:search_recipe
- i need some recipes for [vegan]{"entity": "vegan", "value": "true"}
- I have some [radish](search_ingredients) what can i prepare?
- What can I cook with only [100](max_calories) calories?
- find a recipe for a [dessert](search_text) with [strawberries](search_ingredients)
- I have some [eggs](search_ingredients) what can i prepare?
- avoid recipes with [crab](avoid_ingredients)
- find a recipe for [vegetarians]{"entity": "vegetarian", "value": "true"} where i can use [salad](search_ingredients)
- What can I prepare [gluten free]{"entity": "gluten_free", "value": "true"}?
- avoid recipes with [tomatoes](avoid_ingredients)
- i need dishes [vegetarians]{"entity": "vegetarian", "value": "true"}
- recipes with maximum [170](max_calories) calories?
- i need a recipe where i can use [cardamom](search_ingredients)
- i have to prepare some [vegan]{"entity": "vegan", "value": "true"} dishes
- avoid recipes with [lamb](avoid_ingredients)
- i need the recipe of [muffins](search_text)
- I want to cook using [cabbage](search_ingredients) and [eggplant](search_ingredients)
- I have some [peppers](search_ingredients) what can i cook?
- I want to cook something but I have only [40](max_minutes) minutes
- What can I cook [gluten-free]{"entity": "gluten_free", "value": "true"}?
- find some dishes for [vegetarians]{"entity": "vegetarian", "value": "true"}
- i want to cook [vegan]{"entity": "vegan", "value": "true"}
- i don't want recipes with [bacon](avoid_ingredients)
- i need a recipe where i can use [mint](search_ingredients)
- find a recipe for a [dessert](search_text) without [strawberries](avoid_ingredients)
- I want to cook something using [acacia](search_ingredients)
- I want to cook something using [carrots](search_ingredients)
- find a recipe where i can cook using [parsley](search_ingredients)

## intent:next_page
- find another recipe
- I don't like them
- search others
- Find another one

## intent:choose_recipe
- I like the second one
- the second one

## intent:get_recipe_info
- Tell me the details
- Tell me more about it

## intent:get_recipe_ingredients
- What are its ingredients?
- the ingredients for the second one?
- Explain the ingredients

## intent:get_recipe_nutrition
- Tell me about the nutrition info
- Tell me its calories

## intent:get_recipe_steps
- Can you explain to me the steps
- Tell me the steps needed

## intent:start_cooking
- OK, I'm ready to start
- Let's start!
- Let's prepare it

## intent:next_step
- Go on
- What's the next step?

## intent:clear_search
- Start a new search
- Reset the search

## intent:affirm
- ok i accept
- amazing
- perfect
- go for it
- amazing!
- I accept
- how nice!
- i accept

## intent:deny
- not really
- no i don't
- no you did it wrong
- nah
- never

## synonym:true
- gluten free
- without gluten
- celiac
- gluten-free
- vegetarian
- vegetarians
- vegan
- vegans
