# -*- coding: utf-8 -*-


from pyspark import SparkContext
import sys


def main(infilename, outfilename):
    with SparkContext() as sc:
        sc.setLogLevel("ERROR")
        data = sc.textFile(infilename)
        words_rdd = data.map(lambda y: y.slipt())
        with open(outfilename, 'w') as outfile:
            outfile.write('RESULTS------------------')
            outfile.write('número de palabras: '+ str(words_rdd.sum()))
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 {0} <infilename> <outfilename>".format(sys.argv[0]))
    else:
        main(sys.argv[1], sys.argv[2])

"""

from pyspark import SparkContext
import sys


def main(filename):
    with SparkContext() as sc:
        sc.setLogLevel("ERROR")
        data = sc.textFile(filename)
        words_rdd = data.map(lambda x: len(x.split()))
        print (words_rdd.collect())
        print ('RESULTS------------------')
        print ('words_count', words_rdd.sum())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 {0} <file>".format(sys.argv[0]))
    else:
        main(sys.argv[1])
"""