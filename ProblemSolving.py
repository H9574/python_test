#Räisänen Sanna 2.12.2016 klo 13:03

# Problem solving
# Create a function that solves the most suitable (with most power) link station
# for a device at given point [x,y]. Use any programming language of your choice.
#
# This problem can be solved in 2-dimensional space. Link stations have reach
# and power.
#
# A link station’s power can be calculated: 
# power = (reach - device's distance from link station)^2
# if distance > reach, power = 0
#
# Function receives list of link stations and the point where the device is
# located.
#
# Function should output following line:
# “Best link station for point x,y is x,y with power z”
# Or:
# “No link station within reach for point x,y”
#
# Link stations are located at points (x, y) and have reach (r) ([x, y, r]):
# [[0, 0, 10],
# [20, 20, 5],
# [10, 0, 12]]
#
# Print out function output from points
# (x, y): (0,0), (100, 100), (15,10) and (18, 18).

import math

class station_power:
    def __init__(self, point, stations):
        self.point = point
        self.stations = stations

    def return_point(self):
        return self.point

    def return_stations(self):
        return self.station

    def find(self,lookfor, where):
        for index, item in enumerate(where):
            if lookfor in item: 
                return item

    def calculate_distance_and_power(self,point,stations):
        elements = len(stations)
        helplist=[]
        helppower=[]
        i = 0
        px = point[0]
        py = point[1]
        reach = stations[i][2]
        while(i<elements):
            sx = stations[i][0]
            sy = stations[i][1]
            #print("station ",sx,sy)
            i = i+1
            distance = math.sqrt(math.pow(px - sx,2)+math.pow(py - sy,2))
            power = math.pow(reach - distance,2)
            if distance > reach:
                power = 0
            helplist.append([point,i,power])
            helppower.append(power)
        #print("helplist ",helplist)
        #print("all powers ",helppower)
        max_power = max(helppower)
        #print("maxpower ",max_power)
        answerlist = station_power.find(self,max_power,helplist)
        return answerlist

    def answer(self,answerlist):
        #print("answerlist ",answerlist)
        point = answerlist[0]
        station_index = answerlist[1]
        station = stations[station_index]
        power = answerlist[2]
        if (power != 0):
            print('Best link station for point ',point,' is ',station,' with power ', power)
        else:
            print('No link station within reach for point ', point)

stations = [[0, 0, 10], [20, 20, 5], [10, 0, 12]]
self = [[0,0],[[0, 0, 10], [20, 20, 5], [10, 0, 12]]]
#Test objects
piste1 = [0,0]
piste2 = [100,100]
piste3 = [15,10]
piste4 = (18,18)


eka = station_power.calculate_distance_and_power(self,piste1,stations,)
station_power.answer(self,eka)

toka = station_power.calculate_distance_and_power(self,piste2,stations)
station_power.answer(self,toka)

kolmas = station_power.calculate_distance_and_power(self,piste3,stations)
station_power.answer(self,kolmas)

neljas = station_power.calculate_distance_and_power(self,piste4,stations)
station_power.answer(self,neljas)

#koodaamisen lopetus klo 14:33
