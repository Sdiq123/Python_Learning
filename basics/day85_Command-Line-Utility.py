'''
Aapney kai saarey command line utility dekhey hongey which are invoked from the terminal 

Aaj ham dekhengey python ki sahayita se ye kaisey karinga
'''
# curl ek command line utility hein
# command line utility matlab jinko tum commands dekey istemaal karsaktey ho
# Python mein aap is cheez ko argparse ki sahayita se create kar saktey ho 

import argparse     # Built In Module hein Python mein
import requests

def download_file(url, loc):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                
                f.write(chunk)
                
    return local_filename


parser = argparse.ArgumentParser()

# Add Commad line Arguments
parser.add_argument("url", help = "Url of the file to download")
parser.add_argument("output", help = "by which name do you want to save your file")


# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.url)
print(args.output)
download_file(args.url, args.output)

# commad which you need to run
# python .\day85_Command-Line-Utility.py https://imagej.net/images/Cell_Colony.jpg sadiq_command_line.jpg