import time
import database

__author__ = 'alexa'


class HistoryItem:
    def __init__(self, _action_type, _id, _data, login, _time=None):
        self.action_type = _action_type
        self.id = _id
        self.data = _data
        if _time is not None:
            self.time = _time
        else:
            self.time = time.strftime("%H:%M:%S") + " " + time.strftime("%d/%m/%Y")
        self.login = login

    def save(self):
        return database.save_history_item(self)

    def __str__(self):
        return "ActionType: " + self.action_type + \
               "; ID: " + self.id + \
               "; Data: " + self.data + \
               "; Time: " + self.time + \
               "; Login: " + self.login


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)


ACTION_TYPES = enum('SECTION', 'TEST', 'BOOK')


