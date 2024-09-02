import playsound
import config


def start_counter(text: str, start: int):
    with open('counter.txt', 'w') as f:
        f.write(f'{text} {start}')


def counter_increase(increase: bool):
    with open('counter.txt') as f:
        info: list[str] = f.read().split(' ')
    text: str = ' '.join(info[:-1])
    count: int = int(info[-1])
    if increase: count += 1
    else: count -= 1
    print(count)
    start_counter(text, count)


def soundboard_play(filename: str):
    playsound.playsound(filename, block=False)


def on_press(key):
    try: key_char = key.char
    except AttributeError: return

    if key_char in config.soundboard.keys():
        try: soundboard_play(f'soundfiles/{config.soundboard[key_char]}')
        except playsound.PlaysoundException: print(f'{config.soundboard[key_char]} not found in soundfiles folder')
    elif key_char == config.counter_increase_key:
        counter_increase(True)
    elif key_char == config.counter_decrease_key:
        counter_increase(False)
