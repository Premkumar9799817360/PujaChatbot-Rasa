from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import re
# from testing import insert_data   # for database
# from ema import send_email
from rasa_sdk.events import EventType
from rasa_sdk import Action, Tracker
# import string

# for first action  it is not used in project
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!, Develoer ")

        return []

#for second action it is not used in our project , using only learning purpose
class ActionImage(Action):

    def name(self) -> Text:
        return "action_image"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here is something to cheer you up 😉", image="https://i.imgur.com/nGF1K8f.jpg")

        return []
    

class ActionProvidePujaDetails(Action):
    def name(self) -> Text:
        return "action_provide_puja_details"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict
    ) -> List[EventType]:
        intent = tracker.latest_message.get("intent", {}).get("name")

        if intent == "select_special_puja":
            dispatcher.utter_message(response="utter_special_puja_selected")

        elif intent == "select_personal_puja":
            dispatcher.utter_message(response="utter_personal_puja_selected")

        elif intent == "select_daily_puja":
            dispatcher.utter_message(response="utter_daily_puja_selected")

        elif intent == "select_festival_puja":
            dispatcher.utter_message(response="utter_festival_puja_selected")

        return []
    

class ActionProvideSpecialPujaDetails(Action):
    def name(self) -> Text:
        return "action_provide_special_puja_details"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[EventType]:
        intent = tracker.latest_message.get("intent", {}).get("name")

        if intent == "select_durga_puja":
            dispatcher.utter_message(response="utter_durga_puja_selected")

        elif intent == "select_lakshmi_puja":
            dispatcher.utter_message(response="utter_lakshmi_puja_selected")

        elif intent == "select_ganesh_chaturthi_puja":
            dispatcher.utter_message(response="utter_ganesh_chaturthi_puja_selected")

        elif intent == "select_satyanarayan_puja":
            dispatcher.utter_message(response="utter_satyanarayan_puja_selected")

        elif intent == "select_maha_shivaratri_puja":
            dispatcher.utter_message(response="utter_maha_shivaratri_puja_selected")

        elif intent == "select_navagraha_puja":
            dispatcher.utter_message(response="utter_navagraha_puja_selected")

        elif intent == "select_saraswati_puja":
            dispatcher.utter_message(response="utter_saraswati_puja_selected")

        elif intent == "select_kali_puja":
            dispatcher.utter_message(response="utter_kali_puja_selected")

        elif intent == "select_chandi_puja":
            dispatcher.utter_message(response="utter_chandi_puja_selected")

        elif intent == "select_pitru_paksha_puja":
            dispatcher.utter_message(response="utter_pitru_paksha_puja_selected")

        return []
    



class ActionProvideDailyPujaDetails(Action):
    def name(self) -> Text:
        return "action_provide_daily_puja_details"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[EventType]:
        intent = tracker.latest_message.get("intent", {}).get("name")
        if intent == "select_sandhya_vandana":
            dispatcher.utter_message(response="utter_sandhya_vandana_selected")
        elif intent == "select_tulsi_puja":
            dispatcher.utter_message(response="utter_tulsi_puja_selected")
        elif intent == "select_surya_namaskar":
            dispatcher.utter_message(response="utter_surya_namaskar_selected")
        elif intent == "select_gayatri_mantra_japa":
            dispatcher.utter_message(response="utter_gayatri_mantra_japa_selected")
        elif intent == "select_agnihotra":
            dispatcher.utter_message(response="utter_agnihotra_selected")
        elif intent == "select_deva_darshan":
            dispatcher.utter_message(response="utter_deva_darshan_selected")
        elif intent == "select_hanuman_chalisa":
            dispatcher.utter_message(response="utter_hanuman_chalisa_selected")

        return []
    

class ActionProvideDailyPujaDetails(Action):
    def name(self) -> Text:
        return "action_provide_personal_puja_details"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[EventType]:
        intent = tracker.latest_message.get("intent", {}).get("name")

        if intent == "select_griha_pravesh_puja":
            dispatcher.utter_message(response="utter_griha_pravesh_puja_selected")
        elif intent == "select_birthday_puja":
            dispatcher.utter_message(response="utter_birthday_puja_selected")
        elif intent == "select_vivah_puja":
            dispatcher.utter_message(response="utter_vivah_puja_selected")
        elif intent == "select_sankalp_puja":
            dispatcher.utter_message(response="utter_sankalp_puja_selected")
        elif intent == "select_namkaran_puja":
            dispatcher.utter_message(response="utter_namkaran_puja_selected")
        elif intent == "select_sundarkand_path":
            dispatcher.utter_message(response="utter_sundarkand_path_selected")

        return []
    

class ActionProvideDailyPujaDetails(Action):
    def name(self) -> Text:
        return "action_provide_fesival_puja_details"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[EventType]:
        intent = tracker.latest_message.get("intent", {}).get("name")

        if intent == "select_makar_sankranti":
            dispatcher.utter_message(response="utter_makar_sankranti_selected")
        elif intent == "select_maha_shivaratri":
            dispatcher.utter_message(response="utter_maha_shivaratri_selected")
        elif intent == "select_holi_dahan":
            dispatcher.utter_message(response="utter_holi_dahan_selected")
        elif intent == "select_ram_navami":
            dispatcher.utter_message(response="utter_ram_navami_selected")
        elif intent == "select_raksha_bandhan":
            dispatcher.utter_message(response="utter_raksha_bandhan_selected")
        elif intent == "select_krishna_janmashtami":
            dispatcher.utter_message(response="utter_krishna_janmashtami_selected")
        elif intent == "select_ganesha_chaturthi":
            dispatcher.utter_message(response="utter_ganesha_chaturthi_selected")
        elif intent == "select_navratri":
            dispatcher.utter_message(response="utter_navratri_selected")
        elif intent == "select_karwa_chauth":
            dispatcher.utter_message(response="utter_karwa_chauth_selected")
        elif intent == "select_dhanteras":
            dispatcher.utter_message(response="utter_dhanteras_selected")
        elif intent == "select_diwali":
            dispatcher.utter_message(response="utter_diwali_selected")

        return []
    



# Puja Samgris
class ActionIntoShowCarousel(Action):

    def name(self) -> Text:
        return "actions_puja_samgri_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Puja Items",
                        "subtitle": "Essential Items for Your Puja",
                        "image_url": "Puja Images/pujaitems.jpg",
                        "buttons": [
                            {
                                "title": "Buy Now",
                                "url": "https://k2k-it-ai.solutions/",
                                "type": "web_url"
                            },
                            {
                                "title": "Details",
                                "type": "postback",
                                "payload": "/Puja_items_details"
                            },
                            {
                                "title": "Contact",
                                "type": "postback",
                                "payload": "/contact_details"
                            }
                        ]
                    },
                    {
                        "title": "Puja Status",
                        "subtitle": "Track Your Puja Status",
                        "image_url": "Puja Images/pujastatus.jpg",
                        "buttons": [
                            {
                                "title": "Check Status",
                                "url": "https://k2k-it-ai.solutions/",
                                "type": "web_url"
                            },
                            {
                                "title": "Details",
                                "type": "postback",
                                "payload": "/Puja_status_details"
                            },
                            {
                                "title": "Contact",
                                "type": "postback",
                                "payload": "/contact_details"
                            }
                        ]
                    },
                    {
                        "title": "Puja Ornaments",
                        "subtitle": "Beautiful Ornaments for Puja",
                        "image_url": "Puja Images/pujaornaments.jpg",
                        "buttons": [
                            {
                                "title": "Buy Ornaments",
                                "url": "https://k2k-it-ai.solutions/",
                                "type": "web_url"
                            },
                            {
                                "title": "Details",
                                "type": "postback",
                                "payload": "/Puja_ornaments_details"
                            },
                            {
                                "title": "Contact",
                                "type": "postback",
                                "payload": "/contact_details"
                            }
                        ]
                    },
                    {
                        "title": "Puja Cloths",
                        "subtitle": "Traditional Cloths for Puja",
                        "image_url": "Puja Images/puja cloths.jpg",
                        "buttons": [
                            {
                                "title": "Buy Cloths",
                                "url": "https://k2k-it-ai.solutions/",
                                "type": "web_url"
                            },
                            {
                                "title": "Details",
                                "type": "postback",
                                "payload": "/Puja_cloths_details"
                            },
                            {
                                "title": "Contact",
                                "type": "postback",
                                "payload": "/contact_details"
                            }
                        ]
                    }
                ]
            }
        }
        dispatcher.utter_message(text="Select Puja Samagari", attachment=new_carousel)
        return []
