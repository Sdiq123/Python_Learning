'''
Kai baar aisa hota hein ki ham multiple process run karna chahtey hein apney ek programme ko istemaal karkey
kyunki hamara python programme jo hein vo kai saarey child processess ko spawn kar raha hota hein (spawn matlab - Process ko Start Karna)
par ye sab use karney ki mujhey kya zarurat hein , main to already MultiThread use kar raha hun

Ab Processes aur Thread mein thoda sa Difference hota hein

Processess - Agar aapkey paas Multiple CPUs hein to aap Processess ka istemaal karkey unko use karsaktey hein
           - Lekin Jo Processess hoti hein,vo ek bada kaam parallelly alag alag CPUs mein lagakar aap execute karna chahtey ho , heavy task ko to aap Processess ka istemaal karo

Thread - Agar Thread ka aap use kar rahey ho, to Thread ko spwan karna ,use karna easy hota hein compared to Process
       - Threads Light Weight hotey hein, Threads ek Process ke andar hotey hein
'''

import multiprocessing
import requests
import concurrent.futures

def downloadFile(url, name):
    
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")


if __name__ == "__main__":
    url = "https://picsum.photos/200/300"
    # process = []

    # for i in range(50):      # ye underscore kya hota hein , ye throw of the variable hota hein, 
    #     # downloadFile( url, i )
    #     p = multiprocessing.Process(target=downloadFile, args=[url,i])
    #     p.start()
    #     process.append(p)
        
        
    # for p in process:
    #     p.join()
        
        
with concurrent.futures.ProcessPoolExecutor() as executor:
    l1 = [url for i in range(60)]
    l2 = [i for i in range(60)]
    results = executor.map(downloadFile, url, l)
    for r in results:
        print(r)
# jis tarah hamarey paas Thread Pool Executor hota hein usi tarah hamarey paas process pool executor bhi hota hein