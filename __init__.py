from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class TestSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('skill.test.intent')
    def handle_skill_test(self, message):
        self.speak_dialog('skill.test')

    @intent_handler(IntentBuilder('HelloTest').require('HappyTest'))
    def handle_hello_world_intent(self, message):
        self.speak_dialog("first.test")

def create_skill():
    return TestSkill()

