from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.skills.context import adds_context, removes_context

class TestSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('skill.test.intent')
    def handle_skill_test(self, message):
        self.speak_dialog('skill.test')

    @intent_handler(IntentBuilder('HelloTest').require('HappyTest'))
    @adds_context('HappyContext')
    def handle_hello_world_intent(self, message):
        self.log.info("This is an info level log message.")
        self.speak("Our first test should be simple", expect_response=True)

    @intent_handler(IntentBuilder('OkIntent').require('OkayTest'))
    def handle_hello_world_intent(self, message):
        self.log.info("This is an info level log message2.")
        self.speak("Let us start: what is pi?", expect_response=True)


def create_skill():
    return TestSkill()

