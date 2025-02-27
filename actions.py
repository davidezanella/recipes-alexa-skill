# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from recipes_db.models import Step, RecipeIngredient
from recipes_db.db_functions import search_recipes

from utils import string_to_bool, string_to_int, duckling_word_to_int


def map_entities(tracker, ner_ent_name, target_ent_name):
    entities = tracker.latest_message['entities']

    target_ents = list(filter(lambda x: x['entity'] == target_ent_name, entities))
    if len(target_ents) == 0:
        return None

    target_ent = target_ents[0]
    ner_ents = list(filter(lambda x:
                           x['entity'] == ner_ent_name and
                           x['start'] == target_ent['start'] and
                           x['end'] == target_ent['end'], entities))

    if len(ner_ents) > 0:
        return ner_ents[0]['value']

    return None


class ActionFormSearchRecipe(FormAction):
    def name(self) -> Text:
        return "action_form_search_recipe"

    entities = [
        ("page", "page"), ("gluten_free", "gluten_free"), ("vegetarian", "vegetarian"), ("vegan", "vegan"),
        ("search_text", "search_text"), ("max_minutes", "max_minutes"), ("max_calories", "max_calories"),
        ("search_ingredients", "search_ingredients"), ("avoid_ingredients", "avoid_ingredients")
    ]

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """
        Returns all the non empty slots otherwise they will not be mapped to entities.
        """
        entities = []
        for ent in ActionFormSearchRecipe.entities:
            if map_entities(tracker, ent[1], ent[0]) is not None:
                entities.append(ent[0])
        return entities

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "page": self.from_entity(entity="page"),
            "search_text": self.from_entity(entity="search_text"),
            "max_minutes": self.from_entity(entity="max_minutes"),
            "gluten_free": self.from_entity(entity="gluten_free"),
            "vegetarian": self.from_entity(entity="vegetarian"),
            "vegan": self.from_entity(entity="vegan"),
            "max_calories": self.from_entity(entity="max_calories"),
            "search_ingredients": self.from_entity(entity="search_ingredients"),
            "avoid_ingredients": self.from_entity(entity="avoid_ingredients"),
        }

    def validate_page(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                      domain: Dict[Text, Any]) -> Dict[Text, Any]:
        return {"page": value}

    def validate_search_text(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                             domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if value is None:
            value = ""
        return {"search_text": value}

    def validate_max_minutes(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                             domain: Dict[Text, Any]) -> Dict[Text, Any]:
        return {"max_minutes": duckling_word_to_int(value)}

    def validate_gluten_free(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                             domain: Dict[Text, Any]) -> Dict[Text, Any]:
        return {"gluten_free": string_to_bool(value)}

    def validate_vegetarian(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                            domain: Dict[Text, Any]) -> Dict[Text, Any]:
        return {"vegetarian": string_to_bool(value)}

    def validate_vegan(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                       domain: Dict[Text, Any]) -> Dict[Text, Any]:
        return {"vegan": string_to_bool(value)}

    def validate_max_calories(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                              domain: Dict[Text, Any]) -> Dict[Text, Any]:
        return {"max_calories": duckling_word_to_int(value)}

    def validate_search_ingredients(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                                    domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if not isinstance(value, list):
            value = [value]
        return {"search_ingredients": value}

    def validate_avoid_ingredients(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker,
                                   domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if not isinstance(value, list):
            value = [value]
        return {"avoid_ingredients": value}

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:

        params = {}
        for ent in self.entities:
            params[ent[0]] = tracker.get_slot(ent[0])

        recipes = search_recipes(**params)

        print(ActionFormSearchRecipe.required_slots(tracker))
        print(params)
        print("-" * 15)

        if len(recipes) == 0:
            dispatcher.utter_message(text="No recipes found with this filters!")
        else:
            txt = ''
            for i, recipe in enumerate(recipes):
                idx = i + 1 + (params['page'] - 1) * 5
                txt += "{}: '{}'.\n".format(idx, recipe.name)
            dispatcher.utter_message(txt)

        old_recipes = tracker.get_slot("recipes")
        if old_recipes is None or params['page'] == 1:
            old_recipes = []
        recipes = old_recipes + list(map(lambda x: x.to_dict(), recipes))
        return [SlotSet("recipes", recipes)]


class ActionNextPage(Action):
    def name(self) -> Text:
        return "action_next_page"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
        page = int(tracker.get_slot("page")) + 1

        return [SlotSet("page", page)]


class ActionClearSearch(Action):
    def name(self) -> Text:
        return "action_clear_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
        slots = [SlotSet('page', 1), SlotSet('recipes', [])]
        for entity in ActionFormSearchRecipe.entities[1:]:
            slots.append(SlotSet(entity[0], None))
            slots.append(SlotSet(entity[1], None))

        dispatcher.utter_message("All the search filters have been cleared!")

        return slots


class ActionChooseRecipe(Action):
    def name(self) -> Text:
        return "action_choose_recipe"

    possible_slots = ['ordinal']

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
        chosen_recipe = None
        for slot in self.possible_slots:
            v = tracker.get_slot(slot)
            if v is not None:
                chosen_recipe = v
                break

        if chosen_recipe is None:
            dispatcher.utter_message(template="utter_rephrase")
            return []

        chosen_recipe = chosen_recipe - 1
        return [SlotSet("chosen_recipe", chosen_recipe)]


class ActionGetRecipeInfo(Action):
    def name(self) -> Text:
        return "action_get_recipe_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recipes = tracker.get_slot("recipes")
        chosen_recipe = tracker.get_slot("chosen_recipe")

        if chosen_recipe is None:
            dispatcher.utter_message(template="utter_rephrase")
            return []

        dispatcher.utter_message(text="The '{}' takes {} minutes to be done, and this is its description:\n{}".format(
            recipes[chosen_recipe]['name'], recipes[chosen_recipe]['preparation_minutes'],
            recipes[chosen_recipe]['description']))

        return []


class ActionGetRecipeIngredients(Action):
    def name(self) -> Text:
        return "action_get_recipe_ingredients"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recipes = tracker.get_slot("recipes")
        chosen_recipe = tracker.get_slot("chosen_recipe")

        if chosen_recipe is None:
            dispatcher.utter_message(template="utter_rephrase")
            return []

        txt = "To make the '{}' you will need:\n".format(recipes[chosen_recipe]['name'])
        for ing in RecipeIngredient.select().where(RecipeIngredient.recipe == recipes[chosen_recipe]['id']):
            text = ing.ingredient.name
            if ing.quantity not in [None, "", "some"]:
                text = ing.quantity + " " + text
            txt += text + ".\n"
        dispatcher.utter_message(txt)

        return []


class ActionGetRecipeNutrition(Action):
    def name(self) -> Text:
        return "action_get_recipe_nutrition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recipes = tracker.get_slot("recipes")
        chosen_recipe = tracker.get_slot("chosen_recipe")

        if chosen_recipe is None:
            dispatcher.utter_message(template="utter_rephrase")
            return []

        dispatcher.utter_message(text="This is the nutrition info for the '{}'. "
                                      "Calories: {}, total fat percentage: {} %, sugar percentage: {} %,"
                                      "sodium percentage: {} %, protein percentage: {} %,"
                                      "saturated fat percentage: {} %, total carbohydrate percentage: {} %".format(
            recipes[chosen_recipe]['name'],
            recipes[chosen_recipe]['calories'], recipes[chosen_recipe]['total_fat_perc'],
            recipes[chosen_recipe]['sugar_perc'], recipes[chosen_recipe]['sodium_perc'],
            recipes[chosen_recipe]['protein_perc'], recipes[chosen_recipe]['saturated_fat_perc'],
            recipes[chosen_recipe]['total_carbohydrate_perc']))

        return []


class ActionGetRecipeSteps(Action):
    def name(self) -> Text:
        return "action_get_recipe_steps"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recipes = tracker.get_slot("recipes")
        chosen_recipe = tracker.get_slot("chosen_recipe")

        if chosen_recipe is None:
            dispatcher.utter_message(template="utter_rephrase")
            return []

        txt = "This is the steps for the '{}'.\n".format(recipes[chosen_recipe]['name'])
        for step in Step.select().where(Step.recipe == recipes[chosen_recipe]['id']).order_by(Step.index):
            txt += str(step.index + 1) + ": " + step.text + ".\n"
        dispatcher.utter_message(txt)

        return []


class ActionStartCooking(Action):
    def name(self) -> Text:
        return "action_start_cooking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recipes = tracker.get_slot("recipes")
        chosen_recipe = tracker.get_slot("chosen_recipe")

        if chosen_recipe is None:
            dispatcher.utter_message(template="utter_rephrase")
            return []

        dispatcher.utter_message(text="Ok, so do you want to start preparing the '{}'?"
                                 .format(recipes[chosen_recipe]['name']))

        return [SlotSet("step_index", 0)]


class ActionNextStep(Action):
    def name(self) -> Text:
        return "action_next_step"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recipes = tracker.get_slot("recipes")
        chosen_recipe = tracker.get_slot("chosen_recipe")

        if chosen_recipe is None:
            dispatcher.utter_message(template="utter_rephrase")
            return []

        step_index = tracker.get_slot("step_index")
        steps = Step.select().where((Step.recipe == recipes[chosen_recipe]['id']) & (Step.index == step_index))
        if len(steps) > 0:
            dispatcher.utter_message(text=steps[0].text)
            step_index += 1
        else:
            dispatcher.utter_message(text="You've done! I hope it tastes good.")
            step_index = None
        return [SlotSet("step_index", step_index)]
