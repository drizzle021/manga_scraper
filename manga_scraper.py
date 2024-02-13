import requests
import re
import os

# get working directory
parentDir = os.getcwd()

# ask for input from user
mainDir = input("Manga Name: ") # will be used for folder name
url = input("url to chapter 1 from Manganelo.tv: ") # might or might not work with other sites heheh
startingChapter = int(input("Starting Chapter: "))
chapters = int(input("Number of chapters: "))   # inclusive



# create new directory for saving the chapters
path = os.path.join(parentDir,mainDir)
os.mkdir(path)

for i in range(chapters):
    # edit the url to get the chapters
    url = url[:url.index("/chapter-")+9]+str(i+1)
    print(url)

    # make new directory for each chapter
    parentDir = path
    chapterDir = "Chapter"+str(i+1)
    chapterPath = os.path.join(parentDir,chapterDir)
    os.mkdir(chapterPath)

    # get the HTML
    r = requests.get(url)

    #print(r.text.index('<div class="container-chapter-reader">'))

    # clean up the HTML, remove redundant parts
    text = r.text[r.text.index('<div class="container-chapter-reader">'):]
    text = text[:text.index('</div>')]

    # find all jpgs with regex
    matches = re.findall('data-src="(.*)\\.jpg"',text)


    # for each match download the jpg and save it
    for k,match in enumerate(matches):
        response = requests.get(match+".jpg")
        with open(chapterPath+"/page_"+str(k+1)+".jpg","wb") as jpgSrc:
            jpgSrc.write(response.content)
    




