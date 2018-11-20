import database

for a in database.get_history_for_user(database.get_user()["login"]):
    print a