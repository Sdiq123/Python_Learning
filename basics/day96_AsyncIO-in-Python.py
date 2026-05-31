'''
Kis tarah ham Asynchronous Task kara saktey hein Pyhton mein, aur kaisey ham bahut saara time bacha saktey hein Python mein

Na heen ye Multithreading hein , na heen ye Mutli Processing hein, ye sirf ek tariqa hein jissey aap apna code Concurrently chala saktey hein

'''
# what is the Typical Execution Flow in Your Python Code ?
# baically main function1() ko chala raha hun , phir function2() ko chala raha hun , aisey kerkey main execute kar raha hun apney code ko
# ab hoga kya function1 chalney ke baad heen function2 chalega 

import time
import asyncio
import requests

async def function1():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.ico1", "wb").write(response.content)
    # await asyncio.sleep(1)
    print("func1")
     
    
async def function2():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.ico2", "wb").write(response.content)
    # await asyncio.sleep(1)
    print("func1")
    
    
async def function3():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.ico3", "wb").write(response.content)
    # await asyncio.sleep(1)
    print("func1")


# await ka matlab hota hein kisi bhi async function ke finish honey tak ka "Wait" Karlo, phir apna function chalao , phir uskey baad dusra functon chalao

'''async def main():
    task = asyncio.create_task(function1())
    # jab bhi usey time milega vo chaljayega 
    await function1()
    await function2()
    await function3()

# Kaisey main in teeno functions ko concurrently chala sakta hun, vo dekhtey hein "asyncio" ke madad se zarur karsaktey hein
asyncio.run(main())
'''

# Hamey aur ek cheez milti hein "GATHER" Syntax ka jo easy banata hein apney kaam ko

async def main():
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)

asyncio.run(main())
