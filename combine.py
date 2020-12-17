import os
import struct
import sys
os.remove("vpk.bin")
in_file = open(sys.argv[1], 'rb')
out_file = open("vpk.bin", "wb")
data = in_file.read()
out_file.write(data)
filename = os.path.splitext(os.path.basename(in_file.name))[0]
cardname = (filename + ".bin")
print("{} done".format(cardname))
counter = 1
counter = str(counter) 
cardname = (filename + counter + ".bin")
while os.path.isfile(cardname):
    nextcard = open(cardname, 'rb')
    nextcard.seek(81)
    data = nextcard.read()
    out_file.write(data)
    print("{} done".format(cardname))
    counter = int(counter) 
    counter += 1
    counter = str(counter)
    cardname = (filename + counter + ".bin")
    nextcard.close()
else:
    print("Finished after {} files.\nMade by Revvy".format(counter))
    in_file.close()
    out_file.close()