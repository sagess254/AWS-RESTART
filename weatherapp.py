import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"⏰ Alarm set for {alarm_time}. Waiting...")

    sound_file = "Xylophone Tip Toe Scale Up.mp3"  # replace with your sound file
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)  # shows ticking clock

        if current_time == alarm_time:
            print("🚨 Alarm time reached! Playing sound...")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            is_running = False  # stop loop after alarm triggers

        time.sleep(1)  # pause for 1 second each loop

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
    set_alarm(alarm_time)
