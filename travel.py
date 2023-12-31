import pandas as pd
""" from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
import os
import logging """


def getData(csv="./dataset/timetables.csv"):
    df = pd.read_csv(csv)

    columns_of_interest = ['TripId', 'Departure', 'Destination', 'Duration']
    data = df[columns_of_interest]

    dataController = []

    i = 0
    while i < len(data):
        trips = {
            "id": data.TripId[i],
            "departure": data.Departure[i],
            "destination": data.Destination[i],
            "duration": data.Duration[i]
        }
        dataController.append(trips)
        i += 1

    return dataController


def getTravel(dataController, locations):

    departure = locations[0]
    departureInitial = departure
    destination = locations[-1]
    destinationInitial = destination
    travels = []

    i = 0
    departureList = []
    destinationList = []
    while i < len(dataController):
        if departure in dataController[i]["departure"]:
            departureList.append(dataController[i]["departure"])
        if destination in dataController[i]["destination"]:
            destinationList.append(dataController[i]["destination"])
        i += 1

    departureListUnique = list(set(departureList))
    destinationListUnique = list(set(destinationList))

    print(destinationListUnique)

    if len(departureListUnique) == 1:
        departure = departureListUnique[0]
    if len(destinationListUnique) == 1:
        destination = destinationListUnique[0]

    # Trajet direct
    for departure in departureListUnique:
        for destination in destinationListUnique:
            trip = travelFunction(dataController, departure, destination)
            if trip:
                travels.append(trip)
    if len(travels) == 0:
        print("Aucun trajet direct de "
              + departureInitial + " à " + destinationInitial)

    for departure in departureListUnique:
        listAllDestinationFromDeparture = getAllDestinationFromDeparture(dataController, departure)
        i = 0
        while i < len(listAllDestinationFromDeparture):
            for destination in destinationListUnique:
                if travelFunction(dataController, listAllDestinationFromDeparture[i]["destination"], destination):
                    trip = {
                        "id": dataController[i]["id"],
                        "departure": departure,
                        "destination1": listAllDestinationFromDeparture[i]["destination"],
                        "destination2": destination,
                        "duration": str(int(listAllDestinationFromDeparture[i]["duration"]) +
                                    int(travelFunction(dataController, listAllDestinationFromDeparture[i]["destination"],
                                                   destination)["duration"]))
                    }
                    travels.append(trip)
            i += 1

    sorted_json_data = sorted(travels, key=lambda k: (int(k['duration'])), reverse=False)
    optimalTravel = sorted_json_data    

    return optimalTravel


def travelFunction(dataController, departure, destination):
    i = 0
    while i < len(dataController):
        if (departure in dataController[i]["departure"]) and (destination in dataController[i]["destination"]):
            trip = {
                "id": dataController[i]["id"],
                "departure": departure,
                "destination1": destination,
                "destination2": "",
                "duration": str(dataController[i]["duration"])
            }
            return trip

        i += 1


def getAllDestinationFromDeparture(dataController, departure):
    listAllDestinationFromDeparture = []
    i = 0
    while i < len(dataController):
        if departure in dataController[i]["departure"]:
            trips = {
                "id": dataController[i]["id"],
                "departure": departure,
                "destination": dataController[i]["destination"],
                "duration": dataController[i]["duration"]
            }
            listAllDestinationFromDeparture.append(trips)
        i += 1

    return listAllDestinationFromDeparture

######## FLASK

""" app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

def prod():
    load_dotenv()
    PORT = os.getenv("PORT")
    gunicorn_error_logger = logging.getLogger("travel_order.log")
    CORS(app)
    app.logger.handlers.extend(gunicorn_error_logger.handlers)
    app.logger.setLevel(logging.DEBUG)
    app.run(host="0.0.0.0", port=PORT)


#####

def main():
    dataController = getData()
    getTravel(dataController, ["Paris", "Vittel", "Marseille"]) """