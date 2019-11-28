import enum
from ruamel import yaml
from typing import Optional, List
import yatiml


class Identifier:

    class Type(enum.Enum):
        doi = enum.auto
        url = enum.auto
        swh = enum.auto
        other = enum.auto

    def __init__(self, type: Type, value: str):
        self.type = type
        self.value = value


class Author:
    def __init__(self, given_names: Optional[str] = None, name_particle: Optional[str] = None,
                 family_names: Optional[str] = None, name_suffix: Optional[str] = None,
                 affiliation: Optional[str] = None, orcid: Optional[str] = None) -> None:

        self.given_names = given_names
        self.name_particle = name_particle
        self.family_names = family_names
        self.name_suffix = name_suffix
        self.affiliation = affiliation
        self.orcid = orcid


class Schema(Author):
    def __init__(self, cff_version: str, message: str, authors: List[Author],
                 identifiers: Optional[List[Identifier]] = None):

        self.cff_version = cff_version
        self.message = message
        self.authors = authors
        self.identifiers = identifiers


# Create loader
class MyLoader(yatiml.Loader):
    pass


yatiml.add_to_loader(MyLoader, [Identifier, Author, Schema])
yatiml.set_document_type(MyLoader, Schema)

# Load YAML
yaml_text = 'cff_version: 1.1.0\n' \
            'message: this is the message\n' \
            'authors:\n' \
            '  - given_names: John\n' \
            '    name_particle: von\n' \
            '    family_names: Neuman\n' \
            '    name_suffix: III\n' \
            '    affiliation: hierzo\n' \
            '  - given_names: Janice\n' \
            '    affiliation: hierzo\n' \
            '    orcid: https://orcid.org/111.231231212\n' \
            '  - given_names: Janice\n' \
            '    affiliation: hierzo\n' \
            '  - given_names: John\n' \
            'identifiers:\n' \
            '  - type: url\n' \
            '    value: \n'


doc = yaml.load(yaml_text, Loader=MyLoader)

print('done')



