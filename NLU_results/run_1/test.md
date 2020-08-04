## intent:greet
- good morning
- hi

## intent:search_recipe
- find a recipe where i can use [strawberries](search_ingredients) but without [salad](avoid_ingredients)
- I want something without [coconut](avoid_ingredients)
- i need a recipe with only [168](max_calories) calories
- i want to cook something for [vegetarians]{"entity": "vegetarian", "value": "true"} using [strawberries](search_ingredients)
- search recipes to use [zucchini](search_ingredients)
- What can I cook with maximum [150](max_calories) calories?
- find a recipe ready in maximum [60](max_minutes) minutes
- I am looking for [gluten free]{"entity": "gluten_free", "value": "true"} recipe"
- find a recipe ready in [45](max_minutes) minutes
- what can i cook in [60](max_minutes) minutes with [200](max_calories) calories
- find a recipe with maximum [170](max_calories) calories
- what can i cook in [thirty](max_minutes) minutes?
- what can i cook without using [grapes](avoid_ingredients) or [banana](avoid_ingredients)?
- find a recipe for a [dessert](search_text) with [strawberries](search_ingredients)
- what can i cook without [eggs](avoid_ingredients)?
- recipes with maximum [170](max_calories) calories?
- What can I cook [gluten-free]{"entity": "gluten_free", "value": "true"}?
- I want something without [peppers](avoid_ingredients)
- i need a [vegan]{"entity": "vegan", "value": "true"} recipe
- I don't like [kiwi](avoid_ingredients)
- what can i cook for [vegans]{"entity": "vegan", "value": "true"}?
- find a recipe for [vegetarians]{"entity": "vegetarian", "value": "true"} where i can use [salad](search_ingredients)
- i need a recipe where i can use [red chilly](search_ingredients)
- search recipes to use [milk](search_ingredients)
- What can you suggest me to cook for [vegetarian]{"entity": "vegetarian", "value": "true"}?
- what can i cook without [cane sugar](avoid_ingredients)?
- I want to cook something but I have only [40](max_minutes) minutes

## intent:next_page
- search other recipes
- find other recipes
- more recipes please
- Find another one

## intent:choose_recipe
- the third one
- I like the second one

## intent:get_recipe_info
- Tell me more about it
- Give details about the second one

## intent:get_recipe_ingredients
- Tell me the ingredients
- tell me about the ingredients required by the third one
- Ingredients needed?

## intent:get_recipe_nutrition
- Talk about the nutrition
- Tell me its nutrition

## intent:get_recipe_steps
- Describe the steps
- Tell me how can I make it

## intent:start_cooking
- Let's cook the first recipe
- I decided to prepare the second recipe
- Let's start!

## intent:next_step
- The next step?
- I'm ready

## intent:clear_search
- Remove th previous filters
- I want to search another recipe

## intent:affirm
- cool
- Sure
- cool!
- ok cool
- go for it
- yes
- Oh, ok
- absolutely

## intent:deny
- deny
- neither of these
- i decline
- no
- not really

## synonym:true
- gluten free
- without gluten
- celiac
- gluten-free
- vegetarian
- vegetarians
- vegan
- vegans
