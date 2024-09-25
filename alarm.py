#https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203
# selct time, we display the count down, when time finishes then play the sound
from playsound import playsound
import time
#playsound("surya_son_of_krishna.mp3")

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
# The above are escape characters

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed<seconds:
        time.sleep(1)   # means wait for 1 sec and do other lines
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left//60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will ring in : {minutes_left:02d} : {seconds_left:02d}")
        #02d means pad with 2 zeros, if one zero is there then pad with 1
    playsound("surya_son_of_krishna.mp3")

minutes= int(input("ENter the number of minutes: "))
seconds = int(input(" How many seconds: "))
total_seconds = minutes*60 + seconds
alarm(total_seconds)