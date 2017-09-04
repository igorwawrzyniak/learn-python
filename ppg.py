#!/usr/bin/python3

import sys
import argparse

def printfile(printname=False,printline=False,filename='stdin'):
    if printname:
        print(filename)
    lineno=1
    for line in sys.stdin:
        if printline:
            sys.stdout.write(str(lineno)+' ')
            lineno+=1
        print(line.strip('\n'))

def setargparse():
    parser=argparse.ArgumentParser(description='Primitive Python Grep.')
    parser.add_argument('-H','--with-filename', action='store_true', help='Show filename',dest='printname')
    parser.add_argument('-n', '--line-number', action='store_true', help='Show line number', dest='printline')
    parser.add_argument('-i','--input-file', action='store', help='Input file (empty for stdin)',dest='filename',default='stdin')
    return parser.parse_args()

args=setargparse()
printfile(printname=args.printname,printline=args.printline,filename=args.filename)
