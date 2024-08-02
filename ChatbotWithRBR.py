import random
import re
import datetime
import requests

class ChatBot:

    nr = ("no" , "na" , "nope" , "not" , "nah")
    ec = ("pause" , "stop" , "quit" , "later" , "goodbye" , "exit" , "bye")
    current_date = datetime.date.today()
    current_time = datetime.datetime.now().time()

    def __init__(self):
        self.support_responses = {
            'ask_about_weather': r'.*\s*weather.*',
            'ask_about_date': r'.*\s*date.*',
            'ask_about_time': r'.*\s*time.*'
        }
        self.api_key = '30d4741c779ba94c470ca1f63045390a'

    def greet(self):
        print("Hello! Welcome to the ChatBot... \n")
        self.name = input("BOT: What is your name?\nHUMAN: ")
        will_help = input(f"BOT: Hi {self.name}, Will you like to chat with me?\nHUMAN: ")
        if will_help in self.nr:
            print("BOT: Alright, Have a nice day!")
            return
        self.chat()

    def make_exit(self,reply):
        for command in self.ec:
            if command in reply:
                print("BOT: Thanks for reaching out, have a great day!")
                return True
        return False

    def chat(self):
        reply = input("BOT: Please tell me your query: \nHUMAN: ").lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self,reply):
        for intent , regex_pattern in self.support_responses.items():
            found_match = re.search(regex_pattern, reply)
            if found_match and intent == 'ask_about_date':
                return self.ask_about_date()
            elif found_match and intent == 'ask_about_time':
                return self.ask_about_time()
            elif found_match and intent == 'ask_about_weather':
                return self.ask_about_weather()
        return self.no_match_intent()

    def ask_about_date(self):
        return f"BOT: Today's Date: {self.current_date} \nHUMAN: "

    def ask_about_time(self):
        return f"BOT: Now the Time is: {self.current_time} \nHUMAN: "

    def ask_about_weather(self):
        user_input = input("BOT: Please enter a city name for weather information:\nHUMAN: ")
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={self.api_key}")
        if weather_data.json()['cod'] == '404':
            return f"BOT: No city found for '{user_input}'.\nHUMAN: "
        else:
            weather = weather_data.json()['weather'][0]['main']
            temph = round(weather_data.json()['main']['temp'])
            tempc = round((temph - 32) * (5/9))
            return f"BOT: The weather in {user_input} is: {weather}\n" \
                   f"The temperature in {user_input} is: {temph}ºF / {tempc}ºC \nHUMAN: "

    def no_match_intent(self):
        responses = ("BOT: Sorry I couldn't understand your prompt. \nHUMAN: ",
                     "BOT: ERROR. \nHUMAN: ")
        return random.choice(responses)

bot = ChatBot()
bot.greet() 