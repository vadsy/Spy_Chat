import datetime


class Person:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self. salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.datetime.now()
        self.sent_by_me = sent_by_me



spy = Person("X", "Ms", 21, 4.7)
f1 = Person("", "", 0, 0.0)
msg = ChatMessage("", "")