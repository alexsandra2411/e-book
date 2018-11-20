import wx
import gui
import xml.etree.cElementTree as ET
from Book import Book
import database

BOOK_PATH = 'loader/resource/book4.xml'
STATUS_BAR_WIDTH = 300
STATUS_BAR_HEIGHT = 25
STATUS_BAR_POSITION = 0


CONTENT_WIDTH = 350
CONTENT_HEIGHT = 600


class General:
    def __init__(self):
        self.Login = LoginPanelClass(None)

class LoginPanelClass(gui.LoginPanel):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        gui.LoginPanel.__init__(self,parent)

    def LoginPanelLoginButtonClick( self, event ):
        login = self.MainFrameLoginInput.GetValue();
        password = self.MainFramePasswordInput.GetValue();
        auth = database.auth(login, password);
        if auth == True:
            M = MainPanelClass(None)
            M.Show(True)
            self.Close(True)


    def RegisterPanelLoginButtonClick(self, event):
        login = self.MainFrameLoginInput.GetValue();
        password = self.MainFramePasswordInput.GetValue();
        database.create_user(login, password)

    def MainFrameAnonymLoginButtonClick(self,event):
        print "ololol"
        M = MainPanelClass(None)
        M.Show(True)
        self.Close(True)



class MainPanelClass(gui.MainFrame):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        gui.MainFrame.__init__(self,parent)
        self.initValues()

    def OnLeftClick(self, evt):
        t= evt.GetEventObject()
        treeItem = t.GetItemData(evt.GetItem())
        component = None
        if treeItem is not None:
            component = treeItem.GetData()
            name = component.name if component.name is not None else ""
            content = component.content if component.content is not None else ""
            if component.content is not None: #or component.name is not None:
                self.Content.SetValue(name + content)
            ####
            if len(component.questionList) > 0:
                print "******************************"
                self.mQuestionList = component.questionList
            self.updateView()
            ####
            if database.get_user() is not None:
                database.HistoryItemDB(database.ACTION_TYPESDB.SECTION, component.name, component.name, database.get_user()["login"]).save()

    def GetItemText(self,tree, item):
        if item:
            return tree.GetItemText(item)
        else:
            return ""
    def initValues(self):

        BOOK_TREE = ET.ElementTree(file=BOOK_PATH)
        BOOK_INSTANCE = Book(BOOK_TREE,self, BOOK_PATH)


        self.MainFrameCatalogPanelFrame = wx.TextCtrl(frame,value=BOOK_INSTANCE.getTitle())
        user = database.get_user()
        login = "Anonymous" if user is None else user["login"]
        self.Status = wx.TextCtrl( self.Status , value=" You`ve logged in as " + login, size=( STATUS_BAR_WIDTH , STATUS_BAR_HEIGHT ), pos=(STATUS_BAR_POSITION , -1))
        self.Questions = wx.TextCtrl( self.MainFrameMainPanelHistorySubPanel , value="", size =(350, 300) , pos=(STATUS_BAR_POSITION , -1))

        self.Content = wx.TextCtrl (self.MainFrameMainPanelBookSubPanel,value=BOOK_INSTANCE.foreward, size=(CONTENT_WIDTH,CONTENT_HEIGHT), style=wx.TE_READONLY|wx.TE_MULTILINE)



app = wx.App(False)
frame = LoginPanelClass(None)
frame.Show(True)



app.MainLoop()
