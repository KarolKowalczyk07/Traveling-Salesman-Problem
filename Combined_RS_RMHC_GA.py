# The Traveling Salesman Problem consists of finding the shortest and longest paths along a set number of points (cities)
# The text file used consists of 1000 2D points seperated by a comma and space
# A random search, random mutation hill climber, and genetic algorithm were performed to find the results using the data

import numpy as np
import random as r
import matplotlib.pyplot as plt
import plotly.express as px


############# Defining the Random Search Function #################### 
def random_search():
    pointsX = []          # initialising all our variables
    pointsY = []
    X = []
    Y = []
    iterations = []
    count = 0
    dist = 0
    ndist = 700
    tdist = []
    alldist = []

    file = open(r'C:\Users\Karol\Documents\Fall 2021 Semester\Evolutionary Algorithms & Automation\HW1\tsp.txt')   # reading file tsp.txt

    for i in file:
        row = i.split(', ')
        xcoord = float(row[0])
        ycoord = float(row[1])
        pointsX.append(xcoord)
        pointsY.append(ycoord)
    

    coord = list(zip(pointsX,pointsY))     
    r.shuffle(coord)                   # random shuffling of the order of coordinates
    pointsX, pointsY = list(zip(*coord))
    length = len(coord)                 

    for i in range(0,50000):                  # setting number of iterations to 50000
        for i in range(0, length-1):

            xtemp1 = pointsX[i]
            ytemp1 = pointsY[i]
    
            if ((i+1)>(len(pointsX))):     # for closing the loop from last coordinates to first coordinates
                xtemp2 = pointsX[0]
                ytemp2 = pointsY[0]
        
            xtemp2 = pointsX[i+1]
            ytemp2 = pointsY[i+1]
    
            tempdist = np.sqrt((xtemp2-xtemp1)**2 +(ytemp2-ytemp1)**2) # calculating the distance between two consecutive points
            dist +=  tempdist
    
        iterations.append(count)
        count += 1


        if dist < ndist:                    
            ndist = dist
            tdist.append(dist)                  # collecting all the values of the distances calculated
            X, Y = pointsX, pointsY
            #print(dist)
        else:
            tdist.append(ndist)              # append shortest distance for plotting
            
        r.shuffle(coord)
        pointsX, pointsY = list(zip(*coord))

        dist = 0

    return X,Y,iterations,tdist,count




##################### Defining the Hill Climber Function ############################
def hill_climber():
    pointsX = []          # initialising all our variables
    pointsY = []
    iter = 50000
    X = []
    Y = []
    searches =  10
    iterations = []
    count = 0
    dist = 0
    ndist = 700
    tdist = []
    alldist = []
    new_distance = 0

    file = open(r'C:\Users\Karol\Documents\Fall 2021 Semester\Evolutionary Algorithms & Automation\HW1\tsp.txt')   # reading file tsp.txt

    for i in file:
        row = i.split(', ')
        xcoord = float(row[0])
        ycoord = float(row[1])
        pointsX.append(xcoord)
        pointsY.append(ycoord)
    

    coord = list(zip(pointsX,pointsY))     
    r.shuffle(coord)                   # random shuffling of the order of coordinates
    pointsX, pointsY = list(zip(*coord))
    length = len(coord)   

    pointsX = list(pointsX)
    pointsY = list(pointsY)

                 # setting number of iterations to 50000
    for i in range(0, length-1):

        xtemp1 = pointsX[i]
        ytemp1 = pointsY[i]
    
        if ((i+1)>(len(pointsX))):     # for closing the loop from last coordinates to first coordinates
            xtemp2 = pointsX[0]
            ytemp2 = pointsY[0]
        
        xtemp2 = pointsX[i+1]
        ytemp2 = pointsY[i+1]
    
        tempdist = np.sqrt((xtemp2-xtemp1)**2 +(ytemp2-ytemp1)**2) # calculating the distance between two consecutive points
        dist +=  tempdist
    
    

    print('Current distance: ', dist)
    #print(xpoints)
    distance_saved = dist



    while (count < iter):

        j = r.randrange(length)
        #print(x)
        swap1x = pointsX[j]
        swap1y = pointsY[j]

        if ((j+1) >= length):                        # If final point selected, use first point
            swap2x = pointsX[0]
            swap2y = pointsY[0]
        
            pointsX[j] = swap2x                         # swap 2 points
            pointsY[j] = swap2y
        
            pointsX[0] = swap1x
            pointsY[0] = swap1y
        else:
            swap2x = pointsX[j+1]
            swap2y = pointsY[j+1]
    
            pointsX[j] = swap2x                         # swap 2 points
            pointsY[j] = swap2y
    
            pointsX[j+1] = swap1x
            pointsY[j+1] = swap1y

        for i in range(0, length-1):                  # iterate through swapped path

            x1 = pointsX[i]
            y1 = pointsY[i]
    
            if ((i+1) >= length):                  # i is the last element
                x2 = pointsX[0]
                y2 = pointsY[0]
            else:
                x2 = pointsX[i+1]
                y2 = pointsY[i+1]

            new_path = np.sqrt((x2-x1)**2+(y2-y1)**2)            # take distance between points
            new_distance +=  new_path

        if distance_saved  < new_distance:                          # original path is shorter
            pointsX[j] = swap1x                              # undo the swap
            pointsY[j] = swap1y                             
    
            if ((j+1) >= length):                  # i is the last element
                pointsX[0] = swap2x
                pointsY[0] = swap2y
            else:
                pointsX[j+1] = swap2x
                pointsY[j+1] = swap2y

            X, Y = pointsX, pointsY
            tdist.append(distance_saved) 
            
        
        else:
            distance_saved = new_distance
            tdist.append(distance_saved)
            X, Y = pointsX, pointsY

            #print(distance_saved) 

        iterations.append(count)
        count += 1    
        new_distance = 0     

    return X,Y,iterations,tdist,count




################# Defining GA Function #####################
def genetic_algorithm():
    pointsX, pointsY = [], []          # initialising all our variables
    weightsparallel = []                        # population list of weights (list of lists)
    weightvalues = []
    keyvaluex, keyvaluey, keyvalue = [], [], []
    weightpopx, weightpopy, weightpop = [], [], []                      # list of dictionaries, having list of xvalues: weight for each individual
    weightedx, weightedy, weightedxpop, weightedypop = [], [], [], []
    population, indpop, childlist = [], [], []
    sortedx, sortedy, sortedxy = [], [], []
    indsortedx, indsortedy, indsortedxy, sortedxypop = [], [], [], []
    child, childpointsX, childpointsY, childpoints = [], [], [], []
    childrenX, childrenY = [], []
    even_numbers = []                       # counter for breeding
    xpop, ypop = [], []                     # x and y points of population
    X, Y = [], []                           # saved x,y lists for plotting
    even_numbers = []
    popcount = 10
    weightsum = 0

    iterations = []
    crossovercount = 1                   # number of crossovers (every 100 swaps)
    crossnum = 0
    iter = 50000
    count = 0
    dist = 0
    ndist = 700
    tdist = []
    alldist = []
    new_distance = 0

    file = open(r'C:\Users\Karol\Documents\Fall 2021 Semester\Evolutionary Algorithms & Automation\HW1\tsp.txt')   # reading file tsp.txt

    def distance(population, xpop, ypop, length):
        popdistances = []
        new_dist = 0
        indcount = 0
        count = 0
        for i in population:
            pointsX = xpop[indcount]
            pointsY = ypop[indcount]
            for x in range(0,length-1):

                xp1 = pointsX[x]
                yp1 = pointsY[x]
            
                xp1, yp1 = float(xp1), float(yp1)
            
                if (x+1) >= length:
                    xp2 = pointsX[0]
                    yp2 = pointsY[0]
                
                    xp2, yp2 = float(xp2), float(yp2)
                else:
                    xp2 = pointsX[x+1]
                    yp2 = pointsY[x+1]
                
                    xp2, yp2 = float(xp2), float(yp2)
                
                new_path = np.sqrt((xp2-xp1)**2+(yp2-yp1)**2)            # take distance between points
                new_dist +=  new_path
                
            popdistances.append(new_dist)
            count += 1    
            new_dist = 0

        
            indcount += 1
        
        return popdistances

    def crossover(population, length):
        popcount = len(population)
        childpoints, childpointsX, childpointsY = [], [], []
        for i in range(0,popcount-1):                     # start at second solution, to allow breeding
            if i%2 == 1:
                continue
            #print(i)
            for x in range(int(length/4)):
                childpointsX.append(weightedxpop[i][x])  # starting at first parent, go back to first parent solution
                childpointsY.append(weightedypop[i][x])
                childpoint = str(weightedxpop[i][x]) + ' ' + str(weightedypop[i][x])
                childpoints.append(childpoint)
             
            for x in range(int(length*3/4),length):           # go from point 750 to 1000 in parent 1
                childpointsX.append(weightedxpop[i][x])
                childpointsY.append(weightedypop[i][x])
                childpoint = str(weightedxpop[i][x]) + ' ' + str(weightedypop[i][x])
                childpoints.append(childpoint)
        
            for x in sortedxypop[i+1]:                      # take points from parent 2 which aren't in child
                if x in childpoints:
                    continue
                else:
                    childpoints.append(x)
                    xp1, yp1 = x.split()
                    childpointsX.append(xp1)
                    childpointsY.append(yp1)
            
            population.append(childpoints)
  
            weightedxpop.append(childpointsX)
            weightedypop.append(childpointsY)
   
            childpointsX = []
            childpointsY = []
            childpoints = []
        return population
            
            
    for i in file:
        row = i.split(', ')
        xcoord = float(row[0])
        ycoord = float(row[1])
        pointsX.append(xcoord)
        pointsY.append(ycoord)

    length = len(pointsX)  
    RSorder = list(zip(pointsX,pointsY))        # save original random search for order of points
        
    for x in range(length):
        keyvaluex.append(pointsX[x])
        keyvaluey.append(pointsY[x])
        coord = str(pointsX[x]) + ' ' + str(pointsY[x])
        keyvalue.append(coord)

    
    for i in range(popcount):
        coord = list(zip(pointsX,pointsY))     # pointsX,Y are never appended, dont have to reset
        r.shuffle(coord)                        # random shuffling of the order of coordinates
        pointsX, pointsY = list(zip(*coord)) 

        pointsX = list(pointsX)
        pointsY = list(pointsY)
    
        xpop.append(pointsX)                  # population x coordinates
        ypop.append(pointsY)
    
        coord = str(pointsX) + ' ' + str(pointsY)
  
        for i in range(0, length-1):
            xtemp1 = pointsX[i]
            ytemp1 = pointsY[i]
        
            coord = str(pointsX) + ' ' + str(pointsY)
            indpop.append(coord)
        
            weight = float("%.5f" % r.random())
            weightvalues.append(weight)
    
            if ((i+1)>(len(pointsX))):     # for closing the loop from last coordinates to first coordinates
                xtemp2 = pointsX[0]
                ytemp2 = pointsY[0]
        
            xtemp2 = pointsX[i+1]
            ytemp2 = pointsY[i+1]
    
            tempdist = np.sqrt((xtemp2-xtemp1)**2 +(ytemp2-ytemp1)**2) # calculating the distance between two consecutive points
            dist +=  tempdist
        
        coord = str(xtemp2) + ' ' + str(ytemp2)
        indpop.append(coord)
        

        population.append(indpop)
    
        indpop = []
        weight = float("%.5f" % r.random())     # add point for index 999
        weightvalues.append(weight)
      
        weightx = dict()
        weighty = dict()
        weights = dict()
        for i in range(length):
            weightx[keyvaluex[i]] = weightvalues[i]
            weighty[keyvaluey[i]] = weightvalues[i]
            weights[keyvalue[i]] = weightvalues[i]
        
        weightpopx.append(weightx)
        weightpopy.append(weighty)
        weightpop.append(weights)
   
    
    w = 0
    for x in weightpopx:
        weightpopx[w] = sorted(x.items(), key=lambda x: x[1])
        w += 1
    
    w = 0
    for x in weightpopy:
        weightpopy[w] = sorted(x.items(), key=lambda x: x[1])
        w += 1
    
    w = 0
    for x in weightpop:
        weightpop[w] = sorted(x.items(), key=lambda x: x[1])
        sortedxy.append(x.keys())
        w += 1
    
    # sort population by ascending weight
    
    for i in sortedxy:                          # extract key values (x,y coordinates) from population dictionary
        for e in i:
            indsortedxy.append(e)
            x,y = e.split()
            weightedx.append(x)
            weightedy.append(y)
            indsortedx.append(x)
            indsortedy.append(y)
        
        weightedxpop.append(weightedx)          # population x values in order of ascending weight
        weightedypop.append(weightedy)          # population y values in order of ascending weight
        sortedx.append(indsortedx)
        sortedy.append(indsortedy)
        sortedxypop.append(indsortedxy)
    
        weightedx = []
        weightedy = []
        indsortedx = []
        indsortedy = []
        indsortedxy = []
    


    for i in range(0,popcount-1):                     # start at second solution, to allow breeding
        if i%2 == 1:
            continue
        for x in range(int(length/4)):
            childpointsX.append(weightedxpop[i][x])  # starting at first parent, go back to first parent solution
            childpointsY.append(weightedypop[i][x])
            childpoint = str(weightedxpop[i][x]) + ' ' + str(weightedypop[i][x])
            childpoints.append(childpoint)
             
        for x in range(int(length*3/4),length):           # go from point 750 to 1000 in parent 1
            childpointsX.append(weightedxpop[i][x])
            childpointsY.append(weightedypop[i][x])
            childpoint = str(weightedxpop[i][x]) + ' ' + str(weightedypop[i][x])
            childpoints.append(childpoint)
        
        for x in sortedxypop[i+1]:                      # zip x and y points, compare child x and y points to parent x and y points
            if x in childpoints:
                continue
            else:
                childpoints.append(x)
                xp1, yp1 = x.split()
                childpointsX.append(xp1)
                childpointsY.append(yp1)
            
        childlist.append(childpoints)
    
        weightedxpop.append(childpointsX)
        weightedypop.append(childpointsY)

        childrenX.append(childpointsX)
        childrenY.append(childpointsY)
        child = list(zip(childpointsX, childpointsY))
    
        childpointsX = []
        childpointsY = []
        childpoints = []

    distance_saved = dist

    for i in range(0,len(childlist)):
        population.append(childlist[i])
    

    while crossnum < crossovercount:
        indcount = 0
    
        for i in population:
            while (count < iter):

                pointsX = xpop[indcount]
                pointsY = ypop[indcount]

                x = r.randrange(length)
                swap1x = pointsX[x]
                swap1y = pointsY[x]
            
                if ((x+1) >= length):                        # If final point selected, use first point
                    swap2x = pointsX[0]
                    swap2y = pointsY[0]
                
                    pointsX[x] = swap2x                         # swap 2 points
                    pointsY[x] = swap2y
                
                    pointsX[0] = swap1x
                    pointsY[0] = swap1y
                else:
                    swap2x = pointsX[x+1]
                    swap2y = pointsY[x+1]
    
                    pointsX[x] = swap2x                         # swap 2 points
                    pointsY[x] = swap2y
    
                    pointsX[x+1] = swap1x
                    pointsY[x+1] = swap1y

                for i in range(0, length-1):                  # iterate through swapped path

                    x1 = pointsX[i]
                    y1 = pointsY[i]
    
                    if ((i+1) >= length):                  # i is the last element
                        x2 = pointsX[0]
                        y2 = pointsY[0]
                    else:
                        x2 = pointsX[i+1]
                        y2 = pointsY[i+1]

                    new_path = np.sqrt((x2-x1)**2+(y2-y1)**2)            # take distance between points
                    new_distance +=  new_path

                if distance_saved  < new_distance:                          # original path is shorter
                    pointsX[x] = swap1x                              # undo the swap
                    pointsY[x] = swap1y                             
    
                    if ((x+1) >= length):                           # i is the last element
                        pointsX[0] = swap2x
                        pointsY[0] = swap2y
                    else:
                        pointsX[x+1] = swap2x
                        pointsY[x+1] = swap2y

                        X, Y = pointsX, pointsY
                        tdist.append(distance_saved) 
        
                else:
                    distance_saved = new_distance
                    tdist.append(distance_saved)
                    X, Y = pointsX, pointsY
            
                # Change individual solution in population list
                newpoints = []
                for e in range(0,length):
                    xp = X[e]
                    yp = Y[e]
                    point = str(xp) + ' ' + str(yp)
                    newpoints.append(point)
            
                population[indcount] = newpoints[:]
            
                iterations.append(count)
                count += 1    
                new_distance = 0
                dist = 0
            
                sorteddistances = []
                distorder = []
                indcounter = 0
            
                if count % 100 == 0:
                    popdistances = distance(population, weightedxpop, weightedypop, length)
                    sorteddistances = sorted(range(len(popdistances)), key=lambda k: popdistances[k])
                
                    for i in range(0, 5):
                        del population[int(sorteddistances[i])]
        
                    newpopulation = crossover(population, length)

                

       
            indcount += 1
        
        newdistances = []
        crossnum += 1

    print(distance_saved)

    missing = len(iterations) - len(tdist)

    for i in range(0,missing):
        tdist.append(distance_saved)
    
    return X,Y,iterations,tdist

####### Calling the Functions ########## 
RS_X, RS_Y, RS_iterations, RS_tdist, count = random_search()
HC_X, HC_Y, HC_iterations, HC_tdist, count = hill_climber()
GA_X, GA_Y, GA_iterations, GA_tdist = genetic_algorithm()

#print(RS_iterations)
#print(HC_iterations)
print(count)

RS_yval = []
HC_yval = []
RS_stdss = []
HC_stdss = []
GA_yval = []
GA_stdss = []




############ Calculating the errors for each method ##############
for i in range(0,int(count/10)-1):
    RS_stdss.append(RS_tdist[i])

RS_std = np.std(RS_stdss)
print(RS_std)
RS_error = 50*(RS_std/(np.sqrt(count)))
print(RS_error)

xval = np.arange(0.1,count,count/10)
for i in range(count):
    if i % (count/10) == 0:
        RS_yval.append(RS_tdist[i])


HC_std = np.std(HC_tdist)
print(HC_std)
HC_error = 20*(HC_std/(np.sqrt(count)))
print(HC_error)
for i in range(count):
    if i % (count/10) == 0:
        HC_yval.append(HC_tdist[i])


for i in range(0,int(count/10)-1):
    GA_stdss.append(GA_tdist[i])

GA_std = np.std(GA_stdss)
print(GA_std)
GA_error = 20*(GA_std/(np.sqrt(count)))
print(GA_error)

for i in range(count):
    if i % (count/10) == 0:
        GA_yval.append(GA_tdist[i])      


########### Plotting Graphs ################
plt.figure(1)             # plotting the graph of No. of Iterations vs The Values of calculated distances
plt.plot(RS_iterations,RS_tdist,label="RS")
plt.errorbar(xval,RS_yval,yerr=RS_error,linestyle='')
plt.plot(HC_iterations,HC_tdist,label="RMHC")
plt.errorbar(xval,HC_yval,yerr=HC_error,linestyle='')
plt.plot(GA_iterations,GA_tdist,label="GA")
plt.errorbar(xval,GA_yval,yerr=GA_error,linestyle='')
plt.title('No. of Iterations vs Distance Values')
plt.xlabel('Iterations')
plt.ylabel('Distance')
plt.legend()
plt.show()

RS_dot = px.scatter(x=RS_iterations,y=RS_tdist)   # random search dot plot
#RS_dot.show()

HC_dot = px.scatter(x=HC_iterations,y=HC_tdist)   # hill climber dot plot
#HC_dot.show()

GA_dot = px.scatter(x=GA_iterations,y=GA_tdist)
GA_dot.show()

###### plotting bar graph #######
RS_shortestdist = RS_tdist[-1]
HC_shortestdist = HC_tdist[-1]
GA_shortestdist = GA_tdist[-1]
x_bar = ["RS","HC","GA"]
y_bar = [RS_shortestdist,HC_shortestdist,GA_shortestdist]
bar_fig = plt.figure(figsize = (5,6))
plt.bar(x_bar,y_bar,width = 0.4)
plt.xlabel("Algorithms")
plt.ylabel("Shortest Distance Values")
plt.title("Shortest Distance Comparison")
plt.show()

