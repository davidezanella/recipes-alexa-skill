## intent:greet
- good morning
- hey there

## intent:search_recipe
- I have [30](max_minutes) minutes what can I prepare?
- find a recipe without [honey](avoid_ingredients)
- i need a recipe where i can use [cardamom](search_ingredients)
- i want to cook something for [vegans]{"entity": "vegan", "value": "true"} using [strawberries](search_ingredients)
- search some recipes with maximum [175](max_calories) calories
- find a recipe for a [dessert](search_text) with [strawberries](search_ingredients)
- find some recipes for [vegetarians]{"entity": "vegetarian", "value": "true"}
- i would like to cook the [spaghetti](search_text)
- give me some recipes to cook using [salad](search_ingredients)
- I want to cook something but I have only [40](max_minutes) minutes
- find the recipe of the [strudel](search_text)
- find a recipe where i can cook using [cucumber](search_ingredients)
- what can i cook for [dessert](search_text)?
- what can i cook in [30](max_minutes) minutes?
- What can i cook using [basil](search_ingredients)?
- What can i cook using [avocado](search_ingredients)?
- what can i cook without [eggs](avoid_ingredients)?
- what can i cook in [fifty](max_minutes) minutes?
- Tell me some recipe for a dish [without gluten]{"entity": "gluten_free", "value": "true"}
- i should assume only [150](max_calories) calories
- search the recipe of [meet](search_text)
- What can you suggest me to cook for [vegan]{"entity": "vegan", "value": "true"}?
- I want to cook using [cabbage](search_ingredients) and [eggplant](search_ingredients)
- avoid recipes with [crab](avoid_ingredients)
- i need a recipe where i can use [sugar](search_ingredients)
- i need a recipe with only [168](max_calories) calories
- what can i cook in [60](max_minutes) minutes and maximum [200](max_calories) calories

## intent:next_page
- search other recipes
- more recipes please
- Alternatives?
- search others

## intent:choose_recipe
- the second one
- I like the first recipe

## intent:get_recipe_info
- Tell me more about it
- How much time needed?

## intent:get_recipe_ingredients
- Explain the ingredients needed for the first one
- Explain the ingredients
- the ingredients for the second one?

## intent:get_recipe_nutrition
- Tell me about the nutrition info
- Talk about the nutrition

## intent:get_recipe_steps
- Tell me about the steps
- Describe the steps

## intent:start_cooking
- I want to do the first one
- I decided to prepare the second recipe
- I want to cook the first one

## intent:next_step
- Go on
- What's the next step?

## intent:clear_search
- Forget the previous filters
- I want to search another recipe

## intent:affirm
- Sure
- amazing!
- yes please
- yes
- absolutely
- i will!
- great
- I'm sure I will!

## intent:deny
- No, not really.
- nah
- deny
- not really
- i'm afraid not

## synonym:true
- gluten free
- without gluten
- celiac
- gluten-free
- vegetarian
- vegetarians
- vegan
- vegans
