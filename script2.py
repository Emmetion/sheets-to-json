import json
import os
import sys

if (len(sys.argv) < 2): # less than required amount of arguments
    print("Please include your input. Syntax: \"python script.py <input-file> [pretty]\" <> = required, [] = optional")
    exit()
elif (len(sys.argv) > 3): # more than option amount of arguments
    print("Too many parameters input. Syntax: \"python script.py <input-file> [pretty]\" <> = required, [] = optional")
    exit()

inputFileName = sys.argv[1] # Gets the entries-file name
inputFile = None
try:
    inputFile = open(inputFileName, "r+") # The old timeline-entries.json from the google sheets.
except:
    print("Invalid input-file. Syntax: \"python script.py <input-file> [pretty]\" <> = required, [] = optional")
    exit()

jsonInput = json.load(inputFile) # Load the file into a json object.

if (os.path.exists("output") == False):
    os.mkdir("output")

outputFileName = None
outputFile = None
for i in range(50):
    outputFileName=  "timeline-data-export-" + str(i + 1) + ".json"
    if (os.path.exists("output/"+outputFileName)):
        continue
    else:
        outputFile = open("output/"+outputFileName, "w") # The old timeline-entries.json from the google sheets.
        break

if (outputFile == None):
    print("[FATAL] Output file error, please delete all your timeline-data-exports-?.json files")
    exit()

pretty = False
if (len(sys.argv) == 3):
    prettyString = sys.argv[2]
    if ("pretty" in prettyString): # Will change output type to pretty if 
        pretty = True

def generateData(old_json): # Method for formatting old json to new json
 
    json_obj = {}

    json_obj["title"] = []

    json_obj["events"] = []
    for i in range(len(old_json)):
        currentData = jsonInput[i]

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
        media_caption = currentData["Media Caption"]
        media_credit = currentData["Media Credit"]
        media_thumbnail = currentData["Media Thumbnail"]
        type = currentData["Type"]
        event_types = currentData["Event Types"]
        background = currentData["Background"]


        if ("title" in type): # If the type is title, it will be filtered and input as a title.
            if (len(json_obj["title"]) >= 1): # We don't want more than one title slide, but we will warn the user there were 2 listed.
                print("  [WARNING] Multiple Title Slides Detected, using only one. Make sure you only have one title slide in your google spreadsheet!")
                continue
            json_obj["title"].append({
                'media' : {
                    'url' : media,
                    'thumbnail' : media_thumbnail,
                    'caption' : media_caption,
                    'credit': media_credit,
                },
                'text' : {
                    'headline' : headline,
                    'text' : text
                }
            })
            continue
            
        # Reformats the event types to no longer be a string and instead an array of strings (types).
        event_types = event_types.split()

        # Adds an event with all information possible.

        # json_payload = {}

        # media = {}

        # if (media)

        start_date = {
            'year' : year
        }
        

        if (month != ""): start_date["month"] = month
        if (day != ""): start_date["day"] = day
        if (time != ""): start_date["time"] = time

        end_date = {}

        if (end_year) != "": end_date["year"] = end_year
        if (end_month != ""): end_date["month"] = end_month
        if (end_day != ""): end_date["day"] = end_day
        if (end_time != "") : end_date["time"] = end_time

        media_data = {}
        
        if (media != ""): media_data["url"] = media
        if (media_thumbnail != ""): media_data["thumbnail"] = media_thumbnail
        if (media_caption != ""): media_data["caption"] = media_caption
        if (media_credit != ""): media_data["credit"] = media_credit

        text_data = {}

        if (headline != ""): text_data["headline"] = headline
        if (text != ""): text_data["text"] = text

        event = {
        'media' : media_data,
        'start_date' : start_date,
        'end_date': end_date, 
        'text' : {
            'headline': headline,
            'text' : text
        },
        'display_date' : display_date,
        'background' : background,
        'event_types' : event_types,
        'type' : type
        }

        json_obj["events"].append(event)


        
    return json_obj # outputs the new formatted json

print("\n\nBUILD LOG:")

jsonOutput = generateData(jsonInput) # Gives us out jsonOutput for the new file.
dump = None
if (pretty):
    dump = json.dumps(jsonOutput, indent=2) # Prints it into the document with an indent for beautification.
else:
    dump = json.dumps(jsonOutput) # Prints it into the document with an indent for beautification.


outputFile.write(dump) # Writes it into the document and saves.

title_slide = None
if (len(jsonOutput["title"]) == 1):
    title_slide = jsonOutput["title"][0]


print("  [SUCCESS] Compiled output file " + outputFileName + " from input file " + inputFileName + "\n\n")
print("OUTPUT INFORMATION:")
print("  - Input File            : " + inputFileName)
print("  - Output File           : " + outputFileName)
print("  - Title Slide Headline  : " + ("N/A" if title_slide == None else title_slide["text"]["headline"]))
print("  - Total Events: " + str(len(jsonOutput["events"])))
if (pretty): print("  - Pretty Print          : True")
