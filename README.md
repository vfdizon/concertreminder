# Concert Reminder
___

A simple python script to help remind you of your SeatGeek events using the SeatGeek API! This currently only works with linux systems with Python3 installed. This program will notify you how long the event is away from the current date in a notification. To set up, run ``` chmod +x setup && ./setup ```. This will create a binary called concertreminder in your /bin/ folder, then you can call concertreminder at any time to get notified after getting confugred. 

## Required Python Modules:
  - argparse
  - requests
  - notify2
  - tomli
  - tomli_w

## Usage 
usage: main.py [-h] [--eventid EVENTID] [--key KEY]

options:
  -h, --help            show this help message and exit
  --eventid EVENTID, -e EVENTID
                        The id for the event you want to track (Only if you haven't set up an id or want to change it). This will be the number at the end of the URL for the desired event page.
  --key KEY, -k KEY     Your client id (Only if you haven't set up an client id if you do not have one, you will have to
                        register in https://seatgeek.com/account/develop)

