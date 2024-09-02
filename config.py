from pynput import keyboard
import main

# pair character keys with sound files here, in the format 'h': 'filename.mp3'
soundboard = {
    '1': 'America the Beautiful.mp3',
    '2': 'Crossing the Bar.mp3',
    '3': 'Every Little Thing She Does is Magic.mp3',
    '4': 'Hallelujah.mp3'
            }

# info for the counter function
counter_message = 'Your counter message goes here'
counter_start_number = 0
counter_increase_key = '5'
counter_decrease_key = '6'

# click the green arrow to run
if __name__ == '__main__':
    print('starting...')
    main.start_counter(counter_message, counter_start_number)
    with keyboard.Listener(on_press=main.on_press) as listener:
        listener.join()
