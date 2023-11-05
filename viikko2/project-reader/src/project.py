class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors:\n- " + "\n- ".join(self.authors) +
            f"\n\nDependencies:\n" + '\n'.join(f"- {item}" for item in self.dependencies if item) +
            f"\n\nDevelopment dependencies:\n" + '\n'.join(f"- {item}" for item in self.dev_dependencies if item)
        )
