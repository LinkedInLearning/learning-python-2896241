# Solution to programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import os

totalbytes = 0

# get a list of all the files in the current directory
dirlist = os.listdir()
for entry in dirlist:
    # make sure it's a file!
    if os.path.isfile(entry):
        # add the file size to the total
        filesize = os.path.getsize(entry)
        totalbytes += filesize

# create a subdirectory called "results"
os.mkdir("results")

# create the output file
resultsfile = open("results/results.txt", "w+")
if resultsfile.mode == "w+":
    resultsfile.write("Total bytecount:" + str(totalbytes) + "\n")
    resultsfile.write("Files list:\n")
    resultsfile.write("--------------\n")
    # write the results into the file
    for entry in dirlist:
        if os.path.isfile(entry):
            # write the file name to the results ledger
            resultsfile.write(entry + "\n")

    # close the file when done
    resultsfile.close()
