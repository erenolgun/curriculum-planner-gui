import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from courses import Course
from service import Service
from busy import Busy
from classroom import Classroom
from day import Day
from scheduler import Scheduler
import csv
import os.path


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1480, 644)
        MainWindow.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 140, 471, 461))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.listTheScheduleButton = QtWidgets.QPushButton(self.frame)
        self.listTheScheduleButton.setGeometry(QtCore.QRect(20, 350, 421, 71))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.listTheScheduleButton.setFont(font)
        self.listTheScheduleButton.setStyleSheet(
            "background-color:rgb(105, 223, 222)")
        self.listTheScheduleButton.setObjectName("listTheScheduleButton")

        # BUTTON AYARLAMASI
        self.listTheScheduleButton.clicked.connect(self.listSchedule)

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 421, 31))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                   "color: #FFF")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 421, 31))
        self.label_4.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                   "color: #FFF")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 421, 31))
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                   "color: #FFF")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 250, 421, 31))
        self.label_6.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                   "color: #FFF")
        self.label_6.setObjectName("label_6")
        self.coursesCsvPath = QtWidgets.QTextEdit(self.frame)
        self.coursesCsvPath.setGeometry(QtCore.QRect(20, 50, 421, 31))
        self.coursesCsvPath.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.coursesCsvPath.setObjectName("coursesCsvPath")
        self.classroomCsvPath = QtWidgets.QTextEdit(self.frame)
        self.classroomCsvPath.setGeometry(QtCore.QRect(20, 130, 421, 31))
        self.classroomCsvPath.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.classroomCsvPath.setObjectName("classroomCsvPath")
        self.busyCsvPath = QtWidgets.QTextEdit(self.frame)
        self.busyCsvPath.setGeometry(QtCore.QRect(20, 210, 421, 31))
        self.busyCsvPath.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.busyCsvPath.setObjectName("busyCsvPath")
        self.serviceCsvPath = QtWidgets.QTextEdit(self.frame)
        self.serviceCsvPath.setGeometry(QtCore.QRect(20, 290, 421, 31))
        self.serviceCsvPath.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.serviceCsvPath.setObjectName("serviceCsvPath")

        # WRONG PATH

        self.wrongPathError = QtWidgets.QWidget(self.frame)
        self.wrongPathError.setGeometry(QtCore.QRect(-10, -10, 481, 481))
        self.wrongPathError.setObjectName("wrongPathError")
        self.checkLabel = QtWidgets.QLabel(self.wrongPathError)
        self.checkLabel.setGeometry(QtCore.QRect(100, 110, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(14)
        self.checkLabel.setFont(font)
        self.checkLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkLabel.setObjectName("checkLabel")
        self.OkayButton = QtWidgets.QPushButton(self.wrongPathError)
        self.OkayButton.setGeometry(QtCore.QRect(100, 210, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(14)
        self.OkayButton.setFont(font)
        self.OkayButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OkayButton.setObjectName("OkayButton")

        self.wrongPathError.setVisible(False)

        self.OkayButton.clicked.connect(self.clickWrongOK)

        # NO WAY ERROR

        self.noWayError = QtWidgets.QWidget(self.frame)
        self.noWayError.setGeometry(QtCore.QRect(-10, -10, 481, 481))
        self.noWayError.setObjectName("noWayError")
        self.noWayLabel = QtWidgets.QLabel(self.noWayError)
        self.noWayLabel.setGeometry(QtCore.QRect(100, 110, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        self.noWayLabel.setFont(font)
        self.noWayLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.noWayLabel.setObjectName("noWayLabel")
        self.noWayOK = QtWidgets.QPushButton(self.noWayError)
        self.noWayOK.setGeometry(QtCore.QRect(100, 210, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(14)
        self.noWayOK.setFont(font)
        self.noWayOK.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.noWayOK.setObjectName("noWayOK")

        self.noWayError.setVisible(False)

        self.noWayOK.clicked.connect(self.clickWayOK)

        self.aybuImage = QtWidgets.QLabel(self.centralwidget)
        self.aybuImage.setGeometry(QtCore.QRect(30, 30, 81, 81))
        self.aybuImage.setStyleSheet("")
        self.aybuImage.setText("")
        self.aybuImage.setPixmap(QtGui.QPixmap(
            "Project_Scheduler/ASILAYBULOGO.jpg"))
        self.aybuImage.setScaledContents(True)
        self.aybuImage.setObjectName("aybuImage")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 20, 591, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "color: #FFF\n"
                                    "}")
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 60, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
                                      "color: #FFF\n"
                                      "}")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.scheduleTable = QtWidgets.QTableWidget(self.centralwidget)
        self.scheduleTable.setGeometry(QtCore.QRect(520, 140, 941, 461))
        self.scheduleTable.setMinimumSize(QtCore.QSize(941, 461))
        self.scheduleTable.setMaximumSize(QtCore.QSize(941, 461))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.scheduleTable.setFont(font)
        self.scheduleTable.setStyleSheet("\n"
                                         "color: rgb(98, 208, 206);")
        self.scheduleTable.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.scheduleTable.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scheduleTable.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scheduleTable.setTextElideMode(QtCore.Qt.ElideRight)
        self.scheduleTable.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.scheduleTable.setWordWrap(False)
        self.scheduleTable.setObjectName("scheduleTable")
        self.scheduleTable.setColumnCount(2)
        self.scheduleTable.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.scheduleTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.scheduleTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.scheduleTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.scheduleTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.scheduleTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.scheduleTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.scheduleTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.scheduleTable.setItem(0, 0, item)

        # TABLOYU BURADA DOLDURUYORUZ
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.scheduleTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.scheduleTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.scheduleTable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.scheduleTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.scheduleTable.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.scheduleTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.scheduleTable.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.scheduleTable.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.scheduleTable.setItem(4, 1, item)
        self.scheduleTable.horizontalHeader().setCascadingSectionResizes(True)
        self.scheduleTable.horizontalHeader().setDefaultSectionSize(400)
        self.scheduleTable.horizontalHeader().setMinimumSectionSize(87)
        self.scheduleTable.horizontalHeader().setSortIndicatorShown(True)
        self.scheduleTable.horizontalHeader().setStretchLastSection(True)
        self.scheduleTable.verticalHeader().setCascadingSectionResizes(False)
        self.scheduleTable.verticalHeader().setDefaultSectionSize(90)
        self.scheduleTable.verticalHeader().setSortIndicatorShown(False)
        self.scheduleTable.verticalHeader().setStretchLastSection(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scheduler"))
        self.listTheScheduleButton.setText(
            _translate("MainWindow", "List the Schedule"))
        self.label_2.setText(_translate(
            "MainWindow", "Please write a courses.csv path"))
        self.label_4.setText(_translate(
            "MainWindow", "Please write a classroom.cvs path"))
        self.label_5.setText(_translate(
            "MainWindow", "Please write a busy.csv path"))
        self.label_6.setText(_translate(
            "MainWindow", "Please write a service.csv path"))
        self.checkLabel.setText(_translate(
            "MainWindow", "PLEASE CHECK YOUR FILE PATH!!"))
        self.OkayButton.setText(_translate("MainWindow", "OK"))

        self.noWayLabel.setText(_translate(
            "MainWindow", "THERE IS NO WAY TO CREATE A SCHEDULE!!"))
        self.noWayOK.setText(_translate("MainWindow", "OK"))

        self.lineEdit.setText(_translate(
            "MainWindow", "ANKARA YILDIRIM BEYAZIT UNIVERSITY"))
        self.lineEdit_2.setText(_translate(
            "MainWindow", "COMPUTER ENGINEERING SCHEDULE"))
        self.scheduleTable.setSortingEnabled(False)
        item = self.scheduleTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Monday"))
        item = self.scheduleTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tuesday"))
        item = self.scheduleTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Wednesday"))
        item = self.scheduleTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Thursday"))
        item = self.scheduleTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Friday"))
        item = self.scheduleTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Morning"))
        item = self.scheduleTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Afternoon"))
        __sortingEnabled = self.scheduleTable.isSortingEnabled()
        self.scheduleTable.setSortingEnabled(False)
        self.scheduleTable.setSortingEnabled(__sortingEnabled)

    def listSchedule(self):
        coursePath = self.takeCoursePath()
        classroomPath = self.takeClassroomPath()
        busyPath = self.takeBusyPath()
        servicePath = self.takeServicePath()
        if(coursePath != "" and classroomPath != "" and busyPath != "" and servicePath != ""):
            self.readFiles(coursePath, classroomPath, busyPath, servicePath)
        else:
            self.wrongPathError.setVisible(True)

    def clickWrongOK(self):
        self.wrongPathError.setVisible(False)

    def clickWayOK(self):
        self.noWayError.setVisible(False)

    def takeCoursePath(self):
        course = self.coursesCsvPath.toPlainText()
        return course

    def takeClassroomPath(self):
        classroom = self.classroomCsvPath.toPlainText()
        return classroom

    def takeBusyPath(self):
        busy = self.busyCsvPath.toPlainText()
        return busy

    def takeServicePath(self):
        service = self.serviceCsvPath.toPlainText()
        return service

    def readFiles(self, coursePath, classroomPath, busyPath, servicePath):
        if(os.path.exists(coursePath) and os.path.exists(classroomPath) and os.path.exists(busyPath) and os.path.exists(servicePath)):

            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

            course_list = []
            service_list = []
            busy_list = []
            class_list = []
            days_list = []
            schedule_list = []
            big_class_list = []
            small_class_list = []
            intersection_compare_list = []
            display_curriculum = []
            temporary_list = []

            def is_busy(instructor, day, time):
                for busy in busy_list:
                    if(instructor == busy.get_instructor() and day == busy.get_busy_day() and time == busy.get_busy_time()):
                        return True

            def get_semester(course_code):
                for course in intersection_compare_list:
                    if(course.get_course_code() == course_code):
                        year_of_the_semester = course.get_course_semester()
                        return year_of_the_semester

            def is_intersection(day, time, course_code):
                input_semester = get_semester(course_code)

                for schedule in schedule_list:
                    if(day == schedule.get_day_name() and time == schedule.get_day_time() and input_semester == get_semester(schedule.get_course_code())):
                        return True

            with open(coursePath, 'r') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    course = Course(row[0], row[1], row[2],
                                    row[3], row[4], row[5], row[6])
                    course_list.append(course)

            with open(servicePath, 'r') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    service = Service(row[0], row[1], row[2])
                    service_list.append(service)

            with open(busyPath, 'r') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    busy = Busy(row[0], row[1], row[2])
                    busy_list.append(busy)

            with open(classroomPath, 'r') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    classroom = Classroom(row[0], row[1])
                    class_list.append(classroom)

            for day in days:
                day_ = Day(day, class_list)
                days_list.append(day_)

            intersection_compare_list = list(course_list)

            for service in service_list:
                for day in days_list:
                    if(service.get_course_day() == day.get_name()):
                        if(service.get_course_time() == "Morning"):
                            day.morning.append(service.get_course_code())
                        else:
                            day.afternoon.append(service.get_course_code())

            for day in days_list:
                if(day.get_morning()):
                    for course_code in day.morning:
                        for course in course_list:
                            if(course_code == course.get_course_code() and course.get_course_type() == 'C'):
                                schedule = Scheduler(
                                    day.get_name(), "Morning", day.get_morning_big_class().pop(0), course_code)
                                schedule_list.append(schedule)
                            elif(course_code == course.get_course_code() and course.get_course_type() == 'E'):
                                schedule = Scheduler(
                                    day.get_name(), "Morning", day.get_morning_small_class().pop(0), course_code)
                                schedule_list.append(schedule)

                if(day.get_afternoon()):
                    for course_code in day.afternoon:
                        for course in course_list:
                            if(course_code == course.get_course_code() and course.get_course_type() == 'C'):
                                schedule = Scheduler(
                                    day.get_name(), "Afternoon", day.get_afternoon_big_class().pop(0), course_code)
                                schedule_list.append(schedule)
                            elif(course_code == course.get_course_code() and course.get_course_type() == 'E'):
                                schedule = Scheduler(
                                    day.get_name(), "Afternoon", day.get_afternoon_small_class().pop(0), course_code)
                                schedule_list.append(schedule)

            for service_lesson in service_list:
                for course in course_list:
                    if(service_lesson.get_course_code() == course.get_course_code()):
                        course_list.remove(course)

            for day in days_list:
                for course in course_list:
                    if(day.get_morning_small_class()):
                        if(course.get_course_type() == 'E' and not(is_busy(course.get_course_instructor(), day.get_name(), "Morning")) and not(is_intersection(day.get_name(), "Morning", course.get_course_code()))):
                            schedule = Scheduler(
                                day.get_name(), "Morning", day.get_morning_small_class().pop(0), course.get_course_code())
                            schedule_list.append(schedule)
                            course_list.remove(course)

            for day in days_list:
                for course in course_list:
                    if(day.get_afternoon_small_class()):
                        if(course.get_course_type() == 'E' and not(is_busy(course.get_course_instructor(), day.get_name(), "Afternoon")) and not(is_intersection(day.get_name(), "Afternoon", course.get_course_code()))):
                            schedule = Scheduler(
                                day.get_name(), "Afternoon", day.get_afternoon_small_class().pop(0), course.get_course_code())
                            schedule_list.append(schedule)
                            course_list.remove(course)

            for day in days_list:
                for course in course_list:
                    if(day.get_morning_big_class()):
                        if(course.get_course_type() == 'C' and not(is_busy(course.get_course_instructor(), day.get_name(), "Morning")) and not(is_intersection(day.get_name(), "Morning", course.get_course_code()))):
                            schedule = Scheduler(
                                day.get_name(), "Morning", day.get_morning_big_class().pop(0), course.get_course_code())
                            schedule_list.append(schedule)
                            course_list.remove(course)

            for day in days_list:
                for course in course_list:
                    if(day.get_afternoon_big_class()):
                        if(course.get_course_type() == 'C' and not(is_busy(course.get_course_instructor(), day.get_name(), "Afternoon")) and not(is_intersection(day.get_name(), "Afternoon", course.get_course_code()))):
                            schedule = Scheduler(
                                day.get_name(), "Afternoon", day.get_afternoon_big_class().pop(0), course.get_course_code())
                            schedule_list.append(schedule)
                            course_list.remove(course)

            for day in days_list:
                for course in course_list:
                    if(day.get_morning_big_class()):
                        if(course.get_course_type() == 'E' and not(is_busy(course.get_course_instructor(), day.get_name(), "Morning")) and not(is_intersection(day.get_name(), "Morning", course.get_course_code()))):
                            schedule = Scheduler(
                                day.get_name(), "Morning", day.get_morning_big_class().pop(len(day.get_morning_big_class()) - 1), course.get_course_code())
                            schedule_list.append(schedule)
                            course_list.remove(course)

            for day in days_list:
                for course in course_list:
                    if(day.get_afternoon_big_class()):
                        if(course.get_course_type() == 'E' and not(is_busy(course.get_course_instructor(), day.get_name(), "Afternoon")) and not(is_intersection(day.get_name(), "Afternoon", course.get_course_code()))):
                            schedule = Scheduler(
                                day.get_name(), "Afternoon", day.get_afternoon_big_class().pop(len(day.get_afternoon_big_class()) - 1), course.get_course_code())
                            schedule_list.append(schedule)
                            course_list.remove(course)

            big_class_substring = "bigClass"
            small_class_substring = "smallClass"

            if(len(course_list) != 0):
                self.noWayError.setVisible(True)
            else:
                for day in days_list:
                    for item_morning in schedule_list:
                        if(day.get_name() == item_morning.get_day_name() and item_morning.get_day_time() == "Morning" and item_morning.get_class_type().find(big_class_substring) != -1):
                            display_curriculum.append(item_morning)
                    for item_morning in schedule_list:
                        if(day.get_name() == item_morning.get_day_name() and item_morning.get_day_time() == "Morning" and item_morning.get_class_type().find(small_class_substring) != -1):
                            display_curriculum.append(item_morning)
                    for item_afternoon in schedule_list:
                        if(day.get_name() == item_afternoon.get_day_name() and item_afternoon.get_day_time() == "Afternoon" and item_afternoon.get_class_type().find(big_class_substring) != -1):
                            display_curriculum.append(item_afternoon)
                    for item_afternoon in schedule_list:
                        if(day.get_name() == item_afternoon.get_day_name() and item_afternoon.get_day_time() == "Afternoon" and item_afternoon.get_class_type().find(small_class_substring) != -1):
                            display_curriculum.append(item_afternoon)

                mondayMorning = ""
                tuesdayMorning = ""
                wednesdayMorning = ""
                thursdayMorning = ""
                fridayMorning = ""

                for curric_item in display_curriculum:
                    if(curric_item.get_day_name() == "Monday" and curric_item.get_day_time() == "Morning"):
                        course_code = curric_item.get_course_code()
                        class_type = curric_item.get_class_type()
                        mondayMorning += course_code + ", " + class_type + "\n"

                item = QtWidgets.QTableWidgetItem(mondayMorning)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.scheduleTable.setItem(0, 0, item)

                for curric_item in display_curriculum:
                    if(curric_item.get_day_name() == "Tuesday" and curric_item.get_day_time() == "Morning"):
                        course_code = curric_item.get_course_code()
                        class_type = curric_item.get_class_type()
                        tuesdayMorning += course_code + ", " + class_type + "\n"

                item = QtWidgets.QTableWidgetItem(tuesdayMorning)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.scheduleTable.setItem(1, 0, item)

                for curric_item in display_curriculum:
                    if(curric_item.get_day_name() == "Wednesday" and curric_item.get_day_time() == "Morning"):
                        course_code = curric_item.get_course_code()
                        class_type = curric_item.get_class_type()
                        wednesdayMorning += course_code + ", " + class_type + "\n"

                item = QtWidgets.QTableWidgetItem(wednesdayMorning)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.scheduleTable.setItem(2, 0, item)

                for curric_item in display_curriculum:
                    if(curric_item.get_day_name() == "Thursday" and curric_item.get_day_time() == "Morning"):
                        course_code = curric_item.get_course_code()
                        class_type = curric_item.get_class_type()
                        thursdayMorning += course_code + ", " + class_type + "\n"

                item = QtWidgets.QTableWidgetItem(thursdayMorning)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.scheduleTable.setItem(3, 0, item)

                for curric_item in display_curriculum:
                    if(curric_item.get_day_name() == "Friday" and curric_item.get_day_time() == "Morning"):
                        course_code = curric_item.get_course_code()
                        class_type = curric_item.get_class_type()
                        fridayMorning += course_code + ", " + class_type + "\n"

                item = QtWidgets.QTableWidgetItem(fridayMorning)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.scheduleTable.setItem(4, 0, item)

                # AFTERNOON PART

                mondayAfternoon = ""
                tuesdayAfternoon = ""
                wednesdayAfternoon = ""
                thursdayAfternoon = ""
                fridayAfternoon = ""

                for curric_item in display_curriculum:
                    if(curric_item.get_day_name() == "Monday" and curric_item.get_day_time() == "Afternoon"):
                        course_code = curric_item.get_course_code()
                        class_type = curric_item.get_class_type()
                        mondayAfternoon += course_code + ", " + class_type + "\n"

                item = QtWidgets.QTableWidgetItem(mondayAfternoon)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.scheduleTable.setItem(0, 1, item)

                for curric_item in display_curriculum:
                    if(curric_item.get_day_name() == "Tuesday" and curric_item.get_day_time() == "Afternoon"):
                        course_code = curric_item.get_course_code()
                        class_type = curric_item.get_class_type()
                        tuesdayAfternoon += course_code + ", " + class_type + "\n"

                item = QtWidgets.QTableWidgetItem(tuesdayAfternoon)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.scheduleTable.setItem(1, 1, item)

                for curric_item in display_curriculum:
                    if(curric_item.get_day_name() == "Wednesday" and curric_item.get_day_time() == "Afternoon"):
                        course_code = curric_item.get_course_code()
                        class_type = curric_item.get_class_type()
                        wednesdayAfternoon += course_code + ", " + class_type + "\n"

                item = QtWidgets.QTableWidgetItem(wednesdayAfternoon)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.scheduleTable.setItem(2, 1, item)

                for curric_item in display_curriculum:
                    if(curric_item.get_day_name() == "Thursday" and curric_item.get_day_time() == "Afternoon"):
                        course_code = curric_item.get_course_code()
                        class_type = curric_item.get_class_type()
                        thursdayAfternoon += course_code + ", " + class_type + "\n"

                item = QtWidgets.QTableWidgetItem(thursdayAfternoon)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.scheduleTable.setItem(3, 1, item)

                for curric_item in display_curriculum:
                    if(curric_item.get_day_name() == "Friday" and curric_item.get_day_time() == "Afternoon"):
                        course_code = curric_item.get_course_code()
                        class_type = curric_item.get_class_type()
                        fridayAfternoon += course_code + ", " + class_type + "\n"

                item = QtWidgets.QTableWidgetItem(fridayAfternoon)
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.scheduleTable.setItem(4, 1, item)

        else:
            self.wrongPathError.setVisible(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
