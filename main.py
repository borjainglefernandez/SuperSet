import kivy
kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import  ScrollView


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

    # split names used for exercises
    splitname1 = TextInput(id="splitname1")
    splitname2 = TextInput(id="splitname2")
    splitname3 = TextInput(id="splitname3")
    splitname4 = TextInput(id="splitname4")
    splitname5 = TextInput(id="splitname5")
    splitname6 = TextInput(id="splitname6")
    splitname7 = TextInput(id="splitname7")

    # split name: workout day dict
    split_day = {}

    # split name: exercises dict
    split_exercises = {}

    #grid layout for asking split days
    split_grid = None

    #grid layout for asking exercises for each day
    exercises_grid = None

    #scroll view for exercises_grid
    exercises_scroll = None

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
                #prevents the button from being pressed twice
                self.add_split_pressed = True
                addworkout_screen = self.root.ids["add_workout_screen"]
                self.split_grid = GridLayout(cols_minimum = {0: 50, 1: 500},cols = 2, rows = days, size_hint_x = 0.9, size_hint_y = 0.25, pos_hint = {"top": 0.55, "right": 0.95})
                #idk how else to do this, nik please help
                for x in range(days):
                    self.weekdays += 1
                    if x == 0:
                        self.split_grid.add_widget(self.workoutday0)
                    if x == 1:
                        self.split_grid.add_widget(self.workoutday1)
                    if x == 2:
                        self.split_grid.add_widget(self.workoutday2)
                    if x == 3:
                        self.split_grid.add_widget(self.workoutday3)
                    if x == 4:
                        self.split_grid.add_widget(self.workoutday4)
                    if x == 5:
                        self.split_grid.add_widget(self.workoutday5)
                    if x == 6:
                        self.split_grid.add_widget(self.workoutday6)
                    self.split_grid.add_widget(self.get_days_of_the_week())
                addworkout_screen.add_widget(self.split_grid)

        except:
            #dont do anything if the string is not a number
            pass

    def create_label(self,text):
        return Label(text = text)

    def ask_exercises(self, days_of_week):
        try:
            days = int(days_of_week)
            #the days of the week have to be between 1 and 7
            addworkout_screen = self.root.ids["add_workout_screen"]
            if days >= 1 and days <= 7:
                # prevents the button from being pressed twice
                self.exercises_grid = GridLayout(cols_minimum={0: 50, 1: 500}, cols=2, rows=days, size_hint_x=0.9, size_hint_y=0.25,
                            )
                count = 0
                for splitname in self.split_day.keys():
                    self.exercises_grid.add_widget(self.create_label(splitname))
                    if count == 0:
                        self.exercises_grid.add_widget(self.splitname1)
                    if count == 1:
                        self.exercises_grid.add_widget(self.splitname2)
                    if count == 2:
                        self.exercises_grid.add_widget(self.splitname3)
                    if count == 3:
                        self.exercises_grid.add_widget(self.splitname4)
                    if count == 4:
                        self.exercises_grid.add_widget(self.splitname5)
                    if count == 5:
                        self.exercises_grid.add_widget(self.splitname6)
                    if count == 6:
                        self.exercises_grid.add_widget(self.splitname7)
                    count += 1
                self.exercises_scroll = ScrollView(pos_hint={"top": 0.25, "right": 1}, do_scroll_y = True)
                self.exercises_scroll.add_widget(self.exercises_grid)
                addworkout_screen.add_widget(self.exercises_scroll)



        except:
            #dont do anything if the string is not a number
            pass

    def clear_addworkout_screen(self):
        addworkout_screen = self.root.ids["add_workout_screen"]
        if self.split_grid is not None:
            self.split_grid.clear_widgets()
            addworkout_screen.remove_widget(self.split_grid)

        if self.exercises_scroll is not None:
            self.exercises_grid.clear_widgets()
            addworkout_screen.remove_widget(self.exercises_scroll)

        self.split_day = {}

        self.split_exercises = {}

        self.workoutday0.text = ""
        self.workoutday1.text = ""
        self.workoutday2.text = ""
        self.workoutday3.text = ""
        self.workoutday4.text = ""
        self.workoutday5.text = ""
        self.workoutday6.text = ""


        self.splitname1.text = ""
        self.splitname2.text = ""
        self.splitname3.text = ""
        self.splitname4.text = ""
        self.splitname5.text = ""
        self.splitname6.text = ""
        self.splitname7.text = ""

        self.weekdays = 0

        self.add_split_pressed = False

    def submit_exercises(self):
        if self.splitname1.text != "":
            self.split_exercises[self.workoutday0.text] = self.splitname1.text
        if self.splitname2.text != "":
            self.split_exercises[self.workoutday1.text] = self.splitname2.text
        if self.splitname3.text != "":
            self.split_exercises[self.workoutday2.text] = self.splitname3.text
        if self.splitname4.text != "":
            self.split_exercises[self.workoutday3.text] = self.splitname4.text
        if self.splitname5.text != "":
            self.split_exercises[self.workoutday4.text] = self.splitname5.text
        if self.splitname6.text != "":
            self.split_exercises[self.workoutday5.text] = self.splitname6.text
        if self.splitname7.text != "":
            self.split_exercises[self.workoutday6.text] = self.splitname7.text
        print(self.split_exercises)

if __name__ == '__main__':
    GainsApp().run()