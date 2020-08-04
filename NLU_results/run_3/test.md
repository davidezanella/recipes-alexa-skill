## intent:greet
- good morning
- hi

## intent:search_recipe
- recipes with maximum [170](max_calories) calories?
- search for [vegan]{"entity": "vegan", "value": "true"} recipes
- I don't like [eggs](avoid_ingredients)
- I don't have any [eggs](avoid_ingredients)
- search the recipe of [meet](search_text)
- i don't want recipes with [bacon](avoid_ingredients)
- I want to cook something using [carrots](search_ingredients)
- i want to cook something using [raspberries](search_ingredients) but without using [strawberries](avoid_ingredients)
- I want to cook using [potatoes](search_ingredients) and [chicken](search_ingredients)
- I want something without [coconut](avoid_ingredients)
- what can i cook for [vegetarians]{"entity": "vegetarian", "value": "true"}?
- find a recipe for [vegetarians]{"entity": "vegetarian", "value": "true"} where i can use [salad](search_ingredients)
- search a recipe for [pizza](search_text)
- avoid recipes with [tomatoes](avoid_ingredients)
- what can i cook without [cherry](avoid_ingredients)?
- i need a [vegetarian]{"entity": "vegetarian", "value": "true"} recipe
- I am looking for [gluten free]{"entity": "gluten_free", "value": "true"} recipe"
- what can i cook without [eggs](avoid_ingredients)?
- i need a recipe where i can use [sugar](search_ingredients)
- I have some [garlic](search_ingredients) what can i prepare?
- what can i cook in [60](max_minutes) minutes?
- find a recipe without [cucumber](avoid_ingredients)
- what can i cook in [fifty](max_minutes) minutes?
- Find a recipe [without gluten]{"entity": "gluten_free", "value": "true"}
- find a recipe for [vegan]{"entity": "vegan", "value": "true"} where i can use [salad](search_ingredients)
- What can i cook using [eggs](search_ingredients)?
- find the recipe of the [strudel](search_text)

## intent:next_page
- search other recipes
- other recipes?
- Other options?
- other options?

## intent:choose_recipe
- I like the second one
- the first one

## intent:get_recipe_info
- Tell me more about it
- How much time needed?

## intent:get_recipe_ingredients
- Explain the ingredients
- What are the ingredients?
- Explain the ingredients needed for the first one

## intent:get_recipe_nutrition
- Tell me its calories
- Tell me the nutrition info of the first one

## intent:get_recipe_steps
- Tell me the steps needed
- Tell me how can I make it

## intent:start_cooking
- Let's cook the first recipe
- I want to do the first recipe
- I want to cook the first one

## intent:next_step
- Next step
- I've done

## intent:clear_search
- Reset the search filters
- New search

## intent:affirm
- Oh, ok
- sure thing
- oh cool
- sure
- yup
- ok i accept
- of course
- go for it

## intent:deny
- decline
- i don't want either of those
- nah
- no thanks
- i don't think so

## synonym:true
- gluten free
- without gluten
- celiac
- gluten-free
- vegetarian
- vegetarians
- vegan
- vegans
