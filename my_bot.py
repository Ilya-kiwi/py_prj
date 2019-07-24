import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, text):
    vk.method('messages.send', {'user_id': user_id, 'text': text})


# API key is token
token = "44281af8a4b618939ba44d68276a72a077ebe4085a9dba4b1cdf9f65370675e955869e540cfb71fbd1877"

vk = vk_api.VkApi(token=token)  # Auth like Vkgroup
longpoll = VkLongPoll(vk)  # Work with messages
"""
for action in longpoll.listen():
    if action.type == VkEventType.MESSAGE_NEW and action.to_me:
        request = action.text
        if request == 'hello':
            write_msg(action.user_id, "HI!")
        elif request == "bye":
            write_msg(action.user_id, "GoodBye")
        else:
            write_msg(action.user_id, "I don't understand")
"""

class VkBot:
    def __init__(self, user_id):
        print("create object Bot")
        self._USER_ID = user_id
        self._USER_NAME = self.get_name(user_id)

        self._COMMANDS = ["hello", "weather", "time", "bye"]
