import csv
from operator import itemgetter
import time


def sort_file(infile, outfile, column): # sort a file based on the given column
   reader = csv.reader(open(infile), delimiter="\t")
   #next(reader)
   f = open(outfile,'w')
   for line in sorted(reader, key = lambda x: float(itemgetter(column)(x))):
      for item in line:
         f.write("%s\t" % item)
      f.write("\n")

sort_file("transformed.txt", "transformed_sorted.txt",0)
