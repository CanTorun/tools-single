import sys
from datetime import date

#SetVariables
n = len(sys.argv) #for debug
debug = True #debug
#conf
Tr2En = str.maketrans("ığüşöç", "igusoc")
path = './content/post/'    

#env
title  = sys.argv[1]
date = date.today()
date = date.strftime("%Y-%m-%d")
body = sys.argv[2]
content = ""

#prepare file
file = title.lower()
file = file.replace(" ", "-") 
file = file.replace("#", "")
file = file.translate(Tr2En)
file = path + file + ".md" 

#Make frontmatter
if( title.startswith("#")): #if auto
    title = title.replace("#","")
    content += "+++"
    content += "\ntitle = " + title
    content += "\ndate = " + date
    content += "\n+++\n"
else:
    exit("Pre frontmatter not supported! Aborting!") #FIX ME


#body FIX ME
content += body

with open(file, mode = 'w', encoding = 'utf-8' ) as buffer:
    buffer.write(content)
    print("Succes! " + file + " generated")

if( debug ):
    print("\n\n<--->DEBUG")
    print("total args passed: ",n)
    print("\nname of python script:",sys.argv[0])
    print("Today's date:", date)
    print("File name: ",file)
    print("Title: ",title)
    print("Body: ",body)
    print("\n---\nContent is\n ", content)

