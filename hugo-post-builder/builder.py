# Hugo post builder by Can Torun
# version : Beta-V2.0
import os
from datetime import date



# Configuration variables
Tr2En = str.maketrans("ığüşöç", "igusoc")
path = './content/post/'
debug = True #debug
log = list()

# Get values from env from runner
title  = os.environ['POST_TITLE']
body = os.environ['POST_BODY']
#Set Date
date = date.today()
date = date.strftime("%Y-%m-%d")
#Set content
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
    content += "\ntitle = \"" + title + "\""
    content += "\ndate = \"" + date + "\""
    content += "\n+++\n"


#body FIX ME!
content += body
content.replace("\n","\n")

with open(file, mode = 'w', encoding = 'utf-8' ) as buffer:
    buffer.write(content)
    log.append("[OK] Succes! " + file + " generated.")

if( debug ):
    log.append("[VAR](file): " + file)
    log.append("[VAR](date): " + date)
    log.append("[VAR](title): " + title)
    log.append("[VAR](body): " + body)
    log.append("[VAR](content): " + content)
    print(log)
