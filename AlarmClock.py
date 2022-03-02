# (Just use a string for the time. Don’t worry about the built in py stuff to get real time. Don’t 
#   overcomplicate this one!)
# Set up:
# As a developer, I want to use Python’s proper snake_case for variable names.
# As a developer, I want to create a AlarmClock class.
# As a developer, I want the AlarmClock class to have class instance variables to keep track of the 
#   AlarmClock’s current time, whether the alarm is on or off, and the time the alarm is set to. 
#   (You can use arbitrary strings to represent the time, it does not need to accurately tell the
#    current time or change over time).
# As a developer, I want the AlarmClock class to have a method to set (or change) the current time 
#   and print to the console the current time.
# As a developer, I want the AlarmClock class to have a method to toggle the alarm on or off. 
# 	-T/F Bool would be great; if self.alarm = false then set it to true (if/else)
# As a developer, I want the AlarmClock class to have a method to set the current alarm time and 
#   print to the console the current alarm time.
# Using it: 
# As a developer, I want to import the AlarmClock class into main.py so I can instantiate it as a 
#   new AlarmClock object and call methods on it.
# 1.	Print the clock’s time to the terminal
# 2.	Call the alarm clock’s change time method to change the time
# 3.	Toggle the alarm clock’s on off switch

# Then send code/screen shot and say that you’re moving on

class AlarmClock:
    def __init__(self, alarm):
        self.time = ''
        self.alarm = alarm   #'on' #or True #can be the same as the self thing or different.
        self.alarm_time = ''
    
    def set_current_time(self):
        self.time = input('Enter current time: ')
        print('Current time is:', self.time)
    
    def alarm_on_off(self):
        if self.alarm == True:
            print('Alarm on')
        else:
            print('Alarm off')

    def set_alarm_time(self):
        self.alarm_time = input('Enter a time to set for the alarm: ')
        print('Alarm is set for: ', self.alarm_time)

    