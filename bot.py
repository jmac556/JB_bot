import requests
from itertools import product
import sys
import time
import datetime

base_url = "https://blobcast.jackboxgames.com/room/"


def test_room_code(codes):
    #Iterate through all the variations of the code
    for code in codes:
        try:
            jackbox_url = base_url + str(code)
            r = requests.get(url=jackbox_url)
            data = r.json()
            #If a match is found
            if r.status_code == 200:
                room_row = str(data['roomid'])
            #No match found
            else:
                room_row = '====='
            print(room_row)
        except:
            print("EXCEPTION OCCURED - Jackbox end")

def main():
    #Get user input from arguments
    three_letter_code = sys.argv[1]
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    room_codes = []
    #Generate all room codes based on the first 3 letters streamer gives
    for i in chars:
        room_codes += [three_letter_code + i]
    #Call main test function
    test_room_code(room_codes)
    
#Auto-run main on launch
if __name__ == "__main__":
    main()
