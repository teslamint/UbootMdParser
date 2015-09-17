# UBootMdParser
This is a script written in python which will allow a user to parse a memory dump from U-Boot and create a binary from it

Format: python2 -i inputfile -o outputfile

Step 1: Connect to the specific device over UART or another serial interface and make sure the session is saved to a text file

Step 2: Get into a U-Boot shell

Step 3: Use "printenv" to see the specific memory locations you would like to dump

Step 4: Use "md" + the memory location you would like + the amount of memory you would like to dump

Step 5: Watch the hex go by
  
Step 6: Once the dump is complete, open the text file and get rid of the stuff that is not the memory dump (i.e. everything up to and including the "md" command)

Step 7: Run the script with the input file as the session text file, and the output file being whatever you want

Step 8: If none of this failed, then you have successfully created a binary from a U-Boot memory dump!
