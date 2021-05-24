from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.skills.context import adds_context, removes_context

class TestSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('skill.test.intent')
    def handle_skill_test(self, message):
        self.speak_dialog('skill.test', expect_response=True)

    @intent_handler(IntentBuilder('StartTest').require('StartTest'))
    @adds_context('StartContext')
    def handle_hello_test_intent(self, message):
        self.starttest = False
        self.log.info("Start test was successful.")
        self.speak_dialog('welcome')
        self.speak_dialog('information')
        self.speak("Our first test should be simple. What do you know about social Media?", expect_response=True)

    @intent_handler(IntentBuilder('ContinueTest').require('KnowNothing').build())
    @removes_context('StartContext')
    @adds_context('FirstContext')
    def handle_one_test_intent(self, message):
        self.starttest = True
        self.log.info("self.starttest is true")
        self.speak("Okay that is interesting.")
        if self.starttest:
            self.speak("Sounds great. Let us continue.", expect_response=True)
        else:
            self.speak("But the wrong answer, you are not hired.", expect_response=True)

    @intent_handler(IntentBuilder('OkayStartTest').require('OkayTest').build())
    @removes_context('SecondContext')
    @adds_context('ThirdContext')
    def handle_okay_test_intent(self, message):
        self.speak_dialog('gapText')
        self.speak("What do you know about social Media?", expect_response=True)

    @intent_handler(IntentBuilder('AnswerGap').require('Elephant').build())
    @removes_context('ThirdContext')
    @adds_context('FinalContext')
    def handle_okay_test_intent2(self, message):
        self.speak("What do you know about social Media?")


def create_skill():
    return TestSkill()

