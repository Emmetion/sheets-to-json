# How to use this script?

Open your command line inside of a folder with a text document of what the Extention gave you and save it with .json on the end.
Then, we run a quick python script inside of our console
Read below to understand what everything means.

``python script.py <input-file> <output-file> [pretty]``

<> = Required, [] = Optional

Replace ``<input-file>`` with a JSON document of extracted google spreadsheet information. ex ``timeline-entries-example.json``

Replace ``<output-file>`` with a file name that you want for the output JSON.

Replace ``[pretty]`` with the word ``pretty`` if you want to view your output JSON file beautified, but it is not recommended to use this in production as it causes longer loading times. Leaving this option blank defaults it to minified.

Once you've used the script, some information should pop up about the outcome of your file.
Take the file with the name you gave (``<output-file>``), and download it.

Once you've downloaded it, it should look something like ``output-example.json``, and you should be all set to upload to whatever host you are using.

# Uploading to a Host Server

There are many methods to uploading JSON onto a webserver for you to use, but an efficient free one that's sort of straight forward. GitHub and jsdelivr are really good free ways to host content online. You upload your files to the GitHub Repository, and then jsdelivr sends that content to people requesting that data.

On GitHub, navigate to where you are hosting the JSON files for your websites, and upload a new file. Name the file what it's going to represent on the page.

Once you update the GitHub Repository, navigate to your website host and edit the javascript of the webpage you want to add/change the data of. Navigate to where you load the JSON in your timeline JavaScript.

Change the directory that the URL is pointing to. It should look something like `https://cdn.jsdelivr.net/gh/Emmetion/googlesheets-to-json/output-example.json`

And your done! You've successfully loaded your new events into a Timeline!