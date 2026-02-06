# from multiprocessing import Process

# def worker_function():
#     print("Worker is running")

# if __name__ == "__main__":
#     p = Process(target=worker_function)
#     p.start()
#     p.join()

#     print("Main process is done")
    
    
    

import time
from multiprocessing import Pool
def square(n):
    return n * n
if __name__ == "__main__":
    numbers = [10**7,10**2,10**3,10**4,10**5]
    start=time.time()
    with Pool() as p:
        result=p.map(square,numbers)
    end=time.time()
    print("Squares:",result)
    print("Time taken with multiprocessing:",end-start)
    
    
    
    
import time
from multiprocessing import Pool, Process,Queue
def worker(q):
    q.put("hello")
if __name__ == "__main__":
    q=Queue()
    p=Process(target=worker,args=(q,))
    p.start()
    p.join()
    result=q.get()
    print("Message from worker:",result)
    
    
    
    
    
    
from multiprocessing import Pool
import time

def simulate_region(region):
    print(f"Calculating weather for {region}...")
    time.sleep(1)
    result = f"region {region} complete"
    return result

if __name__ == "__main__":
    regions = ['North', 'South', 'East', 'West']

    with Pool(processes=4) as p:
        result=p.map(simulate_region, regions)

    print("Results:", result )
    
    
    
    
from multiprocessing import Pool
import time
def analyze_log(chunk):
    print(f"Analyzing log chunk {chunk}...")
    time.sleep(1)
    result = f"log chunk {chunk} analyzed"
    return result
if __name__ == "__main__":
    log_chunks = [1, 2, 3, 4]

    with Pool(4) as p:
        result = p.map(analyze_log, log_chunks)

    print("Analysis Results:", result) 
    
    
    
