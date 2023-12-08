import os
from os.path import join
from pprint import pprint
import shutil
import urllib.request
import json
from pprint import pprint


metadata = open("meta-data.json","r")

projects = json.load(metadata)

metadata.close()

for project in projects:
    os.makedirs(project["subject"],exist_ok=True)
    os.makedirs(join(project["subject"],project["bug_id"]),exist_ok=True)

    shutil.copy2("build_subject",join(project["subject"],project["bug_id"],"build_subject"))
    shutil.copy2("clean_subject",join(project["subject"],project["bug_id"],"clean_subject"))
    shutil.copy2("compress_deps",join(project["subject"],project["bug_id"],"compress_deps"))
    shutil.copy2("config_subject",join(project["subject"],project["bug_id"],"config_subject"))
    shutil.copy2("install_deps",join(project["subject"],project["bug_id"],"install_deps"))
    shutil.copy2("test_subject",join(project["subject"],project["bug_id"],"test_subject"))
    shutil.copy2("setup_subject",join(project["subject"],project["bug_id"],"setup_subject"))
    shutil.copy2("verify_dev",join(project["subject"],project["bug_id"],"verify_dev"))
    

    os.system("sed -i 's/<BRANCH>/{}/' {}".format(project['bug_id'],join(project["subject"],project["bug_id"],"setup_subject")))