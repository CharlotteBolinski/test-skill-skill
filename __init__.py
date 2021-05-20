from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class TestSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skill.test.intent')
    def handle_skill_test(self, message):
        self.speak_dialog('skill.test')

    @intent_handler(IntentBuilder('ThankYouIntent').require('ThankYouKeyword'))
    def handle_thank_you_intent(self, message):
        self.speak_dialog("welcome")

def create_skill():
    return TestSkill()

