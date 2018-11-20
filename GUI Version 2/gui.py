# -*- coding: utf-8 -*- 
import wx
import wx.xrc

class Question:
    def __init__(self,iQuestion,iAnswers):
        self.mQuestion = iQuestion
        self.mAnswers = iAnswers
        self.mUserAnswers = iAnswers.copy()
        for answer in self.mUserAnswers:
            self.mUserAnswers[answer] = False

    def getQuestion(self):
        return self.mQuestion

    def getAnswers(self):
        return self.mAnswers

    def getUserAnswers(self):
        return self.mUserAnswers

    def getQuestionResult(self):
        #result for each question is calculated here!
        #one may change result-computing algorithm here:
        result = 0
        for key in self.mUserAnswers:
            if self.mUserAnswers[key] == True and self.mAnswers[key] == True:
                result += 1
            if self.mUserAnswers[key] == True and self.mAnswers[key] == False:
                result -= 1
        return result

class LoginPanel(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Welcome to GliBook!", pos=wx.DefaultPosition,
                          size=wx.Size(200, 136),
                          style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.MainFrameLoginLabel = wx.StaticText(self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0)
        self.MainFrameLoginLabel.Wrap(-1)
        gSizer1.Add(self.MainFrameLoginLabel, 0, wx.ALL, 5)

        self.MainFrameLoginInput = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(85, 20), 0)
        gSizer1.Add(self.MainFrameLoginInput, 0, wx.ALL, 5)

        self.MainFramePasswordLabel = wx.StaticText(self, wx.ID_ANY, u"Password", wx.Point(15, 90), wx.DefaultSize, 0)
        self.MainFramePasswordLabel.Wrap(-1)
        gSizer1.Add(self.MainFramePasswordLabel, 0, wx.ALL, 5)

        self.MainFramePasswordInput = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.Point(15, -1), wx.Size(85, 20), 0)
        gSizer1.Add(self.MainFramePasswordInput, 0, wx.ALL, 5)

        self.MainFrameLoginButton = wx.Button(self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.MainFrameLoginButton, 0, wx.ALL, 5)

        self.MainFrameRegistryButton = wx.Button(self, wx.ID_ANY, u"Registration", wx.DefaultPosition, wx.DefaultSize,
                                                 0)
        gSizer1.Add(self.MainFrameRegistryButton, 0, wx.ALL, 5)

        self.MainFrameAnonymLoginButton = wx.Button(self, wx.ID_ANY, u"Anonymous", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.MainFrameAnonymLoginButton, 0, wx.ALL, 5)

        self.SetSizer(gSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.MainFrameLoginButton.Bind(wx.EVT_BUTTON, self.LoginPanelLoginButtonClick)
        self.MainFrameRegistryButton.Bind(wx.EVT_BUTTON, self.RegisterPanelLoginButtonClick)
        self.MainFrameAnonymLoginButton.Bind(wx.EVT_BUTTON, self.MainFrameAnonymLoginButtonClick)

    def __del__(self):
        pass


    # Virtual event handlers, overide them in your derived class
    def LoginPanelLoginButtonClick(self, event):
        event.Skip()

    def RegisterPanelLoginButtonClick(self, event):
        event.Skip()

    def MainFrameAnonymLoginButtonClick(self, event):
        event.Skip()


class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"GliBook", pos=wx.DefaultPosition, size=wx.Size(1000, 593),
                          style=wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_SHAPED | wx.FRAME_TOOL_WINDOW | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.STAY_ON_TOP | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL)
        #1101
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        MainFrameSizer = wx.GridBagSizer(0, 0)
        MainFrameSizer.SetFlexibleDirection(wx.BOTH)
        MainFrameSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        MainFrameCatalogPanel = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Catalog"), wx.VERTICAL)

        MainFrameCatalogPanel.SetMinSize(wx.Size(250, 500))
        self.MainFrameCatalogPanelFrame = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.MainFrameCatalogPanelFrame.SetExtraStyle(
            wx.WS_EX_BLOCK_EVENTS | wx.WS_EX_PROCESS_IDLE | wx.WS_EX_PROCESS_UI_UPDATES | wx.WS_EX_VALIDATE_RECURSIVELY)
        self.MainFrameCatalogPanelFrame.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))
        self.MainFrameCatalogPanelFrame.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        MainFrameCatalogPanel.Add(self.MainFrameCatalogPanelFrame, 1, wx.EXPAND | wx.ALL, 5)

        MainFrameSizer.Add(MainFrameCatalogPanel, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.EXPAND, 5)

        MainFrameMainPanel = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Main"), wx.VERTICAL)

        MainFrameMainPanel.SetMinSize(wx.Size(750, 500))
        self.MainFrameMainPanelSplitter = wx.SplitterWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                            wx.SP_3D)
        self.MainFrameMainPanelSplitter.Bind(wx.EVT_IDLE, self.MainFrameMainPanelSplitterOnIdle)

        self.MainFrameMainPanelBookHistory = wx.Panel(self.MainFrameMainPanelSplitter, wx.ID_ANY, wx.DefaultPosition,
                                                      wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.MainFrameMainPanelBookHistory.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))
        self.MainFrameMainPanelBookHistory.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        MainFrameMainPanelBookHistorySizer = wx.BoxSizer(wx.VERTICAL)

        self.m_splitter2 = wx.SplitterWindow(self.MainFrameMainPanelBookHistory, wx.ID_ANY, wx.DefaultPosition,
                                             wx.DefaultSize, wx.SP_3D)
        self.m_splitter2.Bind(wx.EVT_IDLE, self.m_splitter2OnIdle)

        self.MainFrameMainPanelBookSubPanel = wx.Panel(self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                       wx.TAB_TRAVERSAL)
        self.MainFrameMainPanelBookSubPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DDKSHADOW))

        self.MainFrameMainPanelHistorySubPanel = wx.Panel(self.m_splitter2, wx.ID_ANY, wx.DefaultPosition,
                                                          wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.MainFrameMainPanelHistorySubPanel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNSHADOW))

        self.m_splitter2.SplitHorizontally(self.MainFrameMainPanelBookSubPanel, self.MainFrameMainPanelHistorySubPanel,
                                           0)
        MainFrameMainPanelBookHistorySizer.Add(self.m_splitter2, 1, wx.EXPAND, 5)

        self.MainFrameMainPanelBookHistory.SetSizer(MainFrameMainPanelBookHistorySizer)
        self.MainFrameMainPanelBookHistory.Layout()
        MainFrameMainPanelBookHistorySizer.Fit(self.MainFrameMainPanelBookHistory)
        ###############################################
        #Tests are here
		
        #Input some questions
        q1 = "What planet do you live on?"
        a1 = {"Earth": True, "Mars": False, "Venus": False, "Saturn": False}

        q2 = "Which city is a capital of Ukraine?"
        a2 = {"Donbas": False, "Lviv": False, "Kyiv": True, "Mykolayiv": False}

        tests = []
        tests.append(Question(q1,a1))
        tests.append(Question(q2,a2))
        tests.append(Question(q1,a1))

        self.mQuestionList = tests
        self.mFinalResult = 0
		
		
        self.MainFrameMainPanelTests = wx.Panel(self.MainFrameMainPanelSplitter, wx.ID_ANY, wx.DefaultPosition,
                                                wx.Size(100, 100), wx.TAB_TRAVERSAL)
        self.MainFrameMainPanelTests.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
		
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        #copy-pasted code goes here
        if len(self.mQuestionList) > 0:
            self.mQuestionIndex = 0
            self.m_questionText = wx.StaticText( self.MainFrameMainPanelTests, wx.ID_ANY, self.mQuestionList[0].getQuestion(), wx.DefaultPosition, wx.DefaultSize, 0 )
            self.m_questionText.Wrap( -1 )
            bSizer2.Add( self.m_questionText, 1, wx.EXPAND|wx.ALL, 5 )
            

            answers = self.mQuestionList[0].getAnswers().keys();

            self.mAnswerCheckBoxes = []

            self.mAnswerCheckBoxes.append( wx.CheckBox( self.MainFrameMainPanelTests, wx.ID_ANY, answers[0], wx.DefaultPosition, wx.DefaultSize, 0 ) )
            bSizer2.Add( self.mAnswerCheckBoxes[0], 1, wx.ALL|wx.EXPAND, 5 ) 
            
            self.mAnswerCheckBoxes.append( wx.CheckBox( self.MainFrameMainPanelTests, wx.ID_ANY, answers[1], wx.DefaultPosition, wx.DefaultSize, 0 ) )
            bSizer2.Add( self.mAnswerCheckBoxes[1], 1, wx.ALL|wx.EXPAND, 5 )
            
            self.mAnswerCheckBoxes.append( wx.CheckBox( self.MainFrameMainPanelTests, wx.ID_ANY, answers[2], wx.DefaultPosition, wx.DefaultSize, 0 ) )
            bSizer2.Add( self.mAnswerCheckBoxes[2], 1, wx.ALL|wx.EXPAND, 5 )
            
            self.mAnswerCheckBoxes.append( wx.CheckBox( self.MainFrameMainPanelTests, wx.ID_ANY, answers[3], wx.DefaultPosition, wx.DefaultSize, 0 ) )
            bSizer2.Add( self.mAnswerCheckBoxes[3], 1, wx.ALL|wx.EXPAND, 5 )

            

        gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
        self.m_continue = wx.Button( self.MainFrameMainPanelTests, wx.ID_ANY, u"Continue", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.m_continue, 0, wx.ALL, 5 )
        
        self.m_results = wx.StaticText( self.MainFrameMainPanelTests, wx.ID_ANY, u"Points: 0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_results.Wrap( -1 )
        gSizer2.Add( self.m_results, 0, wx.ALL, 5 )
        
        bSizer2.Add( gSizer2, 1, wx.EXPAND, 5 )
        
        # Connect Events
        self.m_continue.Bind( wx.EVT_BUTTON, self.m_continueOnLeftDClick )			
        ###########################
        
        self.MainFrameMainPanelTests.SetSizer( bSizer2 )
        #self.MainFrameMainPanelTests.Layout()
        self.MainFrameMainPanelSplitter.SplitVertically(self.MainFrameMainPanelBookHistory,
                                                        self.MainFrameMainPanelTests, 0)
														
														
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        MainFrameMainPanel.Add(self.MainFrameMainPanelSplitter, 1, wx.EXPAND, 5)
        
        ###############################################
        #end of tests

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        MainFrameMainPanel.Add(bSizer5, 1, wx.EXPAND, 5)

        MainFrameSizer.Add(MainFrameMainPanel, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.EXPAND, 5)

        self.SetSizer(MainFrameSizer)
        self.Layout()
        self.Mnu = wx.MenuBar(0)
        self.Mnu.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))
        self.Mnu.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        self.MnuFile = wx.Menu()
        self.MnuFileOpen = wx.Menu()
        self.MnuFile.AppendSubMenu(self.MnuFileOpen, u"Open...")

        self.MnuFile.AppendSeparator()

        self.MnuFileExit = wx.Menu()

        self.MnuFile.AppendSubMenu(self.MnuFileExit, u"Exit")

        self.Mnu.Append(self.MnuFile, u"File")

        self.MnuEdit = wx.Menu()
        self.MnuEditOption1 = wx.Menu()
        self.MnuEdit.AppendSubMenu(self.MnuEditOption1, u"Inpit option 1 here")

        self.MnuEditOption2 = wx.Menu()
        self.MnuEdit.AppendSubMenu(self.MnuEditOption2, u"Input option 2 here")

        self.Mnu.Append(self.MnuEdit, u"Edit")

        self.MnuHelp = wx.Menu()
        self.MnuHelpAbout = wx.Menu()
        self.MnuHelp.AppendSubMenu(self.MnuHelpAbout, u"About...")

        self.Mnu.Append(self.MnuHelp, u"Help")

        self.SetMenuBar(self.Mnu)

        self.Status = self.CreateStatusBar(1, wx.ST_SIZEGRIP, wx.ID_ANY)
        self.Status.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))
        self.Status.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.CloseBook)

    def __del__(self):
        pass
	
	def SetQuestionList(self, iQuestionList):
		self.mQuestionList = iQuestionList

    # Virtual event handlers, overide them in your derived class
    def CloseBook(self, event):
        event.Skip()

    def MainFrameMainPanelSplitterOnIdle(self, event):
        self.MainFrameMainPanelSplitter.SetSashPosition(0)
        self.MainFrameMainPanelSplitter.Unbind(wx.EVT_IDLE)

    def m_splitter2OnIdle(self, event):
        self.m_splitter2.SetSashPosition(0)
        self.m_splitter2.Unbind(wx.EVT_IDLE)
		
    def updateView( self ):
        self.m_results.SetLabel( u"Points: " + str( self.mFinalResult ) )
        if len(self.mQuestionList) > self.mQuestionIndex:
            answers = self.mQuestionList[self.mQuestionIndex].getAnswers().keys();
            self.m_questionText.SetLabel( self.mQuestionList[self.mQuestionIndex].getQuestion() )

            i = 0
            #weak and buggy "for" loop but seem to work (better not change anything here)
            for answer in answers:
                self.mAnswerCheckBoxes[i].SetLabel( answers[i] )
                self.mAnswerCheckBoxes[i].SetValue(False)
                i += 1
        else:
            self.m_continue.SetLabel( u"Finish" )
            
            
            

    def nextQuestion( self ):
        if len(self.mQuestionList) > self.mQuestionIndex:
            userAnswers = self.mQuestionList[self.mQuestionIndex].getUserAnswers()
            
            answers = self.mQuestionList[self.mQuestionIndex].getAnswers().keys();
            i = 0
            #weak and buggy "for" loop but seem to work (better not change anything here)
            for answer in answers:
                userAnswers[answer] = self.mAnswerCheckBoxes[i].GetValue()
                i += 1
            self.mFinalResult += self.mQuestionList[self.mQuestionIndex].getQuestionResult()
            self.mQuestionIndex += 1
            
            self.updateView()
        else:
            self.Close()
	
    # Virtual event handlers, overide them in your derived class
    def m_continueOnLeftDClick( self, event ):
        self.nextQuestion()
        event.Skip()		
	

