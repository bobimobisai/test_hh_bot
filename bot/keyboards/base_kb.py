from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Menu:
    def __init__(self, lang, size):
        self.lang = lang
        self.menu = InlineKeyboardBuilder()
        self.size = size

    def add_button(self, text, callback_data):
        self.menu.add(
            types.InlineKeyboardButton(text=text, callback_data=callback_data)
        )

    def add_url_button(self, text, url):
        self.menu.add(types.InlineKeyboardButton(text=text, url=url))

    def get_size(self):
        self.menu.adjust(self.size)

    def as_markup(self):
        return self.menu.as_markup()


class RussianUserNewMenu(Menu):
    def __init__(self, size):
        super().__init__("ru", size=size)
        self.add_button(text="GPT чат (base)🦾", callback_data="go_gpt_chat")
        self.add_button(text="GPT user data👨‍💻", callback_data="user_data")
        self.add_button(text="GPT snowboard 🏂", callback_data="gtp_snowboard")
        self.add_button(text="User data✅", callback_data="collection")
        self.get_size()

class Back(Menu):
    def __init__(self, size):
        super().__init__("en", size=size)
        self.add_button(text="⛔️ Stop ", callback_data="stop")
        self.get_size()

def go_back(size=1):
        return Back(size=size).as_markup()

def menu(lang: str = "ru", size: int = 2):
    if lang == "ru":
        menu_instance = RussianUserNewMenu(size=size)
    return menu_instance.as_markup()