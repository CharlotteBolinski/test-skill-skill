from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.skills.context import adds_context, removes_context

class TestSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('skill.test.intent')
    def handle_skill_test(self, message):
        self.speak_dialog('skill.test')

    @intent_handler(IntentBuilder('StartTest').require('StartTest'))
    @adds_context('StartContext')
    def handle_hello_test_intent(self, message):
        self.starttest = False
        self.log.info("This is an info level log message.")
        self.speak("Our first test should be simple", expect_response=True)

    @intent_handler(IntentBuilder('OkayStartTest').require('OkayTest').require('StartContext').build())
    @removes_context('StartContext')
    @adds_context('TestContext')
    def handle_okay_test_intent(self, message):
        self.starttest = True
        self.speak("What are the 20 first digits of pi?", expect_response=True)

    @intent_handler(IntentBuilder("GoOnTest").require("OneAnswer").require("TestContext").build())
    @removes_context('TestContext')
    def handle_one_test_intent(self, message):
        if self.starttest:
            self.speak("That is the wrong answer")
        else:
            self.speak("That might be right")

def create_skill():
    return TestSkill()

