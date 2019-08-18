try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

class Config():
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('config.ini')

        if (not self.config.sections()):
            self.createSections()

    def createSections(self):
        working_dir = raw_input("Project Name: ") 
        username = raw_input("Bitbucket Username: ")
        password = raw_input("Bitbucket Password: ")
        projectKey = raw_input("Project Key: ")
        team = raw_input("Team: ")

        config = ConfigParser()
        config.read('config.ini')
        config.add_section('AUTH')
        config.set('AUTH', 'username', username)
        config.set('AUTH', 'password', password)

        config.add_section('PROJECT')
        config.set('PROJECT', 'projectName', working_dir)
        config.set('PROJECT', 'projectKey', projectKey)
        config.set('PROJECT', 'team', team)

        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def getAuthConfig(self):
        return {
            "username": self.config.get('AUTH', 'username'),
            "password": self.config.get('AUTH', 'password')
        }
    
    def getProjectConfig(self):
        return {
            "projectKey": self.config.get('PROJECT', 'projectKey'),
            "team": self.config.get('PROJECT', 'team')
        }