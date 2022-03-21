from requests import get
from os import path

filename = ""

while len(filename) <= 0:
    filename = input("Enter the full name of links file : ")
    if path.exists(filename):
        with open(filename) as f:
            url_list = f.readlines()
            if len(url_list) > 0:
                for index, url in enumerate(url_list, start=1):
                    url = url.strip()
                    try:
                        response = get(url)
                        print(index, url, "\t", response.status_code)
                    except:
                        print(index, url, "BadURL!")
            else:
                print("*** File is empty! ***")
                filename = ""
    else:
        filename = ""
        print("*** File not found. Please try again. ***\n")
