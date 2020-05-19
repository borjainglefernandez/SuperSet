import kivy
kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

class HomeScreen(Screen):
    pass
class AddWorkoutScreen(Screen):
    pass

class ExistingSplitsScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

GUI = Builder.load_file("main.kv")

class GainsApp(App):

    def build(self):
        return GUI

    def change_screen(self, screen_name, direction):
        screen_manager = self.root.ids["screen_manager"]
        if direction == "next":
            screen_manager.transition.direction = "left"
        elif direction == "previous":
            screen_manager.transition.direction = "right"
        screen_manager.current = screen_name


if __name__ == '__main__':
    GainsApp().run()