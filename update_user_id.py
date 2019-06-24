from get_user import get_all_users
from get_user import get_user_id
from update_user import update_user

print("Twitter User ID updater")
listOfUsers = get_all_users()

for user_name in listOfUsers:
    user_name = user_name[0]
    user_id = get_user_id(user_name)
    update_user(user_name, user_id)
    index = index + 1
