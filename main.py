import os
from os.path import expanduser
import argparse
import subprocess
from config.config import Config
from bitbucket.client import Client

GIT_REMOTE= None
AUTH_CONFIG= None
PROJECT_CONFIG= None
PROJECT_DESC= None
PRIVATE= True
WORKING_DIR= "NewProject"
REPO_NAME= None

def create_repo():
    config = Config()
    AUTH_CONFIG = config.getAuthConfig()
    PROJECT_CONFIG = config.getProjectConfig()
    client = Client(AUTH_CONFIG['username'], AUTH_CONFIG['password'])
    data = {
        "scm": "git",
        "project": {
            "key": PROJECT_CONFIG['projectKey']
        },
        "is_private": PRIVATE
    }

    if (PROJECT_DESC):
        data['description'] = PROJECT_DESC

    response = client.post_repository(None, data, REPO_NAME, PROJECT_CONFIG['team'])
    if 'links' in response:
        return response['links']['clone'][0]['href']
    else:
        print response

def init():
    home = expanduser("~")
    path = home+"/Development/%s"%WORKING_DIR
    try:
        # Create target Directory
        os.mkdir(path)
        print("Directory " , path ,  " Created ") 
    except :
        print("Directory " , path ,  " already exists")

    GIT_REMOTE = create_repo()
    
    os.chdir(path)
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'remote', 'add', 'origin', GIT_REMOTE])
    subprocess.call(['touch', '.gitignore'])
    subprocess.call(['touch', 'README.md'])
    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', "'[INITIAL] first commit'"])
    subprocess.call(['git', 'push', '-u', 'origin', 'master'])
    subprocess.call(['code', '.'])

parser = argparse.ArgumentParser()
parser.add_argument('repo', metavar='REPO', type=str, help='Set repository name')
parser.add_argument('-n', metavar='Project Name', type=str, help='Set Project Name; default=true')
parser.add_argument('--c', metavar='Config', type=str, help='Init project config')
parser.add_argument('-p', metavar='private', type=bool, help='Set project privacy; default=true')
parser.add_argument('-d', metavar='description', type=str, help='Set project description')
args = parser.parse_args()

if not args.repo:
    print "ERROR: Repo name is missing"
else:
    REPO_NAME = args.repo
    if args.c:
        Config()

    if args.d:
        PROJECT_DESC = args.d

    if args.p:
        PRIVATE = args.p
    
    if args.n:
        WORKING_DIR = args.n

    init()