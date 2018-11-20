from history import HistoryItem, ACTION_TYPES
import pymongo

__author__ = 'alexa'

global_user = None


def get_db():
    client = pymongo.MongoClient("localhost", 27017)
    return client.ebookbase


# authentication

HistoryItemDB = HistoryItem
ACTION_TYPESDB = ACTION_TYPES


def auth(login, password):
    db = get_db()
    user = db.users.find_one({"login": login, "password": password})
    if user is not None:
        global global_user
        global_user = user
        return True
    else:
        return False


def de_auth():
    global global_user
    global_user = None


def create_user(login, password):
    db = get_db()
    user = db.users.find_one({"login": login})
    if user is not None:
        return False
    db.users.insert({"login": login, "password": password})
    return True


def is_auth():
    return global_user is not None


def get_user():
    return global_user


def get_users():
    db = get_db()
    return db.users.find()


#history
def save_history_item(history_item):
    db = get_db()
    return db.history.insert({
        "login": history_item.login,
        "action_type": history_item.action_type,
        "id": history_item.id,
        "data": history_item.data,
        "time": history_item.time
    })


def get_history_for_user(login):
    db = get_db()
    return [(
                HistoryItem(
                    ACTION_TYPES.reverse_mapping[x["action_type"]],
                    x["id"],
                    x["data"],
                    x["login"],
                    x["time"]
                )
            ) for x in db.history.find({"login": login})]