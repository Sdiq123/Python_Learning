'''
Multi Threading ki zarurat kyun hoti hein, taki aap resources ko parallelly download kar sako  

Agar merey paas 10 (dass) files hein 10 GB Ke aur main inhey paralelly download karna chahta hunto main vo Python main kar sakta hun

--> Python has a Module Called "Threading"

--> Agar aapko Parallel Execution Karna hein to Threading Module Bahut heen Zyada useful Hojata hein, Agar aapConcurrent Module Bhi Use Kartey ho to thoda easy hojata hein

'''


import threading   # thread se ham concurrent cheezein bana saktey hein
import time
from concurrent.futures import ThreadPoolExecutor   # ye ek module hota hein jo ki thread pool executor hota hein, jiska use karke aap apna code ko concurrent bana saktey ho   

# Thread Pool Executor , jab aap bulk mein yahan par kai saarey tasks ko schedule karna chatey ho to usmey aapki madad karta hein

# Indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

def main(): 
    # Normal Code    
    # func(4)
    # func(2)
    # func(1)    

    # time1 = time.perf_counter()    
    # Code Using Threads    
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    time1 = time.perf_counter()
    # Yahan par kya hoga ye teeno ek saath start hojayengey    
    t1.start()    # Start sirf Process ko start karkey aagey bad jaata hein , ye wait nahi karta process ke khatam honey ka, start karkey background mein process ko throw kardeta hein 
    t2.start()    
    t3.start()    

    t1.join()    # join() - ye process ke khatam honey tak bhi wait karta hein
    t2.join()
    t3.join()

    time2 = time.perf_counter()
    print(time2 - time1)  

    '''
    concurrent.features ---> ye ek Module hota hein, jo ki ek Thread Pool Executor hota hein, jiski madad se aap ek function ko Submit kar saktey ho aur issey result Prapt kar saktey ho

    '''
    
def poolingDemo():
    with ThreadPoolExecutor(max_workers=1) as executor:
        # future1 = executor.submit(func, 3)
        # future2 = executor.submit(func, 2)
        # future3 = executor.submit(func, 4)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        
        l = [3,5,1,2]
        results = executor.map(func, l)
        for result in results:
            print(result)
        
poolingDemo()


# Thread Pool Executor Ko Istemaal karney ka aur ek mazedaar Syntax hein vo hein Map Syntax ka 