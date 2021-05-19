from mycroft import MycroftSkill, intent_file_handler


class TestSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skill.test.intent')
    def handle_skill_test(self, message):
        self.speak_dialog('skill.test')


def create_skill():
    return TestSkill()

