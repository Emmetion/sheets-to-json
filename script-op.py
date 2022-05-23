import json
import os
import sys

if (len(sys.argv) != 3 and len(sys.argv) != 4): # Gets the length of arguments
    print("Please include your file names in the command.")
    print("Command Line Arguments: \"<input-file> <output-file> [pretty]\" <> = required, [] = optional")
    exit()
inputFileName = sys.argv[1] # Gets the entries-file name
inputFile = None
try:
    inputFile = open(inputFileName, "r+") # The old timeline-entries.json from the google sheets.
except:
    print("[ERROR] Invalid input-file.")
    print("Command Line Arguments: \"<input-file> <output-file> [pretty]\" <> = required, [] = optional")
    exit()

jsonInput = json.load(inputFile) # Load the file into a json object.

# Choose an output file name.
outputFileName = sys.argv[2]
outputFile = None

if (os.path.exists(outputFileName)): # Checks if output file is already generated, prevents overwriting. 
    print("Provided output-file already exists! (" + outputFileName + ")")
    exit()
if (outputFileName.endswith(".json") == False):
    print("Provided output file does not end with .json, please rerun this program with it correctly formatted.")
    exit()
try:
    outputFile = open(outputFileName, "w") # The old timeline-entries.json from the google sheets.
except:
    print("[ERROR] Invalid output-file.")
    print("Command Line Arguments: \"<input-file> <output-file> [pretty]\" <> = required, [] = optional")
    exit()

pretty = False
if (len(sys.argv) == 4):
    prettyString = sys.argv[3]
    if ("pretty" in prettyString): # Will change output type to pretty if 
        pretty = True

def generateData(old_json): # Method for formatting old json to new json
 
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
        json_obj["events"].append({
        'media' : {
            'url' : media, 
            'thumbnail' : media_thumbnail,
            'caption' : media_caption,
            'credit' : media_credit
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

print("  [SUCCESS] Compiled output file" + outputFileName + " from input file " + inputFileName + "\n\n")
print("OUTPUT INFORMATION:")
print("  - Input File            : " + inputFileName)
print("  - Output File           : " + outputFileName)
print("  - Title Slide Headline  : " + ("N/A" if title_slide == None else title_slide["text"]["headline"]))
print("  - Number of Events      : " +str(len(jsonOutput["events"])))
if (pretty): print("  - Pretty Print          : True")

