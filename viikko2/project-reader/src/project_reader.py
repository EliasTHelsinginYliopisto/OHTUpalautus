from urllib import request
from toml import loads
from project import Project

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        parsed_toml = loads(content)
        #print(parsed_toml)

        name = parsed_toml["tool"]["poetry"]["name"]
        description = parsed_toml["tool"]["poetry"]["description"]
        dependencies = parsed_toml["tool"]["poetry"]["dependencies"]
        development_dependencies = parsed_toml["tool"]["poetry"]["dev-dependencies"]


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, development_dependencies)
