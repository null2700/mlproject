# setup.py
from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> list[str]:
    '''This function returns a list of requirements from the given file.'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]  # remove \n
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='soham',
    author_email='guravsoham182@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
