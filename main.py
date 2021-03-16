import requests
import time

link = input("What is your video link? \n")

while True:
  time.sleep(1)
  requests.get(link)
