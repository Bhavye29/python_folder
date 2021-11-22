import requests,json

def explore_api_with_key(url,key):
    api = url + "api_key=" + key
    signal = requests.get(api)
    if signal.status_code==200:
        
        print(f"\n{signal.status_code} : connected...\n")
        
        d = signal.text
        data = json.loads(d) #convrting json to key,value pairs
        x = data.keys()
        y = data.values()
        print("The keys are : ")
        for i in x:
            print(i)
        print("\n")
        
        print("number of keys : ",len(x))
        print("number of values : ",len(y))
        print("\n")
        
        for i in x:
            print(i," : ",data[i])

        
    else:
        print(f"\n{signal.status_code} : disconneted")



def explore_api_without_key(url):
    api = url
    signal = requests.get(api)
    if signal.status_code==200:
        
        print(f"\n{signal.status_code} : connected...\n")
        
        d = signal.text
        data = json.loads(d) #convrting json to key,value pairs
        x = data.keys()
        y = data.values()
        print("The keys are : ")
        for i in x:
            print(i)
        print("\n")
        
        print("number of keys : ",len(x))
        print("number of values : ",len(y))
        print("\n")

        for i in x:
            print(i," : ",data[i])

        
    else:
        print(f"\n{signal.status_code} : disconneted")



url = input("Enter api : ")
if len(url)==0:
    pass

else:
    key = input("Enter key : ")
    
    if len(key)==0:
        if "api_key" or "api" in url:
            explore_api_without_key(url)
            
    else:
        explore_api_with_key(url,key)
