
import random

class RemoteControl:

    def __init__(self, tv_status="Off", tv_volume=0, channel_list=["BBC", "ESPN","FOX","Euronews", "Discovery", "MTV", "CCTV", "Nickelodeon","SKYsports", "HBO", "HBO Max"], channel="BBC", favorite_channels=[]):
        print("Creating Remote Control...")

        self.tv_volume = tv_volume
        self.tv_status = tv_status
        self.channel_list = channel_list
        self.channel = channel
        self.favorite_channels = favorite_channels
        self.muted = False
        self.parental_control_enabled = False
        self.parental_control_pin = None
        self.sleep_timer = None
        self.user_profiles = {}

    def adjust_volume(self):
        while True:
            character = input("Press '<' to Decrease Volume, '>' to Increase Volume, 'm' to Mute/Unmute, 'q' to Save")

            if character == "<":
                if self.tv_volume != 0:
                    self.tv_volume -= 1
                    print("Volume:", self.tv_volume)
            elif character == ">":
                if self.tv_volume != 32:
                    self.tv_volume += 1
                    print("Volume:", self.tv_volume)
            elif character == "m":
                self.toggle_mute()
            else:
                print("Volume Updated:", self.tv_volume)
                break

    def toggle_mute(self):
        self.muted = not self.muted
        if self.muted:
            print("TV Muted")
        else:
            print("TV Unmuted")

    def turn_off_tv(self):
        print("Turning off TV.")
        self.tv_status = "Off"

    def turn_on_tv(self):
        print("Turning on TV.")
        self.tv_status = "On"

    def __str__(self):
        return "TV Status: {}\nVolume: {}\nChannels: {}\nCurrent Channel: {}\n".format(self.tv_status, self.tv_volume, self.channel_list, self.channel)

    def __len__(self):
        return len(self.channel_list)

    def random_channel(self):
        random_index = random.randint(0, len(self.channel_list)-1)
        self.channel = self.channel_list[random_index]
        print("Current Channel:", self.channel)

    def add_channel(self, channel):
        print("Channel Added: ", channel)
        self.channel_list.append(channel)

    def change_channel(self):
        selected_channel = input("Enter the channel you want to switch to:")
        if selected_channel in self.channel_list:
            while True:
                character = input("Press '<' to Decrease Channel, '>' to Increase Channel, 'q' to Save")
                if character == "<":
                    index = self.channel_list.index(selected_channel)
                    if index != 0:
                        self.channel = self.channel_list[index - 1]
                        print("Channel:", self.channel)
                elif character == ">":
                    index = self.channel_list.index(selected_channel)
                    if index != len(self.channel_list) - 1:
                        self.channel = self.channel_list[index + 1]
                        print("Channel:", self.channel)
                elif character == "q":
                    print("Channel Updated:", self.channel)
                    break
                else:
                    print("Invalid input. Please try again.")
        else:
            print("Invalid channel. Please select a channel from the list.")


    def add_favorite_channel(self, channel):
        if channel in self.channel_list and channel not in self.favorite_channels:
            self.favorite_channels.append(channel)
            print("Channel Added to Favorites:", channel)
        else:
            print("Channel not found or already in favorites.")

    def enable_parental_control(self, pin):
        self.parental_control_enabled = True
        self.parental_control_pin = pin
        print("Parental Control Enabled.")

    def set_sleep_timer(self, duration):
        self.sleep_timer = duration
        print("Sleep Timer Set for", duration, "minutes.")

    def add_user_profile(self, profile_name, settings):
        self.user_profiles[profile_name] = settings
        print("User Profile", profile_name, "Added.")

remote_control = RemoteControl()
print("""*******************

Television Application

Operations:

1. Turn On TV
2. Turn Off TV
3. TV Information
4. Learn Number of Channels
5. Add Channel
6. Switch to Random Channel
7. Adjust Volume
8. Change Channel
9. Add Channel to Favorites
10. Enable Parental Control
11. Set Sleep Timer
12. Add User Profile

*******************

To Exit, Press 'q'.

*******************""")

while True:

    operation = input("Select Operation:")
    if operation == "q":
        print("Exiting Program...")
        break
    if operation == "1":
        remote_control.turn_on_tv()
    elif operation == "2":
        remote_control.turn_off_tv()
    elif operation == "3":
        print(remote_control)
    elif operation == "4":
        print("Number of Channels: ", len(remote_control))
    elif operation == "5":
        channels = input("Enter Channels to Add, Separated by ',':")
        to_add = channels.split(",")
        for channel in to_add:
            remote_control.add_channel(channel)
    elif operation == "6":
        remote_control.random_channel()
    elif operation == "7":
        remote_control.adjust_volume()
    elif operation == "8":
        remote_control.change_channel()
    elif operation == "9":
        channel = input("Enter Channel to Add to Favorites:")
        remote_control.add_favorite_channel(channel)
    elif operation == "10":
        pin = input("Enter Parental Control PIN:")
        remote_control.enable_parental_control(pin)
    elif operation == "11":
        duration = int(input("Enter Sleep Timer Duration (in minutes):"))
        remote_control.set_sleep_timer(duration)
    elif operation == "12":
        profile_name = input("Enter User Profile Name:")
        settings = {}  # Add settings as needed
        remote_control.add_user_profile(profile_name, settings)
    else:
        print("Invalid Operation")





