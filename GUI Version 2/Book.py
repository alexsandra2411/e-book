import sys
import wx
from wx._controls import TreeItemData
import database
TREE_WIDTH = 300
TREE_HEIGHT = 500
sys.path.append('question')
from gui import Question

class Component():
    def _init_(self):
        self.content =''
        self.list =[]
        self.name =''
        self.questionList = []


    def setValues(self, _content, _name, list):
        self.content = _content
        self.name = _name
        self.list = list






class Book:
    def setvalues(self, title,authors, date,content,contents,foreward):
        self.title = title
        self.authors = authors
        self.date = date
        self.content = content
        self.sections = contents
        self.list = []
        self.foreward = foreward



    def __init__(self,book,frame, bookPath):
        self.tree_ctrl = None
        self.initBook(book,frame)
        if database.get_user() is not None:
            database.HistoryItemDB(database.ACTION_TYPESDB.BOOK, bookPath, self.title, database.get_user()["login"]).save()


    def getTitle(self):
        return self.title

    def getDate(self):
        return self.date


    def getAuthors(self):
        for a in self.authors:
            ""
            #print a

    def getContents(self):
        for a in self.contents:
            ""
            ##print a

    def getSections(self):
        #for s in sections:
           # #print s
        self.processTree(self.sections)

    def getMap(self):
        for items in map:
            #print items
            for sub_items in map[items]:
                ""
                #print sub_items

    def getLeafElement (self, elem):
        list = []
        title =""
        content =""
        questionList = []
        ##print elem
        if elem.tag == 'sub_item' or  elem.tag == 'content':
            ##print elem.text
            for e in elem:
                if e.tag == 'item_title':
                    title = e.text.strip()

                elif e.tag == 'text':
                    if e != 'NoneType':
                        content = e.text

                elif e.tag == 'questions':
                    for ques in e:
                        qText = ""
                        answers = {}
                        for q in ques:
                            if q.tag == 'text':
                                qText = q.text.strip()
                            elif q.tag == 'answers':
                                for a in q:
                                    answers[a.text.strip()] = 'True' if a.tag == 'right' else 'False'

                        questionList.append(Question(qText, answers))

                elif e.tag == 'sub_item':
                    ##print "call function:"+e.tag
                    list.append(self.getLeafElement(e))


        c = Component()
        c.name = title
        c.content = content
        c.list = list
        c.questionList = questionList

        return c



    def initBook(self, treeObject,frame):
        title = ''
        date = ''
        authors =[]
        sections = []
        contents = []
        foreward = ''

        for elem in treeObject.iter():
            result =[]
                ##print " ****** "+elem.tag + " ********"
            if elem.tag =='title':
                self.title = elem.text.strip()
            if elem.tag =='date':
                date = elem.text.strip()
                    ##print "date :" +date
            if elem.tag == 'author':
                    ##print "#### "+elem.text.strip()
                authors.append(elem.text.strip())
            if elem.tag == 'foreward':
                foreward = elem.text.strip()

            if elem.tag == 'content':
                self.letters = self.getLeafElement(elem)

        self.setvalues(title,authors,date,contents,contents,foreward)

        self.tree_ctrl = wx.TreeCtrl(frame.MainFrameCatalogPanelFrame, size=(TREE_WIDTH,TREE_HEIGHT), style= wx.TR_FULL_ROW_HIGHLIGHT )#\
        self.tree_ctrl.Bind(wx.EVT_TREE_SEL_CHANGED, frame.OnLeftClick,self.tree_ctrl)
        root = self.tree_ctrl.AddRoot(self.title)
        ##print self.letters
        self.define_tree(root, self.letters)
        self.tree_ctrl.ExpandAll()

    def define_tree(self, parent, component):
        #print component
        temp =TreeItemData()
        temp.SetData(component)
        #print temp.GetData()
        item = self.tree_ctrl.AppendItem(parent, component.name, -1, -1, temp)
        for a in component.list:
            self.define_tree(item, a)


