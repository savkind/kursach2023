
from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_gui(object):
    def setupUi(self, gui):
        if gui.objectName():
            gui.setObjectName(u"gui")
        gui.resize(800, 413)
        gui.setMaximumSize(QSize(800, 600))
        self.tabWidget = QTabWidget(gui)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 800, 600))
        self.TAB_PROJECTS = QWidget()
        self.TAB_PROJECTS.setObjectName(u"TAB_PROJECTS")
        self.TABLE_PROJECT_HEADER = QTableWidget(self.TAB_PROJECTS)
        if (self.TABLE_PROJECT_HEADER.columnCount() < 5):
            self.TABLE_PROJECT_HEADER.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.TABLE_PROJECT_HEADER.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font = QFont()
        font.setPointSize(8)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.TABLE_PROJECT_HEADER.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TABLE_PROJECT_HEADER.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TABLE_PROJECT_HEADER.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TABLE_PROJECT_HEADER.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.TABLE_PROJECT_HEADER.setObjectName(u"TABLE_PROJECT_HEADER")
        self.TABLE_PROJECT_HEADER.setGeometry(QRect(0, 0, 800, 300))
        self.TABLE_PROJECT_HEADER.horizontalHeader().setMinimumSectionSize(39)
        self.TABLE_PROJECT_HEADER.horizontalHeader().setDefaultSectionSize(155)
        self.tabWidget.addTab(self.TAB_PROJECTS, "")
        self.TAB_NEWS = QWidget()
        self.TAB_NEWS.setObjectName(u"TAB_NEWS")
        self.TABLE_PROJECT_NEWS = QTableWidget(self.TAB_NEWS)
        if (self.TABLE_PROJECT_NEWS.columnCount() < 3):
            self.TABLE_PROJECT_NEWS.setColumnCount(3)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TABLE_PROJECT_NEWS.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TABLE_PROJECT_NEWS.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TABLE_PROJECT_NEWS.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        self.TABLE_PROJECT_NEWS.setObjectName(u"TABLE_PROJECT_NEWS")
        self.TABLE_PROJECT_NEWS.setGeometry(QRect(0, 0, 800, 300))
        self.TABLE_PROJECT_NEWS.horizontalHeader().setDefaultSectionSize(155)
        self.BUTTON_PROJECTS_2 = QPushButton(self.TAB_NEWS)
        self.BUTTON_PROJECTS_2.setObjectName(u"BUTTON_PROJECTS_2")
        self.BUTTON_PROJECTS_2.setGeometry(QRect(10, 410, 111, 31))
        self.BUTTON_PROJECT_NEWS = QPushButton(self.TAB_NEWS)
        self.BUTTON_PROJECT_NEWS.setObjectName(u"BUTTON_PROJECT_NEWS")
        self.BUTTON_PROJECT_NEWS.setGeometry(QRect(10, 330, 110, 30))
        self.button_project_news_commit = QPushButton(self.TAB_NEWS)
        self.button_project_news_commit.setObjectName(u"button_project_news_commit")
        self.button_project_news_commit.setGeometry(QRect(140, 330, 111, 31))
        self.tabWidget.addTab(self.TAB_NEWS, "")
        self.TAB_EMPLOYEES = QWidget()
        self.TAB_EMPLOYEES.setObjectName(u"TAB_EMPLOYEES")
        self.TABLE_EMP = QTableWidget(self.TAB_EMPLOYEES)
        if (self.TABLE_EMP.columnCount() < 6):
            self.TABLE_EMP.setColumnCount(6)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.TABLE_EMP.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.TABLE_EMP.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.TABLE_EMP.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.TABLE_EMP.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.TABLE_EMP.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.TABLE_EMP.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        self.TABLE_EMP.setObjectName(u"TABLE_EMP")
        self.TABLE_EMP.setGeometry(QRect(0, 0, 800, 300))
        self.TABLE_EMP.horizontalHeader().setDefaultSectionSize(130)
        self.tabWidget.addTab(self.TAB_EMPLOYEES, "")
        self.TAB_PROG_SET = QWidget()
        self.TAB_PROG_SET.setObjectName(u"TAB_PROG_SET")
        self.textEdit = QTextEdit(self.TAB_PROG_SET)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(80, 20, 104, 31))
        self.toolsLabel = QLabel(self.TAB_PROG_SET)
        self.toolsLabel.setObjectName(u"toolsLabel")
        self.toolsLabel.setGeometry(QRect(0, 30, 71, 16))
        self.issueButton = QPushButton(self.TAB_PROG_SET)
        self.issueButton.setObjectName(u"issueButton")
        self.issueButton.setGeometry(QRect(190, 20, 75, 31))
        self.labelTextCreate = QLabel(self.TAB_PROG_SET)
        self.labelTextCreate.setObjectName(u"labelTextCreate")
        self.labelTextCreate.setGeometry(QRect(320, 100, 61, 31))
        self.textEdit_2 = QTextEdit(self.TAB_PROG_SET)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(410, 70, 231, 111))
        self.issueButtonCreate = QPushButton(self.TAB_PROG_SET)
        self.issueButtonCreate.setObjectName(u"issueButtonCreate")
        self.issueButtonCreate.setGeometry(QRect(670, 90, 75, 51))
        self.label = QLabel(self.TAB_PROG_SET)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 110, 61, 16))
        self.textEdit_header_bug = QTextEdit(self.TAB_PROG_SET)
        self.textEdit_header_bug.setObjectName(u"textEdit_header_bug")
        self.textEdit_header_bug.setGeometry(QRect(63, 70, 171, 111))
        self.label_2 = QLabel(self.TAB_PROG_SET)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 220, 91, 16))
        self.textEdit_3 = QTextEdit(self.TAB_PROG_SET)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(100, 210, 111, 31))
        self.buttonCommitDoc = QPushButton(self.TAB_PROG_SET)
        self.buttonCommitDoc.setObjectName(u"buttonCommitDoc")
        self.buttonCommitDoc.setGeometry(QRect(220, 212, 91, 31))
        self.label_3 = QLabel(self.TAB_PROG_SET)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 290, 221, 41))
        self.textBoxSha = QTextEdit(self.TAB_PROG_SET)
        self.textBoxSha.setObjectName(u"textBoxSha")
        self.textBoxSha.setGeometry(QRect(330, 300, 341, 31))
        self.buttonGetVersion = QPushButton(self.TAB_PROG_SET)
        self.buttonGetVersion.setObjectName(u"buttonGetVersion")
        self.buttonGetVersion.setGeometry(QRect(680, 300, 75, 31))
        self.tabWidget.addTab(self.TAB_PROG_SET, "")

        self.retranslateUi(gui)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(gui)
    # setupUi

    def retranslateUi(self, gui):
        gui.setWindowTitle(QCoreApplication.translate("gui", u"\u041a\u0443\u0440\u0441\u043e\u0432\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u0421\u0430\u0432\u043a\u0438\u043d, \u0423\u043c\u0443\u0440\u0433\u0443\u043b\u043e\u0432 3-421\u0411", None))
        ___qtablewidgetitem = self.TABLE_PROJECT_HEADER.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("gui", u"\u041f\u0440\u043e\u0435\u043a\u0442", None));
        ___qtablewidgetitem1 = self.TABLE_PROJECT_HEADER.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("gui", u"\u041a\u043e\u043c\u0430\u043d\u0434\u0430", None));
        ___qtablewidgetitem2 = self.TABLE_PROJECT_HEADER.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("gui", u"\u0417\u0430\u0434\u0430\u0447\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None));
        ___qtablewidgetitem3 = self.TABLE_PROJECT_HEADER.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("gui", u"\u041f\u043b\u0430\u0442\u0444\u043e\u0440\u043c\u0430", None));
        ___qtablewidgetitem4 = self.TABLE_PROJECT_HEADER.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("gui", u"\u041c\u0435\u0442\u043e\u0434 \u0441\u0432\u044f\u0437\u0438", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TAB_PROJECTS), QCoreApplication.translate("gui", u"\u041f\u0440\u043e\u0435\u043a\u0442\u044b", None))
        ___qtablewidgetitem5 = self.TABLE_PROJECT_NEWS.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("gui", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None));
        ___qtablewidgetitem6 = self.TABLE_PROJECT_NEWS.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("gui", u"\u041f\u0440\u043e\u0435\u043a\u0442", None));
        ___qtablewidgetitem7 = self.TABLE_PROJECT_NEWS.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("gui", u"\u041d\u043e\u0432\u043e\u0441\u0442\u044c", None));
        self.BUTTON_PROJECTS_2.setText(QCoreApplication.translate("gui", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.BUTTON_PROJECT_NEWS.setText(QCoreApplication.translate("gui", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0441\u0442\u044c", None))
        self.button_project_news_commit.setText(QCoreApplication.translate("gui", u"COMMIT!!!!!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TAB_NEWS), QCoreApplication.translate("gui", u"\u041d\u043e\u0432\u043e\u0441\u0442\u0438", None))
        ___qtablewidgetitem8 = self.TABLE_EMP.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("gui", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem9 = self.TABLE_EMP.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("gui", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None));
        ___qtablewidgetitem10 = self.TABLE_EMP.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("gui", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None));
        ___qtablewidgetitem11 = self.TABLE_EMP.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("gui", u"Email", None));
        ___qtablewidgetitem12 = self.TABLE_EMP.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("gui", u"\u0413\u0440\u0443\u043f\u043f\u0430", None));
        ___qtablewidgetitem13 = self.TABLE_EMP.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("gui", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TAB_EMPLOYEES), QCoreApplication.translate("gui", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.toolsLabel.setText(QCoreApplication.translate("gui", u"\u041d\u043e\u043c\u0435\u0440 \u0431\u0430\u0433\u0430:", None))
        self.issueButton.setText(QCoreApplication.translate("gui", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c", None))
        self.labelTextCreate.setText(QCoreApplication.translate("gui", u"\u0422\u0435\u043a\u0441\u0442 \u0431\u0430\u0433\u0430", None))
        self.issueButtonCreate.setText(QCoreApplication.translate("gui", u"\u0417\u0430\u0432\u0435\u0441\u0442\u0438 \u0431\u0430\u0433", None))
        self.label.setText(QCoreApplication.translate("gui", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a:", None))
        self.label_2.setText(QCoreApplication.translate("gui", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430:", None))
        self.buttonCommitDoc.setText(QCoreApplication.translate("gui", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0434\u043e\u043a", None))
        self.label_3.setText(QCoreApplication.translate("gui", u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0435 \u0432\u0435\u0440\u0441\u0438\u0438 \u043f\u0440\u043e\u0435\u043a\u0442\u0430. \u0412\u0432\u0435\u0434\u0438\u0442\u0435 SHA: ", None))
        self.buttonGetVersion.setText(QCoreApplication.translate("gui", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TAB_PROG_SET), QCoreApplication.translate("gui", u"\u0423\u0442\u0438\u043b\u0438\u0442\u044b", None))
    # retranslateUi



    