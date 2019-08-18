
import argparse


def init():
    print 'init'

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