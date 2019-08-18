
from os.path import expanduser
import argparse
import subprocess

GIT_REMOTE= None


def create_repo:
    print "create repo"


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