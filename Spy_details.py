import datetime


class Person:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:
    def __init__(self, message, sent_to, sent_by_me):
        self.message = message
        self.time = datetime.datetime.now()
        self.sent_to = sent_to
        self.sent_by_me = sent_by_me
        self.sent_to = ""



spy = Person("X", "Ms", 30, 5.0)
f1 = Person("", "", 0, 0.0)
msg = ChatMessage("", "", "")