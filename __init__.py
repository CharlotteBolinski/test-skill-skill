from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.context import adds_context, removes_context


class TestSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skill.test.intent')
    def handle_skill_test(self, message):
        self.speak_dialog('skill.test')

    @intent_handler(IntentBuilder("TeaIntent").require("bring").require("tea"))
    @adds_context("MilkContext")
    def handle_tea_intent(self, message):
        self.milk = False
        self.speak("Of course, would you like Milk with that?", expect_response=True)


def create_skill():
    return TestSkill()

