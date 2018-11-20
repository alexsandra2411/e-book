# coding=utf-8
import wx
import sys

class ContentPanel(wx.Panel):
    def __init__(self, parent, size):
        wx.Panel.__init__(self, parent, size=size)

        self.content = ''
        self.SetBackgroundColour('WHITE')
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.codeFont = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Courier')

        self.horizBorder = 10
        self.vertBorder = 10

        _, displayAreaWidth = self.GetSize()

        self.prevWidth = displayAreaWidth

        self.formattedLines = []

        self.maxLinesOnPage = 0
        self.currentPage = 0
        self.numberOfPages = 0

        # self.dc = wx.ClientDC(self)

        self.Centre()
        self.Show()

    def OnPaint(self, e):
        dc = wx.ClientDC(self)
        dc.Clear()

        dc.SetFont(self.codeFont)
        dc.SetTextForeground('BLACK')

        _, textHeight = dc.GetTextExtent("Sample text")
        displayAreaWidth, displayAreaHeight = self.GetSize()

        #recrop lines only if not done before or window was resized
        if (len(self.formattedLines) == 0 or
            abs(self.prevWidth - displayAreaWidth) > 5):

            self.prevWidth = displayAreaWidth

            self.FormatLines(displayAreaHeight, textHeight)



        #to handle the case when user is on last page and resized a window
        if (self.currentPage > self.numberOfPages):
            self.currentPage = self.numberOfPages - 1

        lineIndex = 0

        while (lineIndex < self.maxLinesOnPage and
               lineIndex < len(self.formattedLines)):

            #e.g 0 (index) + 1 ((zero indexed) page) * 9 (max lines) = 9 (1st line on actual 2nd page)
            indexInContextOfPage = lineIndex + self.maxLinesOnPage * self.currentPage

            yPos = self.horizBorder + (textHeight * lineIndex)


            try:
                if indexInContextOfPage < len(self.formattedLines):
                    #if (indexInContextOfPage < len(rawLines) and indexInContextOfPage > 0):
                    dc.DrawText(self.formattedLines[indexInContextOfPage], self.vertBorder, yPos)

            except:
                print sys.exc_info()[0]
                print "indexInContextOfPage: " + str(indexInContextOfPage)
                print "len(rawLines): " + str(len(self.formattedLines))

            lineIndex += 1


    def FormatLines(self, displayAreaHeight, textHeight):
        rawLines = self.content.split('\n')

        #remove empty strings
        rawLines = filter(lambda line: line != '', rawLines)

        rawLines = self.CropLinesToFitInPage(rawLines)

        self.maxLinesOnPage = (displayAreaHeight - self.vertBorder) / textHeight
        self.numberOfPages = len(rawLines) / self.maxLinesOnPage

        self.formattedLines = rawLines

    def OnNextButtonClicked(self, e):
        if self.currentPage < self.numberOfPages:
            self.currentPage += 1
            self.Parent.ForceRedraw()

    def OnPrevButtonClicked(self, e):
        if self.currentPage > 0:
            self.currentPage -= 1
            self.Parent.ForceRedraw()

    # Helpers
    def SplitRawLinesOnPages(self, lines):
        pass

    def CropLinesToFitInPage(self, lines):

        lineIndex = 0
        while lineIndex < len(lines):
            line = lines[lineIndex]

            if not self.FitsInCurrentWidth(line):
                lines[lineIndex] = self.CropLineAndAddRemovedWordsToNextString(lineIndex, lines)

            lineIndex += 1

        return lines

    #Remove last occurence of string
    def rchop(self, thestring, ending):

        whitespaceLength = 0
        i = -1
        while thestring[i] == ' ':
            whitespaceLength += 1
            i -= 1

        if whitespaceLength > 0:
            stringWithNoWhitespaceInEnd = thestring[:-whitespaceLength]
            if stringWithNoWhitespaceInEnd.endswith(ending):
                return thestring[:-len(ending)]

        elif thestring.endswith(ending):
            return thestring[:-len(ending)]

        else:
            st = "put breakpoint here"

        return thestring

    def CropLineAndAddRemovedWordsToNextString(self, lineIndex, lines):
        line = lines[lineIndex]
        words = line.split(' ')

        #remove empty strings
        words = filter(lambda word: word != '', words)

        dc = wx.ClientDC(self)
        dc.SetFont(self.codeFont)

        lineWidth, _ = dc.GetTextExtent(line)

        removedWords = ""
        removedWordsLength = 0

        wordIndex = len(words)
        while wordIndex >= 0:
            wordIndex -= 1

            word = words[wordIndex]

            wordLength, _ = dc.GetTextExtent(word + " ")
            removedWordsLength += wordLength

            removedWords = word + " " + removedWords

            if self.FitsInCurrentWidth2(lineWidth-removedWordsLength):

                #if cropping the last line add removed words to new line
                if lineIndex >= len(lines) - 1:
                    lines.append(removedWords)
                else:
                    lines[lineIndex + 1] = removedWords + lines[lineIndex + 1]

                return " ".join(words[:wordIndex])

    def FitsInCurrentWidth(self, line):
        dc = wx.ClientDC(self)
        dc.SetFont(self.codeFont)

        contentWidth, _ = dc.GetTextExtent(line)
        displayAreaWidth, _ = self.GetSize()

        if contentWidth + self.horizBorder <= displayAreaWidth:
            return True
        else:
            return False

    def FitsInCurrentWidth2(self, lineWidth):
        displayAreaWidth, _ = self.GetSize()

        if lineWidth + self.horizBorder <= displayAreaWidth:
            return True
        else:
            return False


class WrapPanel(wx.Panel):
    def __init__(self, parent, size=(600, 600)):
        super(WrapPanel, self).__init__(parent, size=size)

        #some workaround stuff
        self.redrawDelta = 1

        #Static text with name of the chapter
        self.contentName = wx.StaticText(self, label='Here contents name will be')

        #next page and prev page buttons
        self.buttonPrev = wx.Button(self, label='Prev', size=(70, 30))
        self.buttonNext = wx.Button(self, label='Next', size=(70, 30))

        #let content panel occupy all width of a parent
        #but substract height of other elements and borders
        clientWidth, clientHeight = self.GetSize()
        self.contentPanel = ContentPanel(self, (clientWidth, clientHeight - self.CountHeightOfOherElemets()))

        #bind buttons to OnClicked* methods of contentPanel (next page, prev page)
        self.buttonPrev.Bind(wx.EVT_BUTTON, self.contentPanel.OnPrevButtonClicked)
        self.buttonNext.Bind(wx.EVT_BUTTON, self.contentPanel.OnNextButtonClicked)

        self.InitUI()
        self.ForceRedraw()
        self.Centre()
        self.Show()

    def ForceRedraw(self):
        # workaround to force redraw #
        w, h = self.GetSize()  #
        self.SetSize((w + self.redrawDelta, h + self.redrawDelta))
        self.redrawDelta *= -1

    def CountHeightOfOherElemets(self):
        otherElementsHeight = 0

        sizeW, sizeH = self.contentName.GetSize()
        otherElementsHeight += sizeH

        # multiply by 2 because 2 equally sized buttons
        sizeW, sizeH = self.buttonNext.GetSize()
        otherElementsHeight += sizeH * 2

        borders = 60

        otherElementsHeight += borders

        return otherElementsHeight

    def InitUI(self):
        self.SetBackgroundColour('GRAY')
        vertBox = wx.BoxSizer(wx.VERTICAL)

        # Static text with content name at top|center
        horBox = wx.BoxSizer(wx.HORIZONTAL)
        horBox.Add(self.contentName)
        vertBox.Add(horBox, flag=wx.ALIGN_CENTER | wx.RIGHT | wx.TOP | wx.BOTTOM, border=10)

        #Panel with text content at center
        horBox2 = wx.BoxSizer(wx.HORIZONTAL)
        horBox2.Add(self.contentPanel, flag=wx.EXPAND, proportion=1)
        vertBox.Add(horBox2, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=10)

        #Next and Prev buttons at the bottom|right
        horBox3 = wx.BoxSizer(wx.HORIZONTAL)
        horBox3.Add(self.buttonPrev)
        horBox3.Add(self.buttonNext, flag=wx.LEFT, border=10)
        vertBox.Add(horBox3, flag=wx.ALIGN_RIGHT | wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)

        self.SetSizer(vertBox)

    def DisplayComponent(self, component):
        self.contentName.SetLabel(component.name)
        self.contentPanel.content = component.content
        self.ForceRedraw()


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
                                      size=(400, 500))

        self.Centre()
        self.Show()


class Component:
    def _init_(self):
        self.content = ''
        self.list = []
        self.name = ''

    def setValues(self, _content, _name, list):
        self.content = _content
        self.name = _name
        self.list = list


if __name__ == '__main__':
    content = """
1.3. Організація програми

Перші три стрічки є вказівками препроцесору. Команда include  вказує, що препроцесору потрібно додати до тексту програми зміст файлів stdio.h (стандартні бібліотеки введення-виведення) і файлів з іменем file1.c  та file2.c.
Імена стандартних файлів беруться в дужки &amp;amp;lt; &amp;amp;gt;, а імена інших файлів - в лапки ’’.
Стрічка float res описує зовнішню змінну. Назва main() визначає одну з цих функцій як головну. З неї починається виконання програми.
Фігурні дужки є операторними дужками мови Сі. Оператори int   і float є операторами описувачами. Перший описує змінні цілого типу a і b, а другий - дійсне значення результатів функцій mida() та midg(), які відповідно визначають середнє арифметичне та середнє геометричне значення двох цілих.
Дужки типу /* і */ визначають відповідно початок і кінець коментарю. Оператори printf, scanf належать до групи операторів вводу-виводу, а оператори if...else, return() - до групи операторів керування.
Специфікація  f в операторах printf та scanf визначає, що ввід-вивід в мові СІ носить форматний характер. Параметри цих операторів можна розбити на дві групи. Перша визначає специфікації інформації вводу-виводу, а друга - змінні вводу-виводу.
Як перша, так і друга частина може мати спеціальні символи, або групи символів, чи бути пустою. Так в першому операторі printf текст взятий в лапки ‘ ’ визначає специфікацію вводу. В результаті буде надруковано: введіть 2 цілих числа і потім, голівка   пристрою друку буде переведена на нову стрічку.
Останню дію викликає наявність в специфікації символів.
Спеціальні символи специфікації оператору scanf типу % визначають початок формату опису вводу-виводу змінної.
Так символ d говорить про те що відповідна змінна повинна бути змінною цілого типу, а  f%5,4 визначає змінну дійсного типу з полями 5 і 4 для цілої та дробової частини.
Друга частина оператору scanf типу &amp;amp;а, &amp;amp;b визначає, що введені значення будуть присвоєні змінним а та b.
Оператор if визначається традиційним чином. Оператори mida(a, b)  та midg(a,b) є операторами функціями, а оператор return визначає значення що виробляє відповідна функція, в тілі якої він знаходиться.
Оператор extern   визначає, що  об’єкт його опису є зовнішнім, доступним для всіх функцій цієї програми.
Припустимо, що ми набрали текст цієї  програми в якомусь редакторові і записали її в файл exam11.c. Як ми вже зазначали існує більше 40 компіляторів мови Сі.
Розглянемо варіант компіляції нашої програми в OC UNIX. Компілятор з мови Сі в OC UNIX  називається СС. Тому для компіляції нашої програми потрібно ввести команду: cc exam11.c
Якщо   програма не має синтаксичних помилок, тоді на екрані дисплею буде виводитися символ  запрошення  &amp;amp;gt;, в іншому випадку на екрані будуть виводитися повідомлення про помилки.
Будемо вважати, що наша програма не містить синтаксичних помилок і ми отримали  запрошення .
Це буде означати, що з’явився новий файл з іменем a.out . В цьому файлі міститься файл з програмою, вже готовою до виконання і отриманою в результаті трансляції ( чи компіляції ) нашої початкової програми. Для її виконання ми повинні ввести команду:  a.out.
На екрані дисплею з’явиться фраза:  введіть два цілих числа  і маркер переведеться на початок нової стрічки. Після набору  через розподільник двох цілих чисел, натиснемо клавішу ENTER. В залежності від значень, які ми ввели, отримаємо друк   середнє геометричне дорівнює.  і його значення, або   середнє арифметичне дорівнює.  і його значення.
"""
    name = "1.3. Program organization"

    component = Component()
    component.setValues(content, name, None)

    app = wx.App()
    frame = Example(None, 'Module for Content')
    wrapPanel = WrapPanel(frame, frame.GetClientSize())
    wrapPanel.DisplayComponent(component)
    app.MainLoop()