

def savefile():

#write to file:
    with open("isobel.txt", "a") as text_file:
        message=input("What is your message?")
        print(message, file=text_file)

# Read that file:
    infile= open("isobel.txt","r")
    data= infile.read()
    #print(data)
    #or, tell the doc to not end with a newline char:
    print(data, end="")




savefile()