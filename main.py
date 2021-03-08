from pynput.keyboard import Listener, Key


def log(text):
    #with open("log.txt", "a") as file_log:
        #file_log.write(text)
    print(text)


def monitor(key):
    log (str(key))
    if key == Key.esc:
        return False


with Listener(on_release=monitor) as listner:
    listner.join()