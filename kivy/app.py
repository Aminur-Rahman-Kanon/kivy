from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from database.db import DB_INIT

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        #add widgets to window
        self.window.cols = 1
        self.window.add_widget(Image(source="logo.png"))
        self.db_obj = DB_INIT()
        self.db = self.db_obj.init_connection()
        self.time = self.db_obj.show_records()[0]

        # print(self.time)

        for time in self.time:
            # print(time)
            self.prayer_time = Label(text = time)
            self.window.add_widget(self.prayer_time)



        return self.window

if __name__ == "__main__":
    SayHello().run()
    db = DB_INIT()
    db.init_connection()
    db.show_records()