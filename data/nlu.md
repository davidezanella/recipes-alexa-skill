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
#### search_ingredients
- I want to cook something using [carrots](search_ingredients)
- I want to cook something using [mushrooms](search_ingredients)
- I want to cook something using [acacia](search_ingredients)
- I want to cook using [potatoes](search_ingredients) and [chicken](search_ingredients)
- I want to cook using [corn](search_ingredients) and [broccoli](search_ingredients)
- I want to cook using [cabbage](search_ingredients) and [eggplant](search_ingredients)
- I have some [peppers](search_ingredients) what can i cook?
- I have some [onions](search_ingredients) what can i cook?
- I have some [eggs](search_ingredients) what can i prepare?
- I have some [radish](search_ingredients) what can i prepare?
- I have some [cinnamon](search_ingredients) what can i prepare?
- I have some [garlic](search_ingredients) what can i prepare?
- What can i cook using [beef](search_ingredients)?
- What can i cook using [eggs](search_ingredients)?
- What can i cook using [basil](search_ingredients)?
- What can i cook using [avocado](search_ingredients)?
- find a recipe where i can cook using [cucumber](search_ingredients)
- find a recipe where i can cook using [parsley](search_ingredients)
- give me some recipes to cook using [salad](search_ingredients)
- give me some recipes to cook using [mango](search_ingredients)
- i need a recipe where i can use [sugar](search_ingredients)
- i need a recipe where i can use [mint](search_ingredients)
- i need a recipe where i can use [salt](search_ingredients)
- i need a recipe where i can use [red chilly](search_ingredients)
- i need a recipe where i can use [cardamom](search_ingredients)
- search recipes to use [milk](search_ingredients)
- search recipes to use [zucchini](search_ingredients)
#### search_text
- I would like to prepare a [dessert](search_text)
- find the recipe of the [strudel](search_text)
- i want to cook the [angel pie](search_text)
- the recipe of the [carrots pie](search_text)?
- i would like to cook the [spaghetti](search_text)
- what can i cook for [dessert](search_text)?
- i need the recipe of [muffins](search_text)
- search the recipe of [meet](search_text)
- i want the recipe of [lasagna](search_text)
- search a recipe for [pizza](search_text)
#### max_minutes
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
#### gluten_free
- I am looking for [gluten free]{"entity": "gluten_free", "value": "true"} recipe
- Tell me some recipe for a dish [without gluten]{"entity": "gluten_free", "value": "true"}
- What can you suggest me to cook for [celiac]{"entity": "gluten_free", "value": "true"}?
- What can you suggest me to prepare [without gluten]{"entity": "gluten_free", "value": "true"}?
- What can I cook [gluten-free]{"entity": "gluten_free", "value": "true"}?
- What can I prepare [gluten free]{"entity": "gluten_free", "value": "true"}?
- I need a recipe [without gluten]{"entity": "gluten_free", "value": "true"}
- Search recipes [without gluten]{"entity": "gluten_free", "value": "true"}
- Find a recipe [without gluten]{"entity": "gluten_free", "value": "true"}
- Find a recipe for [celiac]{"entity": "gluten_free", "value": "true"}
#### vegetarian
- What can you suggest me to cook for [vegetarian]{"entity": "vegetarian", "value": "true"}?
- i want to cook [vegetarian]{"entity": "vegetarian", "value": "true"}
- find some [vegetarian]{"entity": "vegetarian", "value": "true"} recipes
- find some recipes for [vegetarians]{"entity": "vegetarian", "value": "true"}
- i need a [vegetarian]{"entity": "vegetarian", "value": "true"} recipe
- find a recipe for [vegetarians]{"entity": "vegetarian", "value": "true"}
- i need to cook for [vegetarians]{"entity": "vegetarian", "value": "true"}
- what can i cook for [vegetarians]{"entity": "vegetarian", "value": "true"}?
- find some dishes for [vegetarians]{"entity": "vegetarian", "value": "true"}
- i need dishes [vegetarians]{"entity": "vegetarian", "value": "true"}
#### vegan
- What can you suggest me to cook for [vegan]{"entity": "vegan", "value": "true"}?
- i want to cook [vegan]{"entity": "vegan", "value": "true"}
- find some [vegan]{"entity": "vegan", "value": "true"} recipes
- fid some recipes for [vegan]{"entity": "vegan", "value": "true"}
- i need a [vegan]{"entity": "vegan", "value": "true"} recipe
- what can i cook for [vegans]{"entity": "vegan", "value": "true"}?
- i need some recipes for [vegan]{"entity": "vegan", "value": "true"}
- i have to prepare some [vegan]{"entity": "vegan", "value": "true"} dishes
- search for [vegan]{"entity": "vegan", "value": "true"} recipes
- i need some [vegan]{"entity": "vegan", "value": "true"} recipes
#### max_calories
- I want to cook something with maximum [200](max_calories) calories
- What can I cook with only [100](max_calories) calories?
- i should assume only [150](max_calories) calories
- find a recipe with maximum [170](max_calories) calories
- What can I cook with maximum [150](max_calories) calories?
- i need a recipe with only [168](max_calories) calories
- i need a recipe with maximum [150](max_calories) calories
- i can assume only [270](max_calories) calories
- search some recipes with maximum [175](max_calories) calories
- recipes with maximum [170](max_calories) calories?
#### avoid_ingredients
- I want something without [peppers](avoid_ingredients)
- I want something without [apple](avoid_ingredients)
- I want something without [coconut](avoid_ingredients)
- I don't have any [eggs](avoid_ingredients)
- I don't have any [pers](avoid_ingredients)
- I don't have any [sultana](avoid_ingredients)
- I don't like [eggs](avoid_ingredients)
- I don't like [kiwi](avoid_ingredients)
- I don't want [eggs](avoid_ingredients) or [chicken](avoid_ingredients)
- I don't want [mango](avoid_ingredients) or [watermelon](avoid_ingredients)
- what can i cook without [eggs](avoid_ingredients)?
- what can i cook without [cane sugar](avoid_ingredients)?
- what can i cook without [cherry](avoid_ingredients)?
- what can i cook without using [lemons](avoid_ingredients)?
- what can i cook without using [caramel](avoid_ingredients)?
- what can i cook without using [apricots](avoid_ingredients)?
- what can i cook without using [carrots](avoid_ingredients) or [potatoes](avoid_ingredients)?
- what can i cook without using [grapes](avoid_ingredients) or [banana](avoid_ingredients)?
- find a recipe without [cucumber](avoid_ingredients)
- find a recipe without [honey](avoid_ingredients)
- avoid recipes with [tomatoes](avoid_ingredients)
- avoid recipes with [peach](avoid_ingredients)
- avoid recipes with [crab](avoid_ingredients)
- avoid recipes with [chops](avoid_ingredients)
- avoid recipes with [lamb](avoid_ingredients)
- i don't want recipes with [potatoes](avoid_ingredients)
- i don't want recipes with [bacon](avoid_ingredients)
#### max_minutes + max_calories
- what can i cook in [60](max_minutes) minutes and maximum [200](max_calories) calories
- what can i cook in [60](max_minutes) minutes with [200](max_calories) calories
- i need a recipe ready in [70](max_minutes) minutes with maximum [140](max_calories) calories
- i need some recipes ready in [30](max_minutes) minutes and maximum [20](max_calories) calories
- i want a recipe with maximum [300](max_calories) calories but i have only [25](max_minutes) minutes
#### search_text + search_ingredients
- find a recipe for a [dessert](search_text) with [strawberries](search_ingredients)
- find a recipe for a [cake](search_text) where i can use [raspberries](search_ingredients)
#### search_text + avoid_ingredients
- find a recipe for a [dessert](search_text) without [strawberries](avoid_ingredients)
- i want to cook a [pie](search_text) without using [apples](avoid_ingredients)
#### gluten_free + search_ingredients
- find a recipe [without gluten]{"entity": "gluten_free", "value": "true"} where i can use [salad](search_ingredients)
- i want to cook something [gluten-free]{"entity": "gluten_free", "value": "true"} but using [strawberries](search_ingredients)
#### vegetarians + search_ingredients
- find a recipe for [vegetarians]{"entity": "vegetarian", "value": "true"} where i can use [salad](search_ingredients)
- i want to cook something for [vegetarians]{"entity": "vegetarian", "value": "true"} using [strawberries](search_ingredients)
#### vegan + search_ingredients
- find a recipe for [vegan]{"entity": "vegan", "value": "true"} where i can use [salad](search_ingredients)
- i want to cook something for [vegans]{"entity": "vegan", "value": "true"} using [strawberries](search_ingredients)
#### search_ingredients + avoid_ingredients
- find a recipe where i can use [strawberries](search_ingredients) but without [salad](avoid_ingredients)
- i want to cook something using [raspberries](search_ingredients) but without using [strawberries](avoid_ingredients)

## intent:next_page
- Are there others?
- Any other?
- Find another one
- I don't like them
- Search more
- Alternatives?
- Other options?
- Other possibilities?
- Find others
- Find again
- search others
- more recipes please
- other recipes?
- find another recipe
- find other recipes
- search more recipes
- search other recipes
- other options?

## intent:choose_recipe
- I like the first recipe
- I like the second recipe
- I like the second one
- the first one
- the second one
- the third one
- the last one
- the first recipe
- what about the forth recipe?
- what about the second one?

## intent:get_recipe_info
- Tell me the details
- Explain it better
- Describe it
- Tell me about the first one
- Describe the second recipe
- Tell me more about it
- I want details about the first recipe
- Give details about the second one
- Tell me more about it
- How much time needed?
- How much time does the second recipe need?

## intent:get_recipe_ingredients
- Tell me the ingredients
- Tell me the ingredients needed by the first one
- Explain the ingredients
- Explain the ingredients needed for the first one
- Ingredients needed?
- What are the ingredients?
- What are its ingredients?
- Its ingredients?
- tell me the ingredients of the third one
- tell me about the ingredients required by the third one
- tell me about the ingredients required
- the ingredients for the second one?
- What do I need for the first recipe?
- What are the ingredients for the second one?

## intent:get_recipe_nutrition
- Tell me the nutrition info of the first one
- What about the nutrition info of the second recipe?
- Talk about the nutrition
- What are the nutrition values?
- Tell me its nutrition
- Tell me its calories
- How many calories does it have?
- Tell me about the nutrition info

## intent:get_recipe_steps
- Can you explain to me the steps
- Tell me the steps needed
- Tell me the steps required
- Explain the procedure
- Tell me about the steps
- What are the steps?
- What is the procedure?
- Tell me how can I make it
- Describe the steps
- Tell me the procedure

## intent:start_cooking
- OK, I'm ready to start
- Let's start!
- Let's cook it
- Let's prepare it
- Let's cook the first recipe
- I decided to make it
- I decided to prepare the second recipe
- I want to do the first one
- I want to do the first recipe
- I want to cook the first of the list
- I want to cook the first one

## intent:next_step
- I've done
- Go on
- Next step
- I'm ready
- What's next?
- Next one
- What's the next step?
- The next step?

## intent:clear_search
- Reset the search filters
- Reset the search
- Start a new search
- I want to search another recipe
- Reset my search
- Clear the search filters
- Remove th previous filters
- New search
- Forget the previous parameters
- Forget the previous filters

## intent:affirm
- yes
- of course
- sure
- yeah
- ok
- cool
- go for it
- yep
- I'm sure I will!
- accept
- I accept
- i accept
- ok i accept
- ok cool
- alright
- i will!
- yes please
- yes please!
- amazing
- confirm
- nice
- definitely yes without a doubt
- yup
- perfect
- sure thing
- absolutely
- Oh, ok
- Sure
- sure!
- yes i accept
- Sweet
- amazing!
- how nice!
- cool!
- great
- oh cool
- yes, let's cook it
- sure, I want to cook it
- sure, i do
- yes i do

## intent:deny
- no
- definitely not
- never
- absolutely not
- i don't think so
- i'm afraid not
- no sir
- no way
- no sorry
- No, not really.
- nah not for me
- nah
- no thanks
- decline
- deny
- i decline
- never mind
- no
- no you did it wrong
- no i don't
- i'm not sure
- not really
- i don't want to
- i don't want either of those
- nah thanks
- neither of these

## synonym:true
- gluten free
- without gluten
- celiac
- gluten-free
- vegetarian
- vegetarians
- vegan
