import math
#from osgeo import ogr
#from osgeo import osr
import csv
import pyproj
from pyproj import Proj, transform





def CoordTransform(input,output):

    inProj = Proj(init='epsg:4326')
    outProj = Proj(init='epsg:3857')



    longlist = []
    latlist = []
    idlist = []
    with open(input) as f:
        # icalculate the rog of all users in the provided file
        file = f.readlines()  # read all the lines in the weibo file
        previous_user_id = -1  # track if current user is the first user
        for j in file:
            data = j.strip('\n').split('\t')
            current_user_id = data[1]  # get user id of the current row
            current_user_lon = float(data[3])  # get longitude of the current row
            current_user_lat = float(data[2])  # get latitude of the current row

            idlist.append(current_user_id)
            x1,y1 = current_user_lon,current_user_lat
            x2,y2 = transform(inProj,outProj,x1,y1)


            latlist.append(y2)


            longlist.append(x2)

    rows = zip(idlist, latlist, longlist)

    out_file = open(output, 'w')  # open output file
    out_file.write("id L B\n")
    writer = csv.writer((out_file), delimiter="\t")
    for row in rows:
        writer.writerow(row)



#CoordTransform('extractedCoordinates.txt',"transformed.txt")


