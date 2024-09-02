# soundboard_hotkeys
Python module for setting up a soundboard and click counter

1. Open and run install.py. You should see "wheel" upgrade, and playsound1.2.2 and pynput download successfully.
2. Open the soundfiles folder. Add as many mp3 files as you want, and remove any unneeded. Unlinked files don't cause an issue, so if you unlink a sound file from its hotkey, you don't need to remove it from the folder.
3. Open config.py. The "soundboard" dictionary links character keys to sound files. THe keys are case sensitive, so 1 and ! can be assigned separately, as can y and Y. Choose any number, letter, or symbol keys and pair it with the file names of mp3 in the soundfiles folder. Add more hotkeys by ending each line with a comma and a line break. The sound should play through system audio.
4. MAC ONLY: You'll need to go into System Settings -> Privacy and Security -> Input Monitoring, and enable Python IDLE and your Python interpreter to monitor input from your keyboard.
5. Editing the counter info only changes the information in counter.txt, so if you don't plan to use it, you can leave the information as open quotes (''). The counter_message appears before the number and with a space. \n will give you a line break, \t will give you a tab break. counter.txt can be paired with an OBS text box to automatically update the counter whenever you press the increase_key or decrease_key.
6. Run config.py.

That should do it!
