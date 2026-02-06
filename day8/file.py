# download files using threading
import urllib.request
import threading
import time
def download_file():
    url='https://localhost:8000/jk.txt'
    filename='downloaded_test.txt'
    
    print("Starting download for file")
    # time.sleep(2)
    urllib.request.urlretrieve(url,'filename')
    print("Completed download for file")
    
t=threading.Thread(target=download_file)
t.start()
print("Main Thread continues execution")