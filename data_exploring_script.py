def data_explorer():
    import requests , json
    global value


    def menu():
        print("1.keys")
        print("2.values")
        print("3.Key,Value pair")
        print("4.dictionary key-values")
        print("5.Exit\n")



    def extract_data(a):
        d = a.text

        data = json.loads(d)

        x = [] #list of keys
        y = [] #list of values
        for i in data.keys():
            x.append(i)
        for i in data.values():
            y.append(i)

        print()
        while True:
            menu()
            a = input("Enter option : ")
            if a=="1":
                print()
                print("\t\t KEYS : ")
                cnt = 0
                for i in x:
                    print("\t\t",i)
                    cnt+=1
                print(f"\n\t\t Total number of keys : {cnt}\n")

            elif a=="2":
                print()
                print("\t\t VALUES : ")
                cnt = 0
                for i in y:
                    if type(i) is list:
                        print(f"\t\t dictionary(key and value pair) {type(i)}")
                    else:
                        print("\t\t",i)
                    cnt+=1
                print(f"\n\t\t Total number of values : {cnt}\n")

            elif a=="3":
                print()
                cnt = 0
                if len(x)==len(y):
                    print("\t\tKEY : VALUE")
                    for i in range(len(x)):
                        if type(y[i]) is list:
                            print(f"\n\t\t{x[i]} : dictionary(key and value pair) {type(y[i])}\n")
                        else:
                            print(f"\n\t\t{x[i]} : {y[i]}\n")
                        cnt+=1
                print(f"\n\t\tTotal number of key-value pairs : {cnt}\n")

            elif a=="4":
                value = []
                cnt = 1
                cnt1 = 0
                for i in y:
                    if type(i) is list:
                        print(f"\n\t\t{i}\n")
                        value.append(i)
                        print("\t\tdictionary number :",cnt)
                        cnt = cnt + 1
                        cnt1  = cnt1 + 1
                print("\t\tTotal number of dictionaries :",cnt1,"\n")
                



            elif a=="5":
                print("Exiting...")
                break
            else:
                print("\nInvalid option\n")

        #print(value)
        
    api = input("Enter API : ")

    if len(api)==0:
        print("No api entered!!!")
    else:
        key = input('Enter KEY : ')
        if len(key)==0:
            if ("key" in api) or ("api" in api):

                a = requests.get(api)

                if a.status_code==200:
                    print(f"\n{a.status_code} : connected")
                    extract_data(a)

                    
                else:
                    print(f"\n{a.status_code} : disconnected")
            else:
                print("API key missing!!!")
        else:
            api = api + "api_key=" + key

            a = requests.get(api)

            if a.status_code==200:
                print(f"\n{a.status_code} : connected")
                extract_data(a)

                    
            else:
                print(f"\n{a.status_code} : disconnected")


