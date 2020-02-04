from math import sqrt

fileIn = open("log_ShooterTest_02_01_2020", "r")
fileOut = open("output.csv", "w")

voltage = 0.0
power = 0.0
start = False
leftlist = []
rightlist = []


def calcMean(arr):
    meanSum = 0.0
    for num in arr:
        meanSum += num
    return meanSum / len(arr)


def calcSD(arr):
    SD = 0.0
    mean = calcMean(arr)
    for num in arr:
        SD += pow(num - mean, 2)
    return sqrt(SD / len(arr))


def calculate(arr):
    # print(calcMean(arr))
    sd = calcSD(arr)
    mean = calcMean(arr)
    lower = mean - 2 * sd
    upper = mean + 2 * sd
    clone = arr[:]
    for i in range(0, len(clone)):
        try:
            if clone[i] < lower or clone[i] > upper:
                clone.pop(i)
        except:
            break

    sd = calcSD(clone)
    mean = calcMean(clone)
    lower = mean - 4 * sd
    upper = mean - 4 * sd
    clone = arr[:]
    for i in range(0, len(clone)):
        try:
            if clone[i] < lower or clone[i] > upper:
                clone.pop(i)
        except:
            break
    # print(clone)
    return calcMean(clone)


for line in fileIn:
    line = line.replace(" ", "")
    line = line.replace("\n", "")
    if "End" in line and start == True:
        start = False
        print("Power: " + str(power) + ", Voltage: " + str(voltage) + ", left avg: " + str(calculate(leftlist)) +
              ", right avg: " + str(calculate(rightlist)))
        fileOut.write(str(power) + "," + str(voltage) + "," + str(calculate(leftlist)) + "," +
                      str(calculate(rightlist)) + "\n")
        continue
    elif "ShooterPower" in line:
        power = float(line.replace("ShooterPowersetto", ""))
        start = True
        leftlist = []
        rightlist = []
        continue
    elif "Voltage" in line:
        voltage = float(line.replace("BatteryVoltage=", ""))
    elif start:
        splitLine = line.split(",")
        if splitLine[1] != "0.0":
            leftlist.append(float(splitLine[1]))
        if splitLine[2] != "0.0":
            rightlist.append(float(splitLine[2]))
    else:
        continue
