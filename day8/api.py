# with threading
import urllib.request
import threading
import time
import json
import ssl
def download_json():
    try:
        print("connecting to api")
        time.sleep(2) 
        url='https://fakestoreapi.com/products'
        headers={
            "User_Agent":"Mozilla/5.0"
        }
        req=urllib.request.Request(url,headers=headers)
        context=ssl._create_unverified_context()
        with url.request.urlopen(req,context=context)as response:
            data=response.read()
        print("Data downloaded")
    # data=urllib.request.urlopen(url).read()
    # data=urllib.request.urlretrieve(url,'filename')
    # time.sleep(2)
        posts=json.loads(data)
        with open('posts.json','w')as f:
            json.dump(posts,f,indent=4)

        print("download complete")
    except Exception as e:
        print("Error:",e)

t=threading.Thread(target=download_json)
t.start()
print("Main thread continues execution")





# without threading
import urllib.request
import time
import json
import ssl

def download_json():
    try:
        print("Connecting to API...")
        time.sleep(2)

        url = 'https://fakestoreapi.com/products'
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        req = urllib.request.Request(url, headers=headers)
        context = ssl._create_unverified_context()

        with urllib.request.urlopen(req, context=context) as response:
            data = response.read()

        print("Data downloaded")

        posts = json.loads(data)

        with open('posts.json', 'w') as f:
            json.dump(posts, f, indent=4)

        print("Download complete")

    except Exception as e:
        print("Error:", e)

# Normal function call (no threading)
download_json()

print("Program finished")