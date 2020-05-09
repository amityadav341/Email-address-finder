fname =input("Enter file name: ")
counter = 0
fh = open(fname)

for line in fh :
    line = line.rstrip()
    if not line.startswith('From '): continue        
    words = line.split()
    print (words[1])
    counter +=1

print ("There were", counter, "email address find from which email recieved ")