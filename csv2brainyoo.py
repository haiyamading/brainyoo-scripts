# -*- coding: utf-8; -*-
# csv2brainyoo.py converts CSV files into the Brainyoo XML format.
# Copyright (C) 2014  monte <at> mibix.de
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import os
import sys
import getopt
import csv

def main(argv):                         
    input   = None
    output  = None
    mapping = "qah"
    try:                                
        opts, args = getopt.getopt(argv, "hi:o:m:t:", ["help", "input=", "output=", "mapping=", "type="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg 
        elif opt in ("-o", "--output"):
            output = arg 
        elif opt in ("-m", "--mapping"):
            mapping = arg 
            
    if input == None or output == None:
        usage()
        exit(3)
        
    print
    print 'Input:   ', input
    print 'Output:  ', output
    print 'Mapping: ', mapping
    print
    csv2brainyoo( input, output, mapping )
            
def usage():
    print '-h,--help'
    print '-i,--input=file.csv'
    print '-o,--output=file.xml'
    print '-m,--mapping=qahi (question, answer, hint, ignore)'

def csv2brainyoo( input, output, mapping ) :
    map      = parseMapping( mapping )
    data     = readCSV( input, map )
    xml_data = generateXML( data )
    
    writeXML( output, xml_data )
   


def parseMapping( mapping ) :
    map = {}
    map['q'] = mapping.index( "q" )
    map['a'] = mapping.index( "a" )
    map['h'] = mapping.index( "h" )
    return map
    
def readCSV( input, map ) :
    csvfile = open(input, 'rb')
    rows = csv.reader(csvfile, delimiter=',', quotechar='\"')
    data =  [{ "question": row[map['q']], "answer":row[map['a']], "hint":row[map['h']] } for row in rows ]
    
    return data
    
def generateXML(  data ) :
    #for dict in data :
    #    print dict["question"], ",",
    #    print dict["answer"],   ",",
    #    print dict["hint"],     ","
    return None
    
    
def writeXML( output, xml_data ) :
    text_file = open(output, "w")
    text_file.write( xml_data )
    text_file.close()

    
if __name__ == "__main__":
    main(sys.argv[1:])
