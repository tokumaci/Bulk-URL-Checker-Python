from requests import get
from os import path

filename = ""
result_text="";
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
                        result_text+=str(index)+" "+url+" "+str(response.status_code)+"\r";
                        print(index, url, "\t", response.status_code)
                    except:
                        print(index, url, "BadURL!")
                with open("result.txt", "w") as f:
                    f.write(result_text)   
            else:
                print("*** File is empty! ***")
                filename = ""
    else:
        filename = ""
        print("*** File not found. Please try again. ***\n")

