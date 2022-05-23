import json
import os
from re import S

if (os.path.exists("/Users/emmet/Downloads/sheets-to-json/timeline-entries-output.json")): os.remove("/Users/emmet/Downloads/sheets-to-json/timeline-entries-output.json")

jsonFile = open("timeline-entries.json", "r+")
data = json.load(jsonFile)


outfile = open("timeline-entries-output.json", "w")




def generateData(old_json):

    json_obj = {}

    json_obj["title"] = []
    json_obj["title"].append({
        'media' : {
            'caption' : "",
            'credit' : "",
            'url' : "",
            'thumbnail': ""
        },
        'text' : {
            'headline' : "Emmet's Example Timeline",
            'text' : "This is bottom text"
        }
    })

    json_obj["events"] = []
    for i in range(len(old_json)):
        currentData = data[i]

        year = currentData["Year"]
        month = currentData["Month"]
        day = currentData["Day"]
        time = currentData["Time"]
        end_year = currentData["End Year"]
        end_month = currentData["End Month"]
        end_day = currentData["End Day"]
        end_time = currentData["End Time"]
        display_date = currentData["Display Date"]
        headline = currentData["Headline"]
        text = currentData["Text"]
        media = currentData["Media"]
        media_credit = currentData["Media Credit"]
        media_thumbnail = currentData["Media Thumbnail"]
        type = currentData["Type"]
        event_types = currentData["Event Types"]
        background = currentData["Background"]

        # Reformats the event types to no longer be a year and instead an indexed list of strings.

        event_types = event_types.split()

        json_obj["events"].append({
        'media' : {
            'url' : media,
            'caption' : media_credit,
            'credit' : media_thumbnail
        },
        'start_date': {
            'year' : year,
            'month' : month,
            'day' : day,
            'time' : time
        },
        'end_date': {
            'year': end_year,
            'month': end_month,
            'day' : end_day,
            'time' : end_time
        },
        'text' : {
            'headline': headline,
            'text' : text
        },
        'display_date' : display_date,
        'background' : background,
        'event_types' : event_types,
        'type' : type
        })
        
    return json_obj

jsonOutput = generateData(data)
dump = json.dumps(jsonOutput)
outfile.write(dump)
print(jsonOutput)
