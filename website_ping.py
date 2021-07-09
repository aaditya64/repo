from os import system
import schedule
import time

web1 = system("ping www.google.com")
web2 = system("ping www.yahoo.com")
web3 = system("ping www.bbc.co.uk")
web4 = system("ping www.iuwybacrioweuaj.com")
web5 = system("ping www.youtube.com")
ret1 = (web1)
ret2 = web2
ret3 = web3
ret4 = web4
ret5 = web5


def job234():
    if ret1 == 0:
        print("google is up and running")
    else:
        print("google is down")
    if ret2 == 0:
        print("yahoo is up and running")
    else:
        print("yahoo is down")
    if ret3 == 0:
        print("bbc is up and running")
    else:
        print("bbc is down")
    if ret4 == 0:
        print("iuwybacrioweuaj is up and running")
    else:
        print("iuwybacrioweuaj is down")
    if ret5 == 0:
        print("youtube is up and running")
    else:
        print("youtube is down")


schedule.every(10).seconds.do(job234)
while True:
    schedule.run_pending()
    time.sleep(10)