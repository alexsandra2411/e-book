class Book:
    def __init__(self, title,authors, date,content,contents):
        self.title = title
        self.authors = authors
        self.date = date
        self.content = content
        #self.contents = contents

    def getDate(self):
        print self.date


    def getAuthors(self):
        for a in self.authors:
            print a

    def getContents(self):
        for a in self.contents:
            ""
            #print a

    def getSections(self):
        #for s in sections:
           # print s
        processTree(self.sections)

    def getMap(self):
        for items in map:
            print items
            for sub_items in map[items]:
                print sub_items


def processTree(elem):

        #print len(elem)
    for e in elem:

        if (e.tag == 'item_content'):
            #print "*************************"
            #print e.tag
            if type(e.text) != "NoneType":

                if (e.text!=None):
                    print e.text
                    #contents.append(e.text.strip())
            #print e.text.strip()
        if (e.tag != 'page'):

			#print (e.text.strip())
            list.append(e.text.strip())
        temp = e.getchildren()
        temp_list = []
        #print temp
        if (len(temp)!= 0 ):
            processTree(e)
