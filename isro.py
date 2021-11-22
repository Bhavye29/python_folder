import requests,json
url = "https://isro.vercel.app/api/spacecrafts"
api = requests.get(url)
status = api.status_code
if status==200:#successful connection
    print("connected...")
    data = api.text
    d = json.loads(data)
    key = d.keys()
    value = d.values()

    '''
    for i in key:
        print(d[i])'''

    for i in value:
        one_value = i

    def number_value(one_value):
        cnt = 0
        for i in one_value:
            cnt+=1
        print(cnt)
        
    x = len(one_value)
    satellite_list = []
    for i in one_value:
        satellite_list.append(i)

    y = len(satellite_list)


    for i in range(y):
        print(f'{satellite_list[i]["id"]} : {satellite_list[i]["name"]}')    

else:
    print("disconnected!!!")
