import psycopg2
from psycopg2 import Error

class Database_tools(object):

    __instance = None

    @staticmethod
    def inst():

        if Database_tools.__instance == None:
            Database_tools.__instance = Database_tools()

        return Database_tools.__instance

    def read_table(self,table):
        command = "SELECT * FROM " + table
        self.cursor.execute(command)
        record = self.cursor.fetchall()
        return record

    def get_project_new(self):
        command = "SELECT project_new.id_project, name, text FROM project_new INNER JOIN project_header on project_header.id_project = project_new.id_project"
        self.cursor.execute(command)
        record = self.cursor.fetchall()
        return record

    def get_project_header(self):
        command = "SELECT name, name_group, task, platform, communication_method FROM project_header INNER JOIN project_group ON project_header.id_group = project_group.id_group"
        self.cursor.execute(command)
        record = self.cursor.fetchall()
        return record
    
    def get_emp000(self):
        command = "SELECT firstname, lastname, email, phone FROM emp000"
        self.cursor.execute(command)
        record = self.cursor.fetchall()
        return record
    
    def get_emp000_f1(self, filter):
        command = f"SELECT firstname, lastname, email, phone, name_group, active FROM emp000 INNER JOIN project_group ON emp000.id = project_group.id_emp WHERE name_group = '{filter}'"
        self.cursor.execute(command)
        record = self.cursor.fetchall()
        return record

    def insert_project_new(self, id_p, t):
        #command = f"INSERT INTO project_new(id_project, text) VALUES ({id_p},{t})"
        command = "INSERT INTO project_new(id_new,id_project, text) VALUES (DEFAULT,%s,%s)"
        record_to_insert = (id_p, t)
        self.cursor.execute(command, record_to_insert)
        self.connection.commit()


    def __init__(self):
            self.connection = psycopg2.connect(user="postgres",
                                      password="root",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="course_work")

            self.cursor = self.connection.cursor()


    def __del__(self):
        self.connection.close()
        
        

