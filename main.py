import basicevent
import tomlfile
import argparse


parser = None

def init():
    global parser

    parser = argparse.ArgumentParser()
    parser.add_argument('--eventid', '-e', type=int, help='The id for the event you want to track (Only if you haven\'t set up an id or want to change it)')
    parser.add_argument('--key', '-k', type=str, help='Your client id (Only if you haven\'t set up an client id if you do not have one, you will have to register in https://seatgeek.com/account/develop)')
    


def main():
    args = parser.parse_args()

    settingsFile = tomlfile.TomlFile("concertReminder.toml")
    eventidArg = f"{args.eventid}"
    keyArg = f"{args.key}"    


    addSettings(eventid=eventidArg, key=keyArg, tomlfile=settingsFile)
    eventid = settingsFile.getValue('eventid')
    key = settingsFile.getValue('key')
    
    if(key == None or eventid == None):
        print("No event ID or client ID configured, run this command with -h for more information")
        exit()

    event = basicevent.BasicEvent(eventid=eventid, clientid=key)
    event.getReminder()


def addSettings(eventid:str, key:str, tomlfile:tomlfile.TomlFile):
    if(eventid != "None"):
        tomlfile.addValue("eventid", eventid)
    if(key != "None"):
        tomlfile.addValue("key", key)


init()
main()


