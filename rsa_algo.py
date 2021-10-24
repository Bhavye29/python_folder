def rsa():
    import time

    p,q = 53,59
    n = p*q
    e = 3
    t = (p-1)*(q-1)
    k = 2
    d = (k*t + 1)/e
    d = (k*t + 1)//e

    xy = "abcdefghijklmnopqrstuvwxyz "
    ox = {}
    for i in range(len(xy)):
        ox[i] = xy[i]

    print(ox)

    data = input()
    print(data)
    start = time.time()
    raw_data = ""


    for i in range(len(ox)):
        for j in range(len(data)):
            if data[j] == ox[i]:
                raw_data = raw_data + str(i + 1)


    print(f"Raw data : {raw_data}")

    def encrypt(raw_data):
        global encrypted
        encrypted = (int(raw_data)**e) % n
        print(f"Encrypted messege : {encrypted}")

    encrypt(raw_data)



    def decrypt(encrypted_data):
        global decrypted
        decrypted = ((encrypted_data)**d) % n
        #print(f"decrypted messege : {decrypted}")
        back = str(decrypted)
        original_data = ""
        for i in back:
            if int(i) in ox:
                original_data = original_data + ox[int(i)-1]
        print(f"Decrypted messege : {original_data}")
        print(f"Decrypted messege : {decrypted}")


    decrypt(encrypted)
    end = time.time()
    print(f"Elapsed time : {end-start}")
rsa()
