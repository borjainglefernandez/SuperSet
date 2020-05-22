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

workoutsplit_tracker = 1


class GainsApp(App):
    # Global Variable to track the amount of workout splits created

    def build(self):
        return GUI

    def change_screen(self, screen_name, direction):
        screen_manager = self.root.ids["screen_manager"]
        if direction == "next":
            screen_manager.transition.direction = "left"
        elif direction == "previous":
            screen_manager.transition.direction = "right"
        screen_manager.current = screen_name

    def add_screen(self, name):
        screen_manager = self.root.ids["screen_manager"]
        workoutsplit_tracker_string = str(workoutsplit_tracker)
        actual_name = name + workoutsplit_tracker_string
        print(actual_name)
        screen = Screen(name=actual_name)
        screen_manager.add_widget(screen)

    def get_next_workout(self):
        return "workout" + str(workoutsplit_tracker)


if __name__ == '__main__':
    GainsApp().run()