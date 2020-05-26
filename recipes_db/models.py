from peewee import *


db = SqliteDatabase('recipes.db')


class BaseModel(Model):
    class Meta:
        database = db


class Tag(BaseModel):
    name = CharField(primary_key=True)


class Ingredient(BaseModel):
    name = CharField(primary_key=True)


class Recipe(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    preparation_minutes = IntegerField()
    calories = FloatField(default=0.0)
    total_fat_perc = FloatField(default=0.0)
    sugar_perc = FloatField(default=0.0)
    sodium_perc = FloatField(default=0.0)
    protein_perc = FloatField(default=0.0)
    saturated_fat_perc = FloatField(default=0.0)
    total_carbohydrate_perc = FloatField(default=0.0)
    description = CharField()


class Step(BaseModel):
    id = PrimaryKeyField()
    index = IntegerField()
    text = CharField()
    recipe = ForeignKeyField(Recipe, backref='step')


class RecipeTag(BaseModel):
    recipe = ForeignKeyField(Recipe, backref='recipe_tag')
    tag = ForeignKeyField(Tag, backref='recipe_tag')


class RecipeIngredient(BaseModel):
    recipe = ForeignKeyField(Recipe, backref='recipe_ingredient')
    ingredient = ForeignKeyField(Ingredient, backref='recipe_ingredient')
    quantity = CharField(default="1")
