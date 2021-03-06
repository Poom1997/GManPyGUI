from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import plugin.databaseConnect as database
import plugin.course as courseItem
from sendMessageForm import sendMessageUI


class seeCourseProfUI(QMainWindow):
    def __init__(self,parent = None):
        QMainWindow.__init__(self,None)
        self.setMinimumSize(900,600)
        self.setWindowTitle("Select Course")
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("resources/imagess/programBackground.png")))
        self.setPalette(palette)
        self.bar = QPixmap("resources/images/topBarBackground.png")
        self.parent = parent
        self.UIinit()

    def UIinit(self):
        loader = QUiLoader()
        form = loader.load("resources/UI/seeCourseProf.ui",None)
        self.setCentralWidget(form)

        #Upper Bar
        self.bar_group = form.findChild(QLabel,"barLabel_2")
        self.bar_group.setPixmap(self.bar)
        self.home_button = form.findChild(QPushButton,"homeButton")
        self.profile_button = form.findChild(QPushButton,"profileButton")
        self.grade_button = form.findChild(QPushButton,"gradeButton")
        self.course_button = form.findChild(QPushButton,"courseButton")
        self.temp = form.findChild(QPushButton, "temp")
        self.temp2 = form.findChild(QPushButton, "temp2")

        #page properties
        self.course_table = form.findChild(QTableWidget,"courseTable")
        self.header = self.course_table.horizontalHeader()
        self.header.setResizeMode(0,QHeaderView.ResizeToContents)
        self.header.setResizeMode(1,QHeaderView.Stretch)
        self.header.setResizeMode(2,QHeaderView.ResizeToContents)

        self.course_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.course_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.course_table.setEditTriggers(QAbstractItemView.NoEditTriggers)


        #Upper Bar pressed
        self.home_button.clicked.connect(self.goHome)
        self.profile_button.clicked.connect(self.goProfile)
        self.grade_button.clicked.connect(self.goGrade)
        self.temp.clicked.connect(self.goTemp)
        self.course_button.clicked.connect(self.goCourse)
        self.temp2.clicked.connect(self.goTemp2)


    def goHome(self):
        self.parent.changePageLoginSection("home")

    def goProfile(self):
        self.parent.changePageLoginSection("profile")

    def goGrade(self):
        self.parent.changePageLoginSection("grade")

    def goCourse(self):
        self.parent.changePageLoginSection("course")

    def goTemp(self):
        self.createM = sendMessageUI(parent = self.parent)
        self.createM.show()

    def goTemp2(self):
        self.parent.changePageLoginSection("login")

    def updatePage(self):
        data = self.parent.getCurrentUser()
        db = database.databaseCourse()
        temp = db.getCourseProfessor(data.getID())
        allCourse = self.createBulk(temp)
        self.course_table.setRowCount(len(allCourse))
        i = 0
        for course in allCourse:
            self.course_table.setItem(i, 0, QTableWidgetItem(course.getCourseID()))
            self.course_table.setItem(i, 1, QTableWidgetItem(course.getCourseName()))
            self.course_table.setItem(i, 2, QTableWidgetItem(course.getCredit()))
            i = i + 1

    def createBulk(self, data):
        temp = []
        for i in data:
            temp.append(courseItem.course(i))
        return temp
