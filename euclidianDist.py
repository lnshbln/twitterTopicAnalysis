import math
#from osgeo import ogr
#from osgeo import osr
import csv
import pyproj
from pyproj import Proj, transform







def euclidean_dist(A,B):
    sum = 0
    if len(A) == len(B):
        points = len(A)
        for i in range(points):
            sum+=math.sqrt((A[i][0]-B[i][0])**2+(A[i][1]-B[i][1])**2)
        return sum/points
    else:
        return -1


def euclidian_traj (inputFile, outFile):

    counter_user = 0
    user_coor_dict = {}  # a dictionary that stores the longitudes of all users.
    with open(inputFile) as f:
        file = f.readline()

        file = f.readlines()  # read all the lines in the weibo file
        previous_user_id = -1 # track if current user is the first user
        for j in file:
            data =j.strip('\n').split('\t')
            current_user_id = data[0] # get user id of the current row
            current_user_lon = float(data[2]) # get longitude of the current row
            current_user_lat= float(data[1]) # get latitude of the current row
            if current_user_id in user_coor_dict: # if some of this user's lat/lon have been added to the dictionary
                user_coor_dict[current_user_id].append((current_user_lon,current_user_lat)) # keep adding to the lon/lat list where the key is the user id
            else: # if this is a new user
                # create a new key
                user_coor_dict[current_user_id]= []
                # add current lat/lon as the first point of this user
                user_coor_dict[current_user_id].append((current_user_lon, current_user_lat))
                counter_user += 1
                #print('user ' + str(counter_user) + ' extracted')
            previous_user_id = current_user_id


    id1 = []
    id2 = []
    euc_dist = []
    euc_sum = 0
    euc_count = 0
    items = user_coor_dict.keys() #get all unique id
    items_corr = user_coor_dict.keys()
    for i in items: # go through each user_id
        for j in items_corr:
            if i == j: # check for a pair(eliminate zero distance)
                continue
            else:
               x = user_coor_dict.get(i) #get unique values for user in first cycle
               y = user_coor_dict.get(j) #get unique values for each user in second cycle
               eucl = euclidean_dist(x,y)
               a = float(eucl)#calculate euclidean distance
               if a != -1:
                   id1.append(i)
                   id2.append(j)
                   euc_dist.append(eucl)
                   if float(eucl)<10000:
                    euc_sum += float(eucl)
                    euc_count +=1
               else:
                   continue



        if len(items_corr) == 1: #check if second loop is not equal to 1
            break

    print (euc_sum/euc_count)



    rows = zip(id1,id2,euc_dist)

    out_file = open(outFile, 'w') # open output file
    out_file.write ("id1 id2 euc_dist\n")
    writer = csv.writer((out_file), delimiter = '\t')
    for row in rows:
        writer.writerow(row)


#euclidian_traj('transformed_sorted.txt',"transformed_euc_dist.txt")
