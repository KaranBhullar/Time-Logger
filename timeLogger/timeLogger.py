import argparse
import math
import time

def format(startTime: float, stopTime: float, log:str = "") -> str:
    time = stopTime - startTime
    hours = int(time / 3600)
    minutes = int(time / 60)
    seconds = int(time % 60)

    return(log + " | " + str(hours).strip() + ":" + str(minutes).strip() + ":" + str(seconds).strip())

def calcStartTime() -> float:
    f = open("time.txt", "r")
    try:
        startTime = float(f.readline().split(",")[1])
    except:
        startTime = float("NaN")
    return startTime
    
def readTime():
    f = open("time.txt", "r").read()
    times = f.split("\n")

    for line in times[0:len(times)-1]:
        piece = line.split(",")
        startTime = calcStartTime()
        #formats log and time into an easily readable string
        print(format(startTime, float(piece[1]), f"{piece[0]: <{str(len(max(times, key=len)) - 16)}}"))

def stop():
    stopTime = time.time()
    startTime = calcStartTime()
    if math.isnan(startTime):
        print("To stop the timer you must start it first. To start the timer type -s or --start")
        return
    sendTime("End", stopTime)
    readTime()
    open("time.txt", "w").close()

def sendTime(log: str, time: float):
    f = open("time.txt", "a")
    f.write (f"{log},{time}\n")
    f.close()

def main():
    parser = argparse.ArgumentParser(prog='Time Logger', description='A simple Command Line Interface that can log your time.')
    toggle = parser.add_mutually_exclusive_group()

    toggle.add_argument('-s', '--start', action="store_true")
    toggle.add_argument('-e', '--stop', action="store_true")
    parser.add_argument('-l', '--log', type=str)
    toggle.add_argument('-c', '--crump', action="store_true")
    args = parser.parse_args()

    if (args.start):
        # print(time.ctime(time.time()))
        startTime = time.time()
        sendTime("Start", startTime)
        
    elif (args.stop):
        stop()

    if bool(args.log):
        stopTime = time.time()
        startTime = calcStartTime()

        if not math.isnan(startTime):
            sendTime(args.log, stopTime)
        else:
            print("You must start the timer before you can log. To start the timer type -s or --start")

