import argparse
import time

parser = argparse.ArgumentParser(prog='Time Logger', description='A simple Command Line Interface that can log your time.')
toggle = parser.add_mutually_exclusive_group()

toggle.add_argument('-s', '--start', action="store_true")
toggle.add_argument('-e', '--stop', action="store_true")
parser.add_argument('-l', '--log', type=str)
args = parser.parse_args()

if (args.start):
    # print(time.ctime(time.time()))
    f = open("time.txt", "w")
    f.write(f"{time.time()} \n")
    f.close()
elif (args.stop):
    stopTime = time.time()
    f = open("time.txt", "r")
    startTime = float(f.readline())

    time = stopTime - startTime
    hours = int(time / 3600)
    minutes = int(time / 60)
    seconds = int(time % 60)

    print(str(hours).strip() + ":" + str(minutes).strip() + ":" + str(seconds).strip())
