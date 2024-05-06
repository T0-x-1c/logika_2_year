from kivy.lang import Builder
from kivymd.app import MDApp as App
from kivymd.uix.button import MDRectangleFlatButton as Button
from kivymd.uix.label import MDLabel as Label
from kivymd.uix.boxlayout import MDBoxLayout as BoxLayout
from kivymd.uix.textfield import MDTextField as TextInput
from kivymd.uix.screenmanager import MDScreenManager as ScreenManager
from kivymd.uix.screen import MDScreen as Screen


global usd_rate
usd_rate = 39

def convert(sum, UAtoUSorUStoUA):
    if UAtoUSorUStoUA == "1":
        return float(sum) / float(usd_rate)
    elif UAtoUSorUStoUA == "2":
        return float(sum) * float(usd_rate)

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)  # ім'я екрана має передаватися конструктору класу Screen
        label1 = Label(text = "Конвертор")
        btn1 = Button(text="UAH to USD")
        btn2 = Button(text="USD to UAH")
        btn3 = Button(text="Встановити курс")
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(label1)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        btn1.on_press = self.next
        btn2.on_press = self.back
        btn3.on_press = self.down
        self.add_widget(layout)  # екран - це віджет, на якому можуть створюватись всі інші (нащадки)

    def next(self):
        self.manager.transition.direction = 'left'  # об'єкт класу Screen має властивість manager
        # - це посилання на батьківський клас
        self.manager.current = 'second'
    def back(self):
        self.manager.transition.direction = 'right'  # об'єкт класу Screen має властивість manager
        # - це посилання на батьківський клас
        self.manager.current = 'third'
    def down(self):
        self.manager.transition.direction = 'up'  # об'єкт класу Screen має властивість manager
        # - це посилання на батьківський клас
        self.manager.current = 'fourth'


class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        layout = BoxLayout(orientation="vertical")
        btn1 = Button(text="Back")
        self.label = Label(text = "результат:")
        self.uah = TextInput(hint_text = 'Введііть суму', multiline = False)

        btn1.on_press = self.next
        self.uah.bind(text=self.update_result)

        layout.add_widget(btn1)
        layout.add_widget(self.uah)
        layout.add_widget(self.label)
        self.add_widget(layout)

    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

    def update_result(self, *args):
        amount = self.uah.text
        if amount.isnumeric():
           amount = int(amount)
           result = round(amount / usd_rate, 2)
           result = (f"{str(result)} usd")
           self.label.text = result
        else:
            self.label.text = "Будь ласка, введіть суму"

class ThirdScr(Screen):
    def __init__(self, name='third'):
        super().__init__(name=name)
        layout = BoxLayout(orientation="vertical")
        btn1 = Button(text="Back")
        self.label = Label(text = "результат:")
        self.uah = TextInput(hint_text = 'Введііть суму', multiline = False)

        btn1.on_press = self.next
        self.uah.bind(text=self.update_result)

        layout.add_widget(btn1)
        layout.add_widget(self.uah)
        layout.add_widget(self.label)
        self.add_widget(layout)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'first'

    def update_result(self, *args):
        amount = self.uah.text
        if amount.isnumeric():
           amount = int(amount)
           result = round(amount * usd_rate, 2)
           result = (f"{str(result)} грн")
           self.label.text = result
        else:
            self.label.text = "Будь ласка, введіть суму"

class FourthScr(Screen):
    def __init__(self, name='fourth'):
        super().__init__(name=name)

        layout = BoxLayout(orientation="vertical")

        btn1 = Button(text="Back")
        btn2 = Button(text="Commit")
        self.except_label = Label(text = '')

        self.usd_rate_txt = TextInput(hint_text="Введіть курс")

        btn1.on_press = self.next
        btn2.on_press = self.commit_usd_rate

        layout.add_widget(btn1)
        layout.add_widget(self.usd_rate_txt)
        layout.add_widget(btn2)
        layout.add_widget(self.except_label)
        self.add_widget(layout)


    def next(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'first'
    def commit_usd_rate(self):
        global usd_rate
        try:
            usd_rate = float(self.usd_rate_txt.text)
            self.except_label.text = ""
        except:
            self.except_label.text = "Введіть курс через крапку"



class ConverterApp(App):
    def build(self):
        Builder.load_file('style.kv')

        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThirdScr())
        sm.add_widget(FourthScr())
        # буде показано FirstScr, тому що він доданий першим. Це можна змінити ось так:
        # sm.current = 'second'
        return sm


app = ConverterApp()
app.run()