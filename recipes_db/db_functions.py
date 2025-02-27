from .models import *


def search_recipes(max_minutes, gluten_free, vegetarian, vegan, max_calories,
                   search_ingredients, avoid_ingredients, page=1, search_text=''):

    recipes = Recipe.select().join(RecipeTag)

    if search_text is not None:
        recipes = recipes.where(Recipe.name.contains(search_text))
    if max_minutes is not None:
        recipes = recipes.where(Recipe.preparation_minutes <= max_minutes)
    if gluten_free:
        recipes = recipes.where(RecipeTag.tag == 'gluten-free')
    if vegetarian:
        recipes = recipes.where(RecipeTag.tag == 'vegetarian')
    if vegan:
        recipes = recipes.where(RecipeTag.tag == 'vegan')
    if max_calories is not None:
        recipes = recipes.where(Recipe.calories <= max_calories)

    if avoid_ingredients is not None:
        for ing in avoid_ingredients:
            recipes_ing = RecipeIngredient.select(RecipeIngredient.recipe).where(RecipeIngredient.ingredient.contains(ing))
            recipes = recipes.where(Recipe.id.not_in(recipes_ing))

    if search_ingredients is not None:
        for ing in search_ingredients:
            ing_alias = RecipeIngredient.alias()
            recipes = recipes.join(ing_alias, on=(Recipe.id == ing_alias.recipe)) \
                .where(ing_alias.ingredient.contains(ing))

    recipes = recipes.distinct().paginate(page, 5)
    return list(recipes)
