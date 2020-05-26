import csv
import json
import peewee
from tqdm import tqdm
from models import *


def clean_parse_json(text):
    text = '`'.join(text.split('"'))
    text = '"'.join(text.split("'"))
    return json.loads(text)


db.create_tables([Tag, Ingredient, Recipe, Step, RecipeTag, RecipeIngredient])

with open('RAW_recipes.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    recipes = []
    tags = []
    recipe_tags = []
    ingredients = []
    recipe_ingredients = []
    steps = []

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        r = {'id': row['id'], 'name': row['name'], 'preparation_minutes': row['minutes'],
             'description': row['description'], 'calories': json.loads(row['nutrition'])[0],
             'total_fat_perc': json.loads(row['nutrition'])[1], 'sugar_perc': json.loads(row['nutrition'])[2],
             'sodium_perc': json.loads(row['nutrition'])[3], 'protein_perc': json.loads(row['nutrition'])[4],
             'saturated_fat_perc': json.loads(row['nutrition'])[5],
             'total_carbohydrate_perc': json.loads(row['nutrition'])[6]}
        recipes.append(r)

        for tag in clean_parse_json(row['tags']):
            t = {
                'name': tag
            }
            tags.append(t)
            recipe_tags.append({
                'recipe': r['id'],
                'tag': tag
            })

        try:
            for ing in clean_parse_json(row['ingredients']):
                ingredients.append({
                    'name': ing
                })
                recipe_ingredients.append({
                    'recipe': r['id'],
                    'ingredient': ing
                })

            for i, step in enumerate(clean_parse_json(row['steps'])):
                steps.append({
                    'index': i,
                    'text': step,
                    'recipe': r['id']
                })
        except json.decoder.JSONDecodeError:
            recipes = recipes[:-1]

    with db.atomic():
        for data_dict in tqdm(recipes):
            Recipe.create(**data_dict)
    print("Recipes inserted")
    
    with db.atomic():
        for data_dict in tqdm(tags):
            Tag.get_or_create(**data_dict)
    print("Tags inserted")
    with db.atomic():
        for data_dict in tqdm(recipe_tags):
            RecipeTag.create(**data_dict)
    print("Recipe tags inserted")
    with db.atomic():
        for data_dict in tqdm(ingredients):
            Ingredient.get_or_create(**data_dict)
    print("Ingredients inserted")
    with db.atomic():
        for data_dict in tqdm(recipe_ingredients):
            RecipeIngredient.create(**data_dict)
    print("Recipe ingredients inserted")
    with db.atomic():
        for data_dict in tqdm(steps):
            Step.create(**data_dict)
    print("Steps inserted")
