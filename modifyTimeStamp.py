import argparse
    
TIMESTAMP_INDICATOR = " --> "

def modifyTimeStamp(stamp, offset):
    print "Old: " + stamp
    segs = stamp.split(",")
    times = segs[0].split(":")
    hours = int(times[0])
    mins = int(times[1])
    secs = int(times[2])
   
    minsToCarry = (secs + offset) / 60
    secs = (secs + offset) % 60

    hoursToCarry = (minsToCarry + mins) / 60
    mins = (minsToCarry + mins) % 60

    hours = hours + hoursToCarry

    hoursStr = str(hours) if (hours >= 10) else "0" + str(hours)
    minsStr = str(mins) if (mins >= 10) else "0" + str(mins)
    secsStr = str(secs) if (secs >= 10) else "0" + str(secs)

    newStamp = hoursStr + ":" + minsStr + ":" + secsStr + "," + segs[1]
    print "New: " + newStamp
    return newStamp

def modifyTimeLine(line, offset):
    segs = line.split(TIMESTAMP_INDICATOR)
    return modifyTimeStamp(segs[0], offset) + TIMESTAMP_INDICATOR + modifyTimeStamp(segs[1], offset)


def main():
    parser = argparse.ArgumentParser(description="modify timestamp")
    parser.add_argument("-i", required=True , help="input srt filename")
    parser.add_argument("-s", required=True, help="offset in seconds")
    parser.add_argument("-o", help="output srt filename, default to output.srt", default="output.srt")
    
    args = parser.parse_args()
    
    inputFilename = args.i
    outputFilename = args.o
    secOffset = int(args.s)
    inputFile = open(inputFilename, "r") 
    outputFile = open(outputFilename, "w")

    for line in iter(inputFile):
        line = line.lstrip(" ")
        if  TIMESTAMP_INDICATOR in line:
            outputFile.write(modifyTimeLine(line, secOffset))
        else:
            outputFile.write(line)
    print "ALL done!!"

if __name__ == "__main__":
    main()

