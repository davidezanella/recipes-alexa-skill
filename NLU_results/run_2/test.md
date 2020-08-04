## intent:greet
- hey
- hi

## intent:search_recipe
- I have some [eggs](search_ingredients) what can i prepare?
- find some [vegetarian]{"entity": "vegetarian", "value": "true"} recipes
- what can i cook without using [grapes](avoid_ingredients) or [banana](avoid_ingredients)?
- What can I cook [gluten-free]{"entity": "gluten_free", "value": "true"}?
- What can I cook with maximum [150](max_calories) calories?
- i want to cook something for [vegans]{"entity": "vegan", "value": "true"} using [strawberries](search_ingredients)
- what can i cook without [cherry](avoid_ingredients)?
- I have some [cinnamon](search_ingredients) what can i prepare?
- what can i cook for [dessert](search_text)?
- I want to cook something using [carrots](search_ingredients)
- what can i cook without [eggs](avoid_ingredients)?
- give me some recipes to cook using [mango](search_ingredients)
- What can you suggest me to prepare [without gluten]{"entity": "gluten_free", "value": "true"}?
- i need a recipe where i can use [sugar](search_ingredients)
- i want to cook something for [vegetarians]{"entity": "vegetarian", "value": "true"} using [strawberries](search_ingredients)
- I don't like [eggs](avoid_ingredients)
- i need to cook for [vegetarians]{"entity": "vegetarian", "value": "true"}
- I have [30](max_minutes) minutes what can I prepare?
- find a recipe where i can cook using [parsley](search_ingredients)
- i want to cook a [pie](search_text) without using [apples](avoid_ingredients)
- I have [50](max_minutes) minutes what can I prepare?
- find a recipe [without gluten]{"entity": "gluten_free", "value": "true"} where i can use [salad](search_ingredients)
- I would like to prepare a [dessert](search_text)
- avoid recipes with [chops](avoid_ingredients)
- i need a recipe where i can use [mint](search_ingredients)
- what can i cook for [vegetarians]{"entity": "vegetarian", "value": "true"}?
- find a recipe where i can cook using [cucumber](search_ingredients)

## intent:next_page
- Find another one
- Other possibilities?
- Find others
- Are there others?

## intent:choose_recipe
- what about the second one?
- I like the first recipe

## intent:get_recipe_info
- How much time needed?
- Give details about the second one

## intent:get_recipe_ingredients
- What are the ingredients for the second one?
- Tell me the ingredients needed by the first one
- What are its ingredients?

## intent:get_recipe_nutrition
- Tell me its calories
- How many calories does it have?

## intent:get_recipe_steps
- Tell me the steps required
- Tell me the procedure

## intent:start_cooking
- Let's cook the first recipe
- I decided to prepare the second recipe
- Let's start!

## intent:next_step
- I've done
- What's next?

## intent:clear_search
- Remove th previous filters
- Reset my search

## intent:affirm
- yeah
- sure, i do
- accept
- I'm sure I will!
- sure!
- I accept
- alright
- Sure

## intent:deny
- no you did it wrong
- absolutely not
- nah thanks
- decline
- definitely not

## synonym:true
- gluten free
- without gluten
- celiac
- gluten-free
- vegetarian
- vegetarians
- vegan
- vegans
