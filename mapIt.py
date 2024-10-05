#! python3 
# mapIt.py - Launches a map in the browser using an address from the 
# command line or clipboard.



import webbrowser, sys, pyperclip

url = "http://www.google.com/maps/place/"
if len(sys.argv) > 1:
    #Get address from command line. 
    address = ' '.join(sys.argv[1:])
    print(f"Command Line: {address}")

else:
    #Get address from clipboard
    address = pyperclip.paste()
    print(f"Clipboard: {address}")

webbrowser.open(f"{url} + {address}")

