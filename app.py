# app.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from threading import Thread
import asyncio
import bot  # Импортируем файл bot.py

# Экран со списком ботов
class BotListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        
        # Кнопка добавления нового бота
        self.add_bot_button = Button(text="Добавить бота", size_hint=(1, 0.1))
        self.add_bot_button.bind(on_press=self.add_bot)
        
        # Добавляем виджеты
        self.layout.add_widget(self.add_bot_button)
        self.add_widget(self.layout)

    def add_bot(self, instance):
        # Создаем новую кнопку для бота
        bot_button = Button(text="Новый бот", size_hint=(1, 0.1))
        bot_button.bind(on_press=self.open_bot_settings)
        self.layout.add_widget(bot_button)

    def open_bot_settings(self, instance):
        # Переход на экран настроек
        self.manager.current = 'bot_settings'


# Экран настройки бота с кнопкой запуска
class BotSettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        
        # Поле для ввода токена
        self.token_input = TextInput(hint_text="Введите токен бота", multiline=False)
        self.layout.add_widget(self.token_input)
        
        # Кнопка запуска бота
        self.start_button = Button(text="Запустить бота", size_hint=(1, 0.1))
        self.start_button.bind(on_press=self.start_bot)
        self.layout.add_widget(self.start_button)
        
        # Добавляем виджет на экран
        self.add_widget(self.layout)

    def start_bot(self, instance):
        # Получаем токен и запускаем бота в отдельном потоке
        token = self.token_input.text
        if token:
            # Запуск бота в новом потоке с токеном пользователя
            bot_thread = Thread(target=lambda: asyncio.run(bot.start_bot(token)))
            bot_thread.start()
            print(f"Бот с токеном {token} запущен")


# Главный класс приложения
class TelegramBotApp(App):
    def build(self):
        # Инициализация менеджера экранов
        sm = ScreenManager()
        
        # Добавляем экраны
        sm.add_widget(BotListScreen(name='bot_list'))
        sm.add_widget(BotSettingsScreen(name='bot_settings'))
        
        return sm


if __name__ == '__main__':
    TelegramBotApp().run()
