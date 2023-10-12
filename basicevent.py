import requests
import json
import notify2
from dateutil import parser as dateparser
import datetime
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

    def __init__(self, clientid:str, eventid:str):

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
        title = title[1:len(title)-1] + " "
        notify2.init("event reminder")
        dateRaw = self.getValue("datetime_local")
        dateParsed = dateparser.parse(dateRaw[1:len(dateRaw) - 1])
        timeUntil = "is in " + str(dateParsed - datetime.datetime.now()) 
        notification = notify2.Notification(summary = title + timeUntil)
        notification.show()


            
        




        

