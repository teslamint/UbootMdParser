#!/usr/bin/python2
import sys, getopt, binascii

def main(argv):
	inputfile = ' '
	outputfile = ' '
	try:
		opts, args = getopt.getopt(argv, "hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'ubootParse.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'ubootParse.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i"):
			inputfile = arg
		elif opt in ("-o"):
			outputfile = arg
		print inputfile
		print outputfile
		timeToParse(inputfile, outputfile)

def timeToParse(input, output):
	f = open(input, 'r')
	outfile = open(output, 'w')
	while True:
		line = f.readline()
		if not line: break
		print line[0:9]
		hextoParse = line[10:18] + line[19:27] + line[28:36] + line[37:45] + line[46:57]
		#hextoParse.replace(' ','')
		print hextoParse
		b_s = binascii.unhexlify(''.join(hextoParse.split()))
		outfile.write(b_s)
	outfile.close()
	f.close()
	print "Finished parsing, now exiting..."

if __name__ == "__main__":
	main(sys.argv[1:])
