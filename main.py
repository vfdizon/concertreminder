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
    eventid = f"{args.eventid}"
    key = f"{args.key}"    

    addSettings(eventid, key, settingsFile)

    eventid = basicevent.BasicEvent(settingsFile)
    eventid.getReminder()


def addSettings(eventid:str, key:str, tomlfile:tomlfile.TomlFile):
    if(eventid != "None"):
        tomlfile.addValue("eventid", eventid)
    if(key != "None"):
        tomlfile.addValue("key", key)
    exit()


init()
main()


