import sys
import re

def main():
    # for line in fileinput.input():
    #         line = line.strip()
	f = open(sys.argv[1],"w") # writes to input txt file
	f.write("test")
    # f.close()
    # while (contents != -1):
    #     print(contents)
    
	f = open(sys.argv[1], "r") # reads to input txt file
	print(f.read())
    # f.close()
	
	f = open(sys.argv[2],"w") # writes to input txt file
	f.write("testPython") # this will be the translated version of the text file
    # f.close()
	
	f = open(sys.argv[2], "r") # reads to input txt file
	print(f.read())
	
	f.close()
	return True

main()