from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        data = toml.loads(content)

        poetry_data = data['tool']['poetry']
        name = poetry_data['name']
        description = poetry_data['description']
        authors = poetry_data['authors']
        license = poetry_data['license']
        dependencies = list(poetry_data['dependencies'].keys())
        dev_dependencies = list(poetry_data['group']['dev']['dependencies'].keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)
