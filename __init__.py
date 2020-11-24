from mycroft import MycroftSkill, intent_file_handler


class Youtubeplayer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('youtubeplayer.intent')
    def handle_youtubeplayer(self, message):
        self.speak_dialog('youtubeplayer')


def create_skill():
    return Youtubeplayer()

