# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from recipes_db.models import Step
from recipes_db.db_functions import search_recipes


class ActionSearchRecipe(Action):
    def name(self) -> Text:
        return "action_search_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recipes = search_recipes(page=tracker.get_slot("page"), name=tracker.get_slot("search_text"),
                                 max_minutes=tracker.get_slot("max_minutes"), gluten_free=tracker.get_slot("gluten_free"),
                                 vegetarian=tracker.get_slot("vegetarian"), vegan=tracker.get_slot("vegan"),
                                 max_calories=tracker.get_slot("max_calories"),
                                 search_ingredients=tracker.get_slot("search_ingredients"),
                                 avoid_ingredients=tracker.get_slot("avoid_ingredients"))
        if len(recipes) == 0:
            dispatcher.utter_message(text="No recipes found with this filters!")
        else:
            for i, recipe in enumerate(recipes):
                dispatcher.utter_message(text="{}° recipe: '{}'".format(i+1, recipe.name))

        return [SlotSet("recipes", recipes)]


class ActionChooseRecipe(Action):
    def name(self) -> Text:
        return "action_choose_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recipes = tracker.get_slot("recipes")
        chosen_recipe = tracker.get_slot("chosen_recipe")
        dispatcher.utter_message(text="Ok so you want the '{}'".format(recipes[chosen_recipe].name))

        return []


class ActionGetRecipeInfo(Action):
    def name(self) -> Text:
        return "action_get_recipe_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recipes = tracker.get_slot("recipes")
        chosen_recipe = tracker.get_slot("chosen_recipe")
        dispatcher.utter_message(text="This is the description for the '{}'".format(recipes[chosen_recipe].name))
        dispatcher.utter_message(text=recipes[chosen_recipe].description)

        return []


class ActionGetRecipeNutrition(Action):
    def name(self) -> Text:
        return "action_get_recipe_nutrition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recipes = tracker.get_slot("recipes")
        chosen_recipe = tracker.get_slot("chosen_recipe")
        dispatcher.utter_message(text="This is the nutrition info for the '{}'".format(recipes[chosen_recipe].name))
        dispatcher.utter_message(text="Calories: {}, total fat percentage: {} %, sugar percentage: {} %,"
                                      "sodium percentage: {} %, protein percentage: {} %,"
                                      "saturated fat percentage: {} %, total carbohydrate percentage: {} %".format(
            recipes[chosen_recipe].calories, recipes[chosen_recipe].total_fat_perc, recipes[chosen_recipe].sugar_perc,
            recipes[chosen_recipe].sodium_perc, recipes[chosen_recipe].protein_perc,
            recipes[chosen_recipe].saturated_fat_perc, recipes[chosen_recipe].total_carbohydrate_perc))

        return []


class ActionGetRecipeSteps(Action):
    def name(self) -> Text:
        return "action_get_recipe_steps"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recipes = tracker.get_slot("recipes")
        chosen_recipe = tracker.get_slot("chosen_recipe")
        dispatcher.utter_message(text="This is the steps for the '{}'".format(recipes[chosen_recipe].name))
        for step in Step.select().where(Step.recipe == recipes[chosen_recipe]).order_by(Step.index):
            dispatcher.utter_message(text=step.text)

        return []


class ActionStartCooking(Action):
    def name(self) -> Text:
        return "action_start_cooking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recipes = tracker.get_slot("recipes")
        chosen_recipe = tracker.get_slot("chosen_recipe")
        dispatcher.utter_message(text="Ok let's start doing the '{}'. "
                                      "Tell me when you're ready.".format(recipes[chosen_recipe].name))

        return [SlotSet("step_index", 0)]


class ActionNextStep(Action):
    def name(self) -> Text:
        return "action_next_step"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recipes = tracker.get_slot("recipes")
        chosen_recipe = tracker.get_slot("chosen_recipe")
        step_index = tracker.get_slot("step_index")
        steps = Step.select().where(Step.recipe == recipes[chosen_recipe] & Step.index == step_index)
        if len(steps) > 0:
            dispatcher.utter_message(text=steps[0].text)
            step_index += 1
        else:
            dispatcher.utter_message(text="You've done! I hopes it tastes good.")
            step_index = None
        return [SlotSet("step_index", step_index)]
