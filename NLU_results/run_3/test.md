## intent:greet
- hello
- good evening

## intent:search_recipe
- what can i cook for [vegetarians]{"entity": "vegetarian", "value": "true"}?
- i don't want recipes with [bacon](avoid_ingredients)
- find a recipe without [honey](avoid_ingredients)
- I want something without [peppers](avoid_ingredients)
- I have [30](max_minutes) minutes what can I prepare?
- what can i cook in [30](max_minutes) minutes?
- find a recipe for a [cake](search_text) where i can use [raspberries](search_ingredients)
- i would like to cook the [spaghetti](search_text)
- What can i cook using [eggs](search_ingredients)?
- i want to cook something for [vegans]{"entity": "vegan", "value": "true"} using [strawberries](search_ingredients)
- avoid recipes with [peach](avoid_ingredients)
- find a recipe where i can cook using [cucumber](search_ingredients)
- what can i cook without using [caramel](avoid_ingredients)?
- i want the recipe of [lasagna](search_text)
- I want something without [coconut](avoid_ingredients)
- I have some [eggs](search_ingredients) what can i prepare?
- i need to cook for [vegetarians]{"entity": "vegetarian", "value": "true"}
- what can i cook in [60](max_minutes) minutes and maximum [200](max_calories) calories
- i don't want recipes with [potatoes](avoid_ingredients)
- What can i cook using [avocado](search_ingredients)?
- I don't have any [pers](avoid_ingredients)
- find a recipe where i can use [strawberries](search_ingredients) but without [salad](avoid_ingredients)
- i need a [vegetarian]{"entity": "vegetarian", "value": "true"} recipe
- I don't want [mango](avoid_ingredients) or [watermelon](avoid_ingredients)
- avoid recipes with [lamb](avoid_ingredients)
- What can i cook using [beef](search_ingredients)?
- What can you suggest me to cook for [celiac]{"entity": "gluten_free", "value": "true"}?

## intent:next_page
- Find others
- more recipes please
- find other recipes
- Other options?

## intent:choose_recipe
- what about the second one?
- what about the forth recipe?

## intent:get_recipe_info
- Tell me about the first one
- Tell me the details

## intent:get_recipe_ingredients
- the ingredients for the second one?
- What do I need for the first recipe?
- What are the ingredients for the second one?

## intent:get_recipe_nutrition
- Tell me its calories
- Talk about the nutrition

## intent:get_recipe_steps
- What are the steps?
- Tell me the procedure

## intent:start_cooking
- I want to do the first one
- Let's cook it
- I want to cook the first of the list

## intent:next_step
- What's the next step?
- I've done

## intent:clear_search
- Start a new search
- I want to search another recipe

## intent:affirm
- definitely yes without a doubt
- yes please!
- I'm sure I will!
- of course
- sure
- absolutely
- Sweet
- yes i accept

## intent:deny
- never
- neither of these
- never mind
- not really
- nah not for me

## synonym:true
- gluten free
- without gluten
- celiac
- gluten-free
- vegetarian
- vegetarians
- vegan
- vegans
