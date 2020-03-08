import time

timeout = time.time() + 5

timeout2 = time.time() + 0.1

def muster2(anfang, ende):
    x = anfang
    while x<=1:
        print("********")
        x+=1
    while ende>=2:
        print("*      *")
        while True:
            test = 0
            if time.time() < timeout:
                break
            test = test - 1
            while True:
                zu = 0
                if zu==0:
                    zu = zu - 1
                    u = "----"
                    print(u)
