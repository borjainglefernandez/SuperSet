import kivy
import datetime
kivy.require('1.11.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# These are all the current screens in the app
# If you need to add more screens add them here

class HomeScreen(Screen):
    pass

class AddWorkoutScreen(Screen):
    pass

class ExistingSplitsScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class WorkoutScreen1(Screen):
    pass

class WorkoutScreen2(Screen):
    pass

class WorkoutScreen3(Screen):
    pass

class WorkoutScreen4(Screen):
    pass

class StatScreen1(Screen):
    pass

class StatScreen2(Screen):
    pass

class StatScreen3(Screen):
    pass

class StatScreen4(Screen):
    pass

class WindowManager(ScreenManager):
    pass


#Uses main.kv as the main file
GUI = Builder.load_file("main.kv")

#The actual app
class GainsApp(App):

    # Global Variable to track the amount of workout splits created
    workoutsplit_tracker = 1

    # Ensure that the ask_split, button is not pressed more than once
    add_split_pressed = False

    # Used to group toggle buttons correctly
    weekdays = 0

    # Used to track the name of each splitday
    workoutday0 = TextInput(id="workoutday1")
    workoutday1 = TextInput(id="workoutday2")
    workoutday2 = TextInput(id="workoutday3")
    workoutday3 = TextInput(id="workoutday4")
    workoutday4 = TextInput(id="workoutday5")
    workoutday5 = TextInput(id="workoutday6")
    workoutday6 = TextInput(id="workoutday7")

    # Used to track the name of each exercises within a splitday
    splitname1 = TextInput(id="splitname1")
    splitname2 = TextInput(id="splitname2")
    splitname3 = TextInput(id="splitname3")
    splitname4 = TextInput(id="splitname4")
    splitname5 = TextInput(id="splitname5")
    splitname6 = TextInput(id="splitname6")
    splitname7 = TextInput(id="splitname7")

    # Split name: day of the week dict for split 1
    split_day_1 = {}

    # Split name: exercises dict for split 1
    split_exercises_1 = {}

    # Split name: day of the week dict for split 2
    split_day_2 = {}
    
    # Split name: exercises dict for split 2
    split_exercises_2 = {}

    # Split name: day of the week dict for split 3
    split_day_3 = {}

    # Split name: exercises dict for split 3
    split_exercises_3 = {}

    # Split name: day of the week dict for split 4
    split_day_4 = {}

    # Split name: exercises dict for split 4
    split_exercises_4 = {}

    # Grid layout for asking split days
    split_grid = None

    # Grid layout for asking exercises for each day
    exercises_grid = None

    # Scroll view for exercises_grid
    exercises_scroll = None

    # Grid layout for spreadsheet
    spreadsheet_grid = None

    # Scroll view for spreatsheet_grid
    spreadsheet_scroll = None

    # Name of the current workout screen
    # (up to 4, keeps track of which one is being used)
    actual_name = "workout_screen_1"

    # Keeps track of how many workout screens have been created
    # so that the next spreadsheet to be created has the correct name
    # In other words, keeps track of which spreadsheets have been created
    temp_actual_name = "workout_screen_0"

    # Used to track the column number of each box in the spreadsheet
    # Used to id each textinput
    col_count = 0

    # Used to track the row number of each box in the spreadsheet
    # Used to id each textinput
    row_count = 0

    # Dict for holding the row number, split day, and data of each exercise for workout_screen_1
    workout_screen_1_data = {}

    # Dict for holding the row number, split day, and data of each exercise for workout_screen_2
    workout_screen_2_data = {}

    # Dict for holding the row number, split day, and data of each exercise for workout_screen_3
    workout_screen_3_data = {}

    # Dict for holding the row number, split day, and data of each exercise for workout_screen_4
    workout_screen_4_data = {}

    # Row number: Exercise name in spreadsheet 1
    row_dict_1 = {}

    # Row number: Exercise name in spreadsheet 2
    row_dict_2 = {}

    # Row number: Exercise name in spreadsheet 3
    row_dict_3 = {}

    # Row number: Exercise name in spreadsheet 4
    row_dict_4 = {}

    # Split day: list of date text boxes in spreadsheet 1
    date_dict_1 = {}

    # Split day: list of date text boxes in spreadsheet 2
    date_dict_2 = {}

    # Split day: list of date text boxes in spreadsheet 3
    date_dict_3 = {}

    # Split day: list of date text boxes in spreadsheet 4
    date_dict_4 = {}

    # List to iterate through each text box in spreadsheet 1
    text_boxes_list_screen_1 = []

    # List to iterate through each text box in spreadsheet 2
    text_boxes_list_screen_2 = []

    # List to iterate through each text box in spreadsheet 3
    text_boxes_list_screen_3 = []

    # List to iterate through each text box in spreadsheet 4
    text_boxes_list_screen_4 = []

    # Label List for stat screen 1
    #
    # Used to delete the labels so that they are updated
    stat_screen_1_labels = []

    # Label List for stat screen 2
    #
    # Used to delete the labels so that they are updated
    stat_screen_2_labels = []

    # Label List for stat screen 3
    #
    # Used to delete the labels so that they are updated
    stat_screen_3_labels = []

    # Label List for stat screen 4
    #
    # Used to delete the labels so that they are updated
    stat_screen_4_labels = []

    # ScrollView for stat screen 1
    stat_scroll_1 = ScrollView(size_hint=(1, None), size=(Window.width, Window.height),
                                         do_scroll_x=True, do_scroll_y=True, pos_hint={"top": 0.78})
    # ScrollView for stat screen 2
    stat_scroll_2 = ScrollView(size_hint=(1, None), size=(Window.width, Window.height),
                                         do_scroll_x=True, do_scroll_y=True, pos_hint={"top": 0.78})

    # ScrollView for stat screen 3
    stat_scroll_3 = ScrollView(size_hint=(1, None), size=(Window.width, Window.height),
                                         do_scroll_x=True, do_scroll_y=True, pos_hint={"top": 0.78})

    # ScrollView for stat screen 4
    stat_scroll_4 = ScrollView(size_hint=(1, None), size=(Window.width, Window.height),
                                         do_scroll_x=True, do_scroll_y=True, pos_hint={"top": 0.78})

    # Not exactly sure what this does LOL don't worry about it
    def build(self):
        return GUI

    # Changes the current screen
    #
    # @param string screen_name (the name of the screen to switch to)
    # @param string direction (either "next" or "previous" which determines the direction of the transition)
    def change_screen(self, screen_name, direction):

        # If any of the spreadsheets are not created yet,
        # switching to that screen or its stat screen is prohibited
        if (screen_name == "workout_screen_1" or screen_name == "stat_screen_1") and not(self.temp_actual_name == "workout_screen_1"
        or self.temp_actual_name == "workout_screen_2" or self.temp_actual_name == "workout_screen_3" or self.temp_actual_name == "workout_screen_4"):
            print("screen 1 not working")

        elif (screen_name == "workout_screen_2" or screen_name == "stat_screen_2") and not(self.temp_actual_name == "workout_screen_2" or self.temp_actual_name == "workout_screen_3" or self.temp_actual_name == "workout_screen_4"):
            print("screen 2 not working")

        elif (screen_name == "workout_screen_3" or screen_name == "stat_screen_3") and not(self.temp_actual_name == "workout_screen_3" or self.temp_actual_name == "workout_screen_4"):
            print("screen 3 not working")

        elif (screen_name == "workout_screen_4" or screen_name == "stat_screen_4") and not(self.temp_actual_name == "workout_screen_4"):
            print("screen 4 not working")

        else:
            # Screen_manager manages which screen is the current one
            screen_manager = self.root.ids["screen_manager"]
            if direction == "next":
                screen_manager.transition.direction = "left"
            elif direction == "previous":
                screen_manager.transition.direction = "right"
            screen_manager.current = screen_name

    # Adds a spreadsheet to the screen manager
    #
    # @param string name the name of the screen to be added
    def add_screen(self, name):
        screen_manager = self.root.ids["screen_manager"]
        workoutsplit_tracker_string = str(self.workoutsplit_tracker)
        self.actual_name = name + workoutsplit_tracker_string
        screen = Screen(name=self.actual_name)
        screen_manager.add_widget(screen)
        screen_manager.current = self.actual_name
        self.workoutsplit_tracker += 1

    # Creates a new spreadsheet
    def create_spreadsheet(self):
        data_creator = {}
        row_dict = {}

        # Reset for the next spreadsheet
        self.col_count = 0
        self.row_count = 0

        # Sets each of the necessary information of each spreadsheet
        # to a neutral variable

        if self.actual_name == "workout_screen_1":
            data_creator = self.workout_screen_1_data
            row_dict = self.row_dict_1
            split_day = self.split_day_1
            split_exercises = self.split_exercises_1
            text_boxes_list_screen = self.text_boxes_list_screen_1
            date_dict = self.date_dict_1
            self.add_stats("stat_screen_1", self.workout_screen_1_data, self.split_exercises_1, self.stat_scroll_1)

        elif self.actual_name == "workout_screen_2":
            data_creator = self.workout_screen_2_data
            row_dict = self.row_dict_2
            split_day = self.split_day_2
            split_exercises = self.split_exercises_2
            text_boxes_list_screen = self.text_boxes_list_screen_2
            date_dict = self.date_dict_2
            self.add_stats("stat_screen_2", self.workout_screen_2_data, self.split_exercises_2, self.stat_scroll_2)

        elif self.actual_name == "workout_screen_3":
            data_creator = self.workout_screen_3_data
            row_dict = self.row_dict_3
            split_day = self.split_day_3
            split_exercises = self.split_exercises_3
            text_boxes_list_screen = self.text_boxes_list_screen_3
            date_dict = self.date_dict_3
            self.add_stats("stat_screen_3", self.workout_screen_3_data, self.split_exercises_3, self.stat_scroll_3)

        elif self.actual_name == "workout_screen_4":
            data_creator = self.workout_screen_4_data
            row_dict = self.row_dict_4
            split_day = self.split_day_4
            split_exercises = self.split_exercises_4
            text_boxes_list_screen = self.text_boxes_list_screen_4
            date_dict = self.date_dict_4
            self.add_stats("stat_screen_4", self.workout_screen_4_data, self.split_exercises_4, self.stat_scroll_4)

        else:
            pass

        # Put in a try block because of user error
        # If the user doesn't everything perfectly, this ensures the program doesn't crash
        try:
            # Neutral variable to add all of the widgets to the correct screen
            spreadsheet_screen = self.root.ids[self.actual_name]

            #num_of_rows = len(split_day) + len(split_exercises) <- idk why this is here lol but im keeping it for now

            # Creates the grid layout for the spreadsheet
            self.spreadsheet_grid = GridLayout(rows = 100, cols=30, spacing=10, size_hint_y=None, size_hint_x = None)
            # I can't remember what this does lol dw ab it
            self.spreadsheet_grid.bind(minimum_height=self.spreadsheet_grid.setter('height'))
            self.spreadsheet_grid.bind(minimum_width=self.spreadsheet_grid.setter('width'))

            # Loops through each split day
            for split in split_day.keys():
                # Label for each split day goes first
                # Bolded so that it's differentiated
                split_label = Label(text = str("[size=40]" + '[b]' + split + '[/b]' + "[/size]"), size_hint_y=None, size_hint_x = None, height=200, width = 350, markup = True)
                self.spreadsheet_grid.add_widget(split_label)

                date = datetime.date.today()

                # Used to automatically find the first valid date of each split day
                # Starts at today and keeps adding a day until the correct day of the week is found
                if split_day[split] == "Mon":
                    while date.weekday() != 0:
                        date = date + datetime.timedelta(days=1)
                if split_day[split] == "Tues":
                    while date.weekday() != 1:
                        date = date + datetime.timedelta(days=1)
                if split_day[split] == "Wed":
                    while date.weekday() != 2:
                        date = date + datetime.timedelta(days=1)
                if split_day[split] == "Thur":
                    while date.weekday() != 3:
                        date = date + datetime.timedelta(days=1)
                if split_day[split] == "Fri":
                    while date.weekday() != 4:
                        date = date + datetime.timedelta(days=1)
                if split_day[split] == "Sat":
                    while date.weekday() != 5:
                        date = date + datetime.timedelta(days=1)
                if split_day[split] == "Sun":
                    while date.weekday() != 6:
                        date = date + datetime.timedelta(days=1)

                # If the row count is less than 10, puts a 0 in front of row count in the id in order
                # for all the id's to be the same length
                # These text inputs hold the date for each split day
                if(self.row_count < 10 and self.col_count < 10):
                    # id ex: row01col20
                    text_input = TextInput(text = str(date.month) + "/" + str(date.day), id = "row" + "0" + str(self.row_count) + "col" + "0" + str(self.col_count), size_hint_y=None, size_hint_x = None, height=200, width = 350)
                elif(self.row_count < 10):
                    text_input = TextInput(text = str(date.month) + "/" + str(date.day), id = "row" + "0" + str(self.row_count) + "col" + str(self.col_count), size_hint_y=None, size_hint_x = None, height=200, width = 350)
                elif (self.col_count < 10):
                    text_input = TextInput(text=str(date.month) + "/" + str(date.day),
                                           id="row" + str(self.row_count) + "col" + "0" + str(self.col_count),
                                           size_hint_y=None, size_hint_x=None, height=200, width=350)
                else:
                    text_input = TextInput(text = str(date.month) + "/" + str(date.day), id = "row" + str(self.row_count) + "col" + str(self.col_count), size_hint_y=None, size_hint_x = None, height=200, width = 350)

                # Advance the date a week in the future for the next text input in the same row
                date = date + datetime.timedelta(days=7)

                # Split name: list of dates
                date_dict[split] =[]
                date_dict[split].append(text_input)

                self.col_count += 1
                self.spreadsheet_grid.add_widget(text_input)

                # Adds the rest of the date text inputs (28 to start with)
                for i in range(28):
                    if (self.row_count < 10 and self.col_count < 10):
                        # id ex: row01col20
                        text_input = TextInput(text=str(date.month) + "/" + str(date.day),
                                               id="row" + "0" + str(self.row_count) + "col" + "0" + str(self.col_count),
                                               size_hint_y=None, size_hint_x=None, height=200, width=350)
                    elif (self.row_count < 10):
                        text_input = TextInput(text=str(date.month) + "/" + str(date.day),
                                               id="row" + "0" + str(self.row_count) + "col" + str(self.col_count),
                                               size_hint_y=None, size_hint_x=None, height=200, width=350)
                    elif (self.col_count < 10):
                        text_input = TextInput(text=str(date.month) + "/" + str(date.day),
                                               id="row" + str(self.row_count) + "col" + "0" + str(self.col_count),
                                               size_hint_y=None, size_hint_x=None, height=200, width=350)
                    else:
                        text_input = TextInput(text=str(date.month) + "/" + str(date.day),
                                               id="row" + str(self.row_count) + "col" + str(self.col_count),
                                               size_hint_y=None, size_hint_x=None, height=200, width=350)
                    date_dict[split].append(text_input)
                    date = date + datetime.timedelta(days=7)
                    self.col_count += 1
                    self.spreadsheet_grid.add_widget(text_input)
                self.row_count += 1
                self.col_count = 1

                # Iterates through all the exercises in a particular split day
                for exercise in split_exercises[split]:
                    # Initially each workout screens data dict starts with just Exercise Name: [Split Day Name, row]
                    data_creator[exercise] = [split, str(self.row_count)]
                    # Again, the row dict is Row: Exercise Name
                    row_dict[self.row_count] = exercise
                    # Label for the exercise name
                    exercise_label = Label(text = str(exercise), size_hint_y=None, size_hint_x = None, height=200, width = 350)
                    self.spreadsheet_grid.add_widget(exercise_label)

                    # These text inputs are used for the weights of each exercise each day
                    for i in range(29):
                        if (self.row_count < 10 and self.col_count < 10):
                            # id ex: row01col20
                            text_input = TextInput(id="row" + "0" + str(self.row_count) + "col" + "0" + str(
                                                       self.col_count), size_hint_y=None, size_hint_x=None, height=200,
                                                   width=350)
                        elif (self.row_count < 10):
                            text_input = TextInput(id="row" + "0" + str(self.row_count) + "col" + str(self.col_count),
                                                   size_hint_y=None, size_hint_x=None, height=200, width=350)
                        elif (self.col_count < 10):
                            text_input = TextInput(id="row" + str(self.row_count) + "col" + "0" + str(self.col_count),
                                                   size_hint_y=None, size_hint_x=None, height=200, width=350)
                        else:
                            text_input = TextInput(id="row" + str(self.row_count) + "col" + str(self.col_count),
                                                   size_hint_y=None, size_hint_x=None, height=200, width=350)

                        text_input.bind(text = self.on_text)
                        text_boxes_list_screen.append(text_input)
                        self.col_count += 1
                        self.spreadsheet_grid.add_widget(text_input)
                    self.row_count += 1
                    self.col_count = 1

            self.spreadsheet_scroll = ScrollView(size_hint=(None, None), size=(Window.width, Window.height - 10), do_scroll_x = True, do_scroll_y = True, pos_hint = {"top": 0.85})
            self.spreadsheet_scroll.add_widget(self.spreadsheet_grid)
            spreadsheet_screen.add_widget(self.spreadsheet_scroll)

        except:
            # In case the creation of the spreadsheet doesn't work, this prevents the app from crashing
            pass

    # Calculates the statistics in a given spreadsheet
    #
    # @param dict dict is the data dict for a particular spreadsheet (i.e. workout_screen_1_data)
    # @param dict split_exercises is the particular dict containing each split day's exercises (i.e. split_exercises_1)
    # @param dict date_dict is the part dict containing each splits list of dates
    # @param string stat_screen the name of the stat screen
    def calculate_stats(self, dict, split_exercises, date_dict, stat_screen):
        # Iterates through each split day's list of exercises
        for exercises in split_exercises.values():
            # Iterates through the exercise list's exercises
            for exercise in exercises:
                print(exercise)
                # Holds the list of a particular exercises' data
                #
                # The first two slots are the split day's name to which the exercise belongs to as
                # well as the row number respectively, followed by concurrent average weight of each text input
                #
                # (i.e. Deadlift: ["Back and Biceps", "2", 122.0, 123.5])
                list_of_data = dict[exercise]

                # Average increase
                average_increase_sum = 0

                # Iterates through the weight portion of the list and averages it out
                #
                # (i.e. Deadlift: ["Back and Biceps", "2", 122.0, 123.5], iterates through 122.0 and 123.5)
                for x in range(2, len(list_of_data) - 1):
                    # None used as a sentinel value in case a workout is skipped
                    #
                    # If the values right next to each other are both not none, proceed as normal
                    if list_of_data[x] != None and list_of_data[x + 1] != None:
                        average_increase_sum += (list_of_data[x + 1] - list_of_data[x])

                    # Keep iterating until you find a non none if the first is not met
                    #
                    # If you find a value that's not none but its neighbor is, keep iterating until you find a non none
                    # then do the correct calculations
                    elif list_of_data[x] != None:
                        i = x + 1
                        while list_of_data[i] == None:
                            i += 1
                        average_increase_sum += (list_of_data[i] - list_of_data[x])


                # Average
                sum = 0
                count = 0

                # Max
                max = -999999999
                max_date = "" # Date in which the max was achieved

                # Min
                min = 999999999
                min_date = "" # Date in which the min was achieved

                # Iterates through the weight portion of the list and calculates the average, max, and min
                for i in range(2, len(list_of_data)):
                    # None used as a sentinal value in case a workout is skipped
                    if list_of_data[i] != None:
                        sum += list_of_data[i]
                        count += 1
                        if list_of_data[i] > max:
                            max = list_of_data[i]
                            max_date = date_dict[list_of_data[0]][i - 2].text
                        if list_of_data[i] < min:
                            min = list_of_data[i]
                            min_date = date_dict[list_of_data[0]][i - 2].text

                # If the weight portion of the list isn't big enough to calculate a particular statistic
                # then that piece of data isn't added
                if count != 0:
                    dict[exercise + "_average"] = (sum/count)
                    dict[exercise + "_min"] = [min, min_date]
                    dict[exercise + "_max"] = [max, max_date]

                if count != 1 and count != 0:
                    dict[exercise + "_average_increase"] = (average_increase_sum/(count - 1))

                print(count)
                #print(dict)

    # Calculates the local average for each text input cell and automatically adds it
    #
    # The weights in the text input must be in the format #/#/#, with the slashes seperating each set's weight
    # (i.e. 100/105/110 would then be updated automatically to 100/105/110 = 105)
    #
    # @param string name_of_screen is the name of the spreadsheet
    def calculate_average(self, name_of_screen):
        if name_of_screen == "workout_screen_1":
            text_boxes_list = self.text_boxes_list_screen_1

        elif name_of_screen == "workout_screen_2":
            text_boxes_list = self.text_boxes_list_screen_2

        elif name_of_screen == "workout_screen_3":
            text_boxes_list = self.text_boxes_list_screen_3

        elif name_of_screen == "workout_screen_4":
            text_boxes_list = self.text_boxes_list_screen_4

        else:
            pass

        # Iterates through each textinput used to hold weights (not dates)
        for textinput in text_boxes_list:
            if textinput.text != "":

                # If there is already a "=" this gets rid of it
                if textinput.text.find("=") != -1:
                    textinput.text = textinput.text[0:textinput.text.find("=")]

                # Put in a try block so that program doesn't crash if the user formats the weights wrong
                try:
                    # Split each number into a list and convert to float
                    string_list = textinput.text.split("/")
                    numbers_list = []
                    for string in string_list:
                        numbers_list.append(float(string))

                    # Calculate the average of that list of floats
                    count = 0
                    sum = 0
                    for number in numbers_list:
                        sum += number
                        count += 1

                    # Update the text of the text input to include the average
                    textinput.text = textinput.text + "=" + str(sum/count)

                except:
                    pass

    # Adds the necessary labels to the stat screen after collecting the data
    #
    # @param string name_of_screen is the name of the spreadsheet
    # @param dict data_dict the dict holding the data for the spreadsheet
    # @param dict exercise_dict the dict holding the exercise names for the spreadsheet
    # @param list label_list the list holding the labels for a particular spreadsheet's data
    # @param ScrollView stat_scroll the scroll view holding all the labels for the stat screen
    def add_stats(self, name_of_screen, data_dict, exercise_dict, stat_scroll):
        # Neutral variable to add all of the widgets to the correct screen
        stat_screen = self.root.ids[name_of_screen]

        # Variable to hold the grid
        stat_grid = GridLayout(cols = 5, size_hint_y = None, pos_hint = {"top": 0.2, "right": 0.1}, spacing = 10)#row_force_default=True, row_default_height = 100)
        stat_grid.bind(minimum_height=stat_grid.setter('height'))

        # Delete all the labels so that they are updated accordingly
        try:
            # If stat scroll already in the stat screen then remove it
            stat_screen.remove_widget(stat_scroll)
        except:
            pass

        stat_scroll.clear_widgets()
        
        # Go through all of the exercises
        for exercise_list in exercise_dict.values():
            for exercise in exercise_list:
                stat_label = Label(text = exercise, font_size = "10sp", size_hint_y=None, height=50, width=100)
                stat_grid.add_widget(stat_label)

                # If there is data for the exercise add it as a label, if not add a label that says "No Data"
                try:
                    min_label_text = ""
                    for text in data_dict[str(exercise + "_min")]:
                        min_label_text += str(text)
                        min_label_text += ", "
                    min_label = Label(text = min_label_text, font_size = "10sp", size_hint_y=None, height=50, width=100)
                    stat_grid.add_widget(min_label)

                except KeyError:
                    min_label = Label(text = "No data", font_size = "10sp", size_hint_y=None, height=50, width=100)
                    stat_grid.add_widget(min_label)

                try:
                    max_label_text = ""
                    for text in data_dict[str(exercise + "_max")]:
                        max_label_text += str(text)
                        max_label_text += ", "
                    max_label = Label(text = max_label_text, font_size = "10sp", size_hint_y=None, height=50, width=100)
                    stat_grid.add_widget(max_label)

                except KeyError:
                    max_label = Label(text = "No data", font_size = "10sp", size_hint_y=None, height=50, width=100)
                    stat_grid.add_widget(max_label)

                try:
                    avg_label_text = str(data_dict[str(exercise + "_average")])
                    avg_label = Label(text = avg_label_text, font_size = "10sp", size_hint_y=None, height=50, width=100)
                    stat_grid.add_widget(avg_label)

                except KeyError:
                    avg_label = Label(text="No data", font_size = "10sp", size_hint_y=None, height=50, width=100)
                    stat_grid.add_widget(avg_label)

                try:
                    avg_increase_label_text = str(data_dict[str(exercise + "_average_increase")])
                    avg_increase_label = Label(text=avg_increase_label_text, font_size = "10sp", size_hint_y=None, height=50, width=100)
                    stat_grid.add_widget(avg_increase_label)

                except KeyError:
                    avg_increase_label = Label(text="No data", font_size = "10sp", size_hint_y=None, height=50, width=100)
                    stat_grid.add_widget(avg_increase_label)

        # Add the grid to the scroll view and the scrollview to the screen itself
        stat_scroll.add_widget(stat_grid)
        stat_screen.add_widget(stat_scroll)



    # Tied to a button so that calculate_average() and calculate_stats() are both performed
    # after pressing the button
    #
    # @param string name_of_screen is the name of the spreadsheet
    def collect_data(self, name_of_screen):

        if name_of_screen == "workout_screen_1":
            self.calculate_average("workout_screen_1")
            self.calculate_stats(self.workout_screen_1_data, self.split_exercises_1, self.date_dict_1, "stat_screen_1")
            self.add_stats("stat_screen_1", self.workout_screen_1_data, self.split_exercises_1, self.stat_scroll_1)

        elif name_of_screen == "workout_screen_2":
            self.calculate_average("workout_screen_2")
            self.calculate_stats(self.workout_screen_2_data, self.split_exercises_2, self.date_dict_2, "stat_screen_2")
            self.add_stats("stat_screen_2", self.workout_screen_2_data, self.split_exercises_2, self.stat_scroll_2)

        elif name_of_screen == "workout_screen_3":
            self.calculate_average("workout_screen_3")
            self.calculate_stats(self.workout_screen_3_data, self.split_exercises_3, self.date_dict_3, "stat_screen_3")
            self.add_stats("stat_screen_3", self.workout_screen_3_data, self.split_exercises_3, self.stat_scroll_3)

        elif name_of_screen == "workout_screen_4":
            self.calculate_average("workout_screen_4")
            self.calculate_stats(self.workout_screen_4_data, self.split_exercises_4, self.date_dict_4, "stat_screen_4")
            self.add_stats("stat_screen_4", self.workout_screen_4_data, self.split_exercises_4, self.stat_scroll_4)

        else:
            pass

    # Creates split name: day of the week dict from the text input boxes
    #
    # @param radiobutton instance the radio button who's data is being used
    # instance can either be "Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"
    def create_split_dict(self,instance):

        if self.actual_name == "workout_screen_1":
            split_day = self.split_day_1

        elif self.actual_name == "workout_screen_2":
            split_day = self.split_day_2

        elif self.actual_name == "workout_screen_3":
            split_day = self.split_day_3

        elif self.actual_name == "workout_screen_4":
            split_day = self.split_day_4

        # Creates the split dict with the format (Split Day: Day of the week)
        #
        # (i.e. "Back and Biceps": 'Mon'"
        if instance.group == "weekdays1":
            split_day[self.workoutday0.text] = instance.text

        if instance.group == "weekdays2":
            split_day [self.workoutday1.text] = instance.text

        if instance.group == "weekdays3":
            split_day [self.workoutday2.text] = instance.text

        if instance.group == "weekdays4":
            split_day [self.workoutday3.text] = instance.text

        if instance.group == "weekdays5":
            split_day [self.workoutday4.text] = instance.text

        if instance.group == "weekdays6":
            split_day [self.workoutday5.text] = instance.text

        if instance.group == "weekdays7":
            split_day [self.workoutday6.text] = instance.text

    # Obtains the next name of the radio button group so that each set of radio buttons belongs to a different group
    #
    # Radio Button groups make it so that only one button can be toggled at a time
    def get_next_group(self):
        return "weekdays" + str(self.weekdays)

    # Creates the radio button groups for each weekday
    #
    # @return week the GridLayout containing all 7 weekdays
    def get_days_of_the_week(self):
        week = GridLayout(cols = 7, size_hint_x = 0.5, size_hint_y = 0.1)

        sunday = ToggleButton(text = "Sun", font_size = "10sp", group = self.get_next_group())
        # When any of the radio buttons are pressed, create_split_dict() is called
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

    # Dynamically adds the labels and text inputs to ask for the name of each split day
    #
    # @param string (immediately converted to int) of the amount of days a week the user works out
    def ask_split(self,days_of_week):
        try:
            days = int(days_of_week)
            # The days of the week have to be between 1 and 7
            if days >= 1 and days <= 7 and self.add_split_pressed == False:
                # Prevents the button from being pressed twice
                self.add_split_pressed = True
                addworkout_screen = self.root.ids["add_workout_screen"]
                self.split_grid = GridLayout(cols_minimum = {0: 50, 1: 500},cols = 2, rows = days, size_hint_x = 0.9, size_hint_y = 0.25, pos_hint = {"top": 0.55, "right": 0.95})
                # Adds the appropriate number of labels
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
                    # For each label denoting the split name, adds the radio button groups with the days of the week
                    self.split_grid.add_widget(self.get_days_of_the_week())
                addworkout_screen.add_widget(self.split_grid)

        except:
            # Don't do anything if the string is not a number
            pass

    # Automatically creates a label with a certain font size
    #
    # @param string text the text of the label
    def create_label(self,text):
        return Label(text = text, font_size = '10sp')

    # Dynamically adds the labels and text inputs to ask for the name of each exercise of a particular split day
    #
    # @param string (immediately converted to int) of the amount of days a week the user works out
    def ask_exercises(self, days_of_week):

        if self.actual_name == "workout_screen_1":
            split_day = self.split_day_1

        elif self.actual_name == "workout_screen_2":
            split_day = self.split_day_2

        elif self.actual_name == "workout_screen_3":
            split_day = self.split_day_3

        elif self.actual_name == "workout_screen_4":
            split_day = self.split_day_4

        try:
            days = int(days_of_week)
            # The days of the week have to be between 1 and 7
            addworkout_screen = self.root.ids["add_workout_screen"]
            if days >= 1 and days <= 7:
                # Prevents the button from being pressed twice
                self.exercises_grid = GridLayout(cols_minimum={0: 50, 1: 500}, cols=2, rows=days, size_hint_x=0.9, size_hint_y=0.25,
                            )
                count = 0

                # Iterates through each split day to add the appropriate amount of labels
                for splitname in split_day.keys():
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

                # Added to a scrollview so that if it gets too big you can scroll through
                # However it doesn't work LOL
                self.exercises_scroll = ScrollView(pos_hint={"top": 0.25, "right": 1}, do_scroll_y = True)
                self.exercises_scroll.add_widget(self.exercises_grid)
                addworkout_screen.add_widget(self.exercises_scroll)

        except:
            # Don't do anything if the string is not a number
            pass

    # Clears the add workout screen when either the back or submit button is hit
    def clear_addworkout_screen(self):
        addworkout_screen = self.root.ids["add_workout_screen"]

        # Reset the text input for number of weekdays
        text_input_num_of_weekdays = addworkout_screen.ids["workout_days"]
        text_input_num_of_weekdays.text = ""


        if self.split_grid is not None:
            self.split_grid.clear_widgets()
            addworkout_screen.remove_widget(self.split_grid)
            self.split_grid = None

        if self.exercises_scroll is not None:
            self.exercises_grid.clear_widgets()
            addworkout_screen.remove_widget(self.exercises_scroll)
            self.exercises_grid = None
            self.exercises_scroll = None

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

    # Used to create the split_exerices dict
    #
    # (i.e. "Back and Biceps": ["Hammer Curls", "Deadlift"])
    def submit_exercises(self):
        if self.actual_name == "workout_screen_1":
            split_exercises = self.split_exercises_1

        elif self.actual_name == "workout_screen_2":
            split_exercises = self.split_exercises_2

        elif self.actual_name == "workout_screen_3":
            split_exercises = self.split_exercises_3

        elif self.actual_name == "workout_screen_4":
            split_exercises = self.split_exercises_4

        if self.splitname1.text != "":
            # In the textinput each exercise is seperated by ", " so that an easy list forms
            split_exercises[self.workoutday0.text] = self.splitname1.text.split(", ")

        if self.splitname2.text != "":
            split_exercises[self.workoutday1.text] = self.splitname2.text.split(", ")

        if self.splitname3.text != "":
            split_exercises[self.workoutday2.text] = self.splitname3.text.split(", ")

        if self.splitname4.text != "":
            split_exercises[self.workoutday3.text] = self.splitname4.text.split(", ")

        if self.splitname5.text != "":
            split_exercises[self.workoutday4.text] = self.splitname5.text.split(", ")

        if self.splitname6.text != "":
            split_exercises[self.workoutday5.text] = self.splitname6.text.split(", ")

        if self.splitname7.text != "":
            split_exercises[self.workoutday6.text] = self.splitname7.text.split(", ")

        print(split_exercises)

    # Used to automatically add the average to the data dict
    #
    # (i.e. after the text input looks like this 12/13/14 = 13.0 then it would automatically add 13.0 to the data dict)
    def on_text(self, instance, value):
        data_creator = {}
        row_dict = {}

        if self.actual_name == "workout_screen_1":
            data_creator = self.workout_screen_1_data
            row_dict = self.row_dict_1

        elif self.actual_name == "workout_screen_2":
            data_creator = self.workout_screen_2_data
            row_dict = self.row_dict_2

        elif self.actual_name == "workout_screen_3":
            data_creator = self.workout_screen_3_data
            row_dict = self.row_dict_3

        elif self.actual_name == "workout_screen_4":
            data_creator = self.workout_screen_4_data
            row_dict = self.row_dict_4

        else:
            pass

        # Used to obtain the row number of the text input
        row_num = int(instance.id[3:5])

        # Used to obtain the first digit of the column number of the text input
        # Adds one so that the position corresponds to the index in the data dict's list
        #
        # (i.e. if the column number is 14 )
        position = int(instance.id[8:10]) + 1
        exercise_name = row_dict[row_num]

        # Adds the average to the data dict (the number after the "=")
        if instance.text != "" and instance.text.find("=") > -1:
            # If the position has not yet been created in the split dict (if workouts were skipped)
            # then sentinal values are put in place
            #
            # This is done to ensure that the dates match up with the statistics
            while position >= len(data_creator[exercise_name]):
                data_creator[exercise_name].append(None)
            print("position", position)
            data_creator[exercise_name][position] = float(instance.text[instance.text.find("=") + 1:])
        else:
            pass

    # Used to switch to the next spreadsheet when creating a new one
    def advance_screen_name(self):
        if self.temp_actual_name == "workout_screen_0":
            self.actual_name = "workout_screen_1"
            self.temp_actual_name = "workout_screen_1"

        elif self.temp_actual_name == "workout_screen_1":
            self.actual_name = "workout_screen_2"
            self.temp_actual_name = "workout_screen_2"

        elif self.temp_actual_name == "workout_screen_2":
            self.actual_name = "workout_screen_3"
            self.temp_actual_name = "workout_screen_3"

        elif self.temp_actual_name == "workout_screen_3":
            self.actual_name = "workout_screen_4"
            self.temp_actual_name = "workout_screen_4"

        else:
            pass

    # Used to switch to the precious spreadsheet when the back button is hit on the addworkout screen
    def revert_screen_name(self):
        if self.temp_actual_name == "workout_screen_1":
            self.actual_name = "workout_screen_1"
            self.temp_actual_name = "workout_screen_0"

        elif self.temp_actual_name == "workout_screen_2":
            self.actual_name = "workout_screen_1"
            self.temp_actual_name = "workout_screen_1"

        elif self.temp_actual_name == "workout_screen_3":
            self.actual_name = "workout_screen_2"
            self.temp_actual_name = "workout_screen_2"

        elif self.temp_actual_name == "workout_screen_4":
            self.actual_name = "workout_screen_3"
            self.temp_actual_name = "workout_screen_3"

        else:
            pass

    # Used to clear the dicts for the (Split Day: Exercise) and (Split Day: Weekday) if the back
    # button is hit on the addworkout screen
    def clear_dicts(self):
        if self.actual_name == "workout_screen_1":
            self.split_exercises_1 = {}
            self.split_day_1 = {}
        elif self.actual_name == "workout_screen_2":
            self.split_exercises_2 = {}
            self.split_day_2 = {}
        elif self.actual_name == "workout_screen_3":
            self.split_exercises_3 = {}
            self.split_day_3 = {}
        elif self.actual_name == "workout_screen_4":
            self.split_exercises_4 = {}
            self.split_day_4 = {}
        else:
            pass

    # Used to change to the correct spreadsheet from the existing splits screen
    def change_active_spreadsheet(self, name_of_screen):
        if name_of_screen == "workout_screen_1":
            self.actual_name = "workout_screen_1"

        elif name_of_screen == "workout_screen_2":
            self.actual_name = "workout_screen_2"

        elif name_of_screen == "workout_screen_3":
            self.actual_name = "workout_screen_3"

        elif name_of_screen == "workout_screen_4":
            self.actual_name = "workout_screen_4"

        else:
            pass

# Used as the main method: just runs the app
if __name__ == '__main__':
    GainsApp().run()