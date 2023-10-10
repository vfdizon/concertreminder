import basicevent
import argparse

parser = None

def init():
    global parser

    parser = argparse.ArgumentParser()
    parser.add_argument('--eventid', '-e', type=int)


def main():

    args = parser.parse_args()
    
    eventid = f"{args.eventid}"
    event = basicevent.BasicEvent(str(eventid))
    event.getReminder() 

init()
main()


