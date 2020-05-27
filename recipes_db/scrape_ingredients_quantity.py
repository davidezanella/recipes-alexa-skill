from bs4 import BeautifulSoup
import requests as r
from models import *
from tqdm import tqdm
from multiprocessing import Pool


base_url = 'https://www.food.com/recipe/'
recipes = Recipe.select()

to_update = []


def process_fn(recipe):
    url = base_url + str(recipe.id)
    page = r.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    ingredients = list(RecipeIngredient.select().where(RecipeIngredient.recipe == recipe))
    for ing in soup.select('.recipe-ingredients__ingredient'):
        qty = ing.select_one('.recipe-ingredients__ingredient-quantity').text
        name = ing.select_one('.recipe-ingredients__ingredient-parts').text
        for i in ingredients:
            if i.ingredient.name in name:
                if qty == '':
                    qty = "some"
                i.quantity = qty
                to_update.append(i)
                break
    return True


with Pool() as pool:
    i = 0
    for _ in tqdm(pool.imap_unordered(process_fn, recipes), total=len(recipes)):
        i += 1
        if i % 5000 == 0:
            with db.atomic():
                RecipeIngredient.bulk_update(to_update, fields=[RecipeIngredient.quantity], batch_size=50)
            to_update.clear()
            print('updated')

    with db.atomic():
        RecipeIngredient.bulk_update(to_update, fields=[RecipeIngredient.quantity], batch_size=50)
