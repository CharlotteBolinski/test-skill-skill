from mycroft import MycroftSkill, intent_file_handler

class TestSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.flavors = ['vanilla', 'chocolate', 'mint']

    @intent_file_handler('skill.test.intent')
    def handle_skill_test(self, message):
        self.speak_dialog('skill.test')

    @intent_file_handler('set.test.intent')
    def handle_skill_test(self, message):
        self.speak_dialog('set.test')

    @intent_handler('request.icecream.intent')
    def handle_request_icecream(self):
        self.speak_dialog('welcome')


def create_skill():
    return TestSkill()

