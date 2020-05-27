from .models import *


def search_recipes(max_minutes, gluten_free, vegetarian, vegan, max_calories,
                   search_ingredients, avoid_ingredients, page=1, name=''):

    recipes = Recipe.select().where(Recipe.name.contains(name)).join(RecipeTag)

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

    avoid_rec_id = set()

    if avoid_ingredients is not None:
        for ing in avoid_ingredients:
            recipes_ing = RecipeIngredient.select().where(RecipeIngredient.ingredient.contains(ing))
            for rec in recipes_ing:
                avoid_rec_id.add(rec.recipe.id)
        recipes = recipes.where(Recipe.id.not_in(avoid_rec_id))

    if search_ingredients is not None:
        for ing in search_ingredients:
            ing_alias = RecipeIngredient.alias()
            recipes = recipes.join(ing_alias, on=(Recipe.id == ing_alias.recipe)) \
                .where(ing_alias.ingredient.contains(ing))

    recipes = recipes.distinct().paginate(page, 5)
    return list(recipes)
