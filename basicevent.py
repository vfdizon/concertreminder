import requests
import json
import notify2
import tomlfile
from dateutil import parser as dateparser
import tomli
import os

class BasicEvent:
    eventid = None
    title = None
    date = None
    response = None
    responseDataJSON = None
    valuesMap = None

    time = None
    performer = None
    venue = None

    def __init__(self, settingsfile:tomlfile.TomlFile):
        eventid = settingsfile.getValue('eventid')
        clientid = settingsfile.getValue('clientid')

        if(eventid == None or clientid == None):
            print("No event id or client id, please configure, run this command with -h for more information")
            exit()

        api_url = "https://api.seatgeek.com/2/events/" + eventid
        api_params = {
            "client_id": clientid
        }

        self.eventid = eventid
        self.response = requests.get(api_url, api_params)
        self.responseDataJSON = json.dumps(self.response.json(), indent=4)
        self.valuesMap = json.loads(self.responseDataJSON)
        
    def getValue(self, key:str):
        return json.dumps(self.valuesMap[key], indent=4)
    
    def getSecondary(self, key_main:str, key_secondary:str):
        tempMap = self.valuesMap[key_main]
        return tempMap[key_secondary]
    
    def getReminder(self):
        title = self.getValue("title")
        print(title)

        notify2.init("event reminder")
        notification = notify2.Notification(title)
        notification.show()
        dateRaw = self.getValue("datetime_local")
        dateParsed = dateparser.parse(dateRaw[1:len(dateRaw) - 1])
        
        # text = "The " + self.getValue("type") + " at " + date.date()


            
        




        

