from PyQt6.QtWidgets import QMainWindow
from Database_tools import *
from gui import *
from Git_tools import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_gui() 
        self.ui.setupUi(self)

        self.database_cw = Database_tools.inst()
        self.git_con     = Git_tools()

        self._init_table_project_new()
        self._init_table_project_header()
        self._init_table_emp000()

        self.ui.TABLE_PROJECT_HEADER.itemClicked.connect(self.project_header_column_clicked)
        self.ui.BUTTON_PROJECT_NEWS.clicked.connect(self.add_project_news)
        self.ui.button_project_news_commit.clicked.connect(self.project_news_commit)
        self.ui.issueButton.clicked.connect(self.get_bug)
        self.ui.issueButtonCreate.clicked.connect(self.create_bug)
        self.ui.buttonCommitDoc.clicked.connect(self.upload_doc)


    def _init_table_project_new(self):

        news = self.database_cw.get_project_new()

        for n in news:
            i = 0
            self.ui.TABLE_PROJECT_NEWS.insertRow(i)

            self.ui.TABLE_PROJECT_NEWS.setItem(i,0, QTableWidgetItem(str(n[0])))
            self.ui.TABLE_PROJECT_NEWS.setItem(i,1, QTableWidgetItem(str(n[1])))
            self.ui.TABLE_PROJECT_NEWS.setItem(i,2, QTableWidgetItem(str(n[2])))

            i = i + 1
        
    
    def _init_table_project_header(self):

        projects = self.database_cw.get_project_header()

        for p in projects:
            i = 0
            self.ui.TABLE_PROJECT_HEADER.insertRow(i)

            self.ui.TABLE_PROJECT_HEADER.setItem(i,0, QTableWidgetItem(str(p[0])))
            self.ui.TABLE_PROJECT_HEADER.setItem(i,1, QTableWidgetItem(str(p[1])))
            self.ui.TABLE_PROJECT_HEADER.setItem(i,2, QTableWidgetItem(str(p[2])))
            self.ui.TABLE_PROJECT_HEADER.setItem(i,3, QTableWidgetItem(str(p[3])))
            self.ui.TABLE_PROJECT_HEADER.setItem(i,4, QTableWidgetItem(str(p[4])))

            i = i + 1
    
    def _init_table_emp000(self):

        emp = self.database_cw.get_emp000()

        for e in emp:
            i = 0
            self.ui.TABLE_EMP.insertRow(i)

            self.ui.TABLE_EMP.setItem(i,0, QTableWidgetItem(str(e[0])))
            self.ui.TABLE_EMP.setItem(i,1, QTableWidgetItem(str(e[1])))
            self.ui.TABLE_EMP.setItem(i,2, QTableWidgetItem(str(e[2])))
            self.ui.TABLE_EMP.setItem(i,3, QTableWidgetItem(str(e[3])))
            self.ui.TABLE_EMP.setItem(i,4, QTableWidgetItem("-"))

            i = i + 1
       
    def project_header_column_clicked(self,item):

        value = self.ui.TABLE_PROJECT_HEADER.model().data(self.ui.TABLE_PROJECT_HEADER.currentIndex())
        col =   self.ui.TABLE_PROJECT_HEADER.indexFromItem(item).column()

        if value and col == 1:
            emp = self.database_cw.get_emp000_f1(value)

            self.ui.TABLE_EMP.clearContents()

            for e in emp:
                i = 0

                self.ui.TABLE_EMP.insertRow(i)

                self.ui.TABLE_EMP.setItem(i,0, QTableWidgetItem(str(e[0])))
                self.ui.TABLE_EMP.setItem(i,1, QTableWidgetItem(str(e[1])))
                self.ui.TABLE_EMP.setItem(i,2, QTableWidgetItem(str(e[3])))
                self.ui.TABLE_EMP.setItem(i,3, QTableWidgetItem(str(e[2])))
                self.ui.TABLE_EMP.setItem(i,5, QTableWidgetItem(str(e[5])))
                self.ui.TABLE_EMP.setItem(i,4, QTableWidgetItem(str(e[4])))

                i = i + 1
    
    def add_project_news(self):
        rowPosition = self.ui.TABLE_PROJECT_NEWS.rowCount()
        self.ui.TABLE_PROJECT_NEWS.insertRow(rowPosition)

    def project_news_commit(self):
        rowPosition = self.ui.TABLE_PROJECT_NEWS.rowCount() 
        rowPosition -= 1
        id_p = self.ui.TABLE_PROJECT_NEWS.item(rowPosition, 0).text()
        t = self.ui.TABLE_PROJECT_NEWS.item(rowPosition, 2).text()
        self.database_cw.insert_project_new(id_p, t)
    
    def get_bug(self):
        number = self.ui.textEdit.toPlainText()
        if number.isdigit():
            self.git_con.get_bug(number)
    
    def create_bug(self):
        text = self.ui.textEdit_2.toPlainText()
        header = self.ui.textEdit_header_bug.toPlainText()
        self.git_con.create_bug(header,text)

    def upload_doc(self):
        filename = self.ui.textEdit_3.toPlainText()
        self.git_con.upload_tech_doc(filename)







            


        
    

        
        

