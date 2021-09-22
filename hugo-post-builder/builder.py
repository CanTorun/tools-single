# Hugo post builder by Can Torun
# version : Beta-V2.0
import os
from datetime import date



# Configuration variables
Tr2En = str.maketrans("ığüşöç", "igusoc")
path = './content/post/'
debug = True #debug
local = False
log = list()

# Get values from env from runner
if local:
    log.append("[INF] Debug mode is active, reading from files.")
    with open("title", mode = 'r', encoding = 'utf-8' ) as buffer:
        title = buffer.read()
        log.append("[OK] title read. ")
        buffer.close()
    with open("body", mode = 'r', encoding = 'utf-8' ) as buffer:
        body = buffer.read()
        log.append("[OK] body read. ") 
        buffer.close()
else:
    title  = os.environ['POST_TITLE']
    body = os.environ['POST_BODY']
#Set Date
date = date.today()
date = date.strftime("%Y-%m-%d")
#Set content
content = ""


#prepare file
if local:
    file = title.lower()
    file = file.replace(" ", "-")
    file = file.replace("\n", "") 
    file = file.replace("#", "")
    file = file.translate(Tr2En)
    file = file + ".md" 
else:
    file = title.lower()
    file = file.replace(" ", "-")
    file = file.replace("\n", "") 
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
else :
    content = body

with open(file, mode = 'w', encoding = 'utf-8' ) as buffer:
    buffer.write(content)
    log.append("[OK] Succes! " + file + " generated.")

if( debug ):
    log.append("[VAR](file): " + file)
    log.append("[VAR](date): " + date)
    log.append("[VAR](title): " + title)
    log.append("[VAR](body): " + body)
    log.append("[VAR](content): " + content)
    if local:
        for line in log:
            print(line)
    else:
        print(log)
