from github import Github
from github import InputGitTreeElement
import json
import requests
import zipfile

class Git_tools():

    def __init__(self):    
        self.access_token = "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"
        self.g = Github(self.access_token)
        self.user = self.g.get_user()
        self.repo = self.user.get_repo("kursach2023")
    
    def get_bug(self,number):
        issue = self.repo.get_issue(number=1)
        filename = "bugs/BUG-"
        filename = filename + number + ".json"
        
        body_is = json.dumps(issue.raw_data)        
        
        with open(filename, 'a') as f:
            f.write(body_is)
            
            for i in issue.get_comments():
                body_com = json.dumps(i.raw_data)
                f.write(body_com)
    
    def create_bug(self,header,text):
        title = "BUG " + header
        self.repo.create_issue(title=title, body=text)

    def upload_tech_doc(self,filename):
        file_list = []
        file_list.append(filename)
        file_names = []
        str_file_name = 'documents/' + filename
        file_names.append(str_file_name)
        commit_message = 'doc commit'
        master_ref = self.repo.get_git_ref('heads/main')
        master_sha = master_ref.object.sha
        base_tree = self.repo.get_git_tree(master_sha)
        element_list = list()

        for i, entry in enumerate(file_list):
            with open(entry) as input_file:
                data = input_file.read()
            element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
            element_list.append(element)

        tree   = self.repo.create_git_tree(element_list, base_tree)
        parent = self.repo.get_git_commit(master_sha)
        commit = self.repo.create_git_commit(commit_message, tree, [parent])
        master_ref.edit(commit.sha)
    
    def get_version(self,sha):
        ref = 'https://github.com/savkind/kursach2023/archive/{sha}.zip'
        r = requests.get(ref, allow_redirects=True)
        open("object.zip", "wb").write(r.content)
        z = zipfile.ZipFile('object.zip', 'r')
        path = z.filelist[0].filename.rpartition('/')[0]
