import kivy
kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput


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
    # Global Variable to track the amount of workout splits created
    workoutsplit_tracker = 1
    # ensure that the ask_split, button is not pressed more than once
    add_split_pressed = False
    # used to group toggle buttons correctly
    weekdays = 0

    # split names
    workoutday0 = TextInput(id="workoutday1")
    workoutday1 = TextInput(id="workoutday2")
    workoutday2 = TextInput(id="workoutday3")
    workoutday3 = TextInput(id="workoutday4")
    workoutday4 = TextInput(id="workoutday5")
    workoutday5 = TextInput(id="workoutday6")
    workoutday6 = TextInput(id="workoutday7")

    # split name: workout day dict
    split_day = {}

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
        workoutsplit_tracker_string = str(self.workoutsplit_tracker)
        actual_name = name + workoutsplit_tracker_string
        print(actual_name)
        screen = Screen(name=actual_name)
        screen_manager.add_widget(screen)

    def get_next_workout(self):
        return "workout" + str(self.workoutsplit_tracker)

    def get_next_group(self):
        return "weekdays" + str(self.weekdays)

    def create_split_dict(self,instance):
        if instance.group == "weekdays1":
            self.split_day[self.workoutday0.text] = instance.text
        if instance.group == "weekdays2":
            self.split_day [self.workoutday1.text] = instance.text
        if instance.group == "weekdays3":
            self.split_day [self.workoutday2.text] = instance.text
        if instance.group == "weekdays4":
            self.split_day [self.workoutday3.text] = instance.text
        if instance.group == "weekdays5":
            self.split_day [self.workoutday4.text] = instance.text
        if instance.group == "weekdays6":
            self.split_day [self.workoutday5.text] = instance.text
        if instance.group == "weekdays7":
            self.split_day [self.workoutday6.text] = instance.text
        print(self.split_day)

    def get_days_of_the_week(self):
        week = GridLayout(cols = 7, size_hint_x = 0.5, size_hint_y = 0.1)
        sunday = ToggleButton(text = "Sun", font_size = "10sp", group = self.get_next_group())
        sunday.bind(on_press = self.create_split_dict)
        monday = ToggleButton(text = "Mon", font_size = "10sp", group = self.get_next_group())
        monday.bind(on_press = self.create_split_dict)
        tuesday = ToggleButton(text = "Tues", font_size = "10sp", group = self.get_next_group())
        tuesday.bind(on_press = self.create_split_dict)
        wednesday = ToggleButton(text = "Wed", font_size = "10sp", group = self.get_next_group())
        wednesday.bind(on_press = self.create_split_dict)
        thursday = ToggleButton(text = "Thur", font_size = "10sp", group = self.get_next_group())
        thursday.bind(on_press = self.create_split_dict)
        friday = ToggleButton(text = "Fri", font_size = "10sp", group = self.get_next_group())
        friday.bind(on_press = self.create_split_dict)
        saturday = ToggleButton(text = "Sat", font_size = "10sp", group = self.get_next_group())
        saturday.bind(on_press = self.create_split_dict)
        week.add_widget(sunday)
        week.add_widget(monday)
        week.add_widget(tuesday)
        week.add_widget(wednesday)
        week.add_widget(thursday)
        week.add_widget(friday)
        week.add_widget(saturday)
        return week

    def ask_split(self,days_of_week):
        try:
            days = int(days_of_week)
            #the days of the week have to be between 1 and 7
            if days >= 1 and days <= 7 and self.add_split_pressed == False:
                self.add_split_pressed = True
                grid = GridLayout(cols_minimum = {0: 50, 1: 500},cols = 2, rows = days, size_hint_x = 0.9, size_hint_y = 0.3, pos_hint = {"top": 0.55, "right": 0.95})
                addworkout_screen = self.root.ids["add_workout_screen"]
                #idk how else to do this, nik please help
                for x in range(days):
                    self.weekdays += 1
                    if x == 0:
                        grid.add_widget(self.workoutday0)
                    if x == 1:
                        grid.add_widget(self.workoutday1)
                    if x == 2:
                        grid.add_widget(self.workoutday2)
                    if x == 3:
                        grid.add_widget(self.workoutday3)
                    if x == 4:
                        grid.add_widget(self.workoutday4)
                    if x == 5:
                        grid.add_widget(self.workoutday5)
                    if x == 6:
                        grid.add_widget(self.workoutday6)
                    grid.add_widget(self.get_days_of_the_week())
                addworkout_screen.add_widget(grid)


        except:
            #dont do anything if the string is not a number
            pass




if __name__ == '__main__':
    GainsApp().run()