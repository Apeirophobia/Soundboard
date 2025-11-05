import pygame._sdl2
from pygame import mixer
import pygame._sdl2.audio
import pygame._sdl2.controller
import pygame._sdl2.mixer
import pygame._sdl2.video
import sys
import keyboard

# Initialize:
# Press 'G' to play the sound
# Press 'L' to exit the soundboard
print("""
# Initialize:
# Select Device
# Press 'G' to play the sound
# Press 'L' to exit the soundboard
""")

#mixer.init(devicename="SteelSeries Sonar - Microphone (SteelSeries Sonar Virtual Audio Device)") # INPUT
#mixer.init(devicename="Headphones (JLab GO Air Pop Stereo") # OUTPUT
mixer.init(devicename="Speakers (Realtek(R) Audio)") # OUTPUT



for i in pygame._sdl2.audio.get_audio_device_names(False): # Output devices
    print(i)


mixer.music.load("moo audio for soundboard.wav")
#mixer.music.play()

def check():
    #print("keybind pressed")
    mixer.music.play()
    keyboard.press('v')
    while mixer.music.get_busy():
        continue
        #print("playing...")
    keyboard.release('v')
    #print("stopped")

keyboard.add_hotkey('b', lambda: check())

while keyboard.wait('l'):
    keyboard.wait()

mixer.quit()
sys.exit()