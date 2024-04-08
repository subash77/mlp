from setuptools import find_packages,setup
from typing import List

Hyphen_E_Dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    Requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n'," ") for req in requirements]

        if Hyphen_E_Dot in requirements:
            requirements.remove(Hyphen_E_Dot)

    return requirements





setup(
    name='mlp',
    version='0.0.1',
    author='subash',
    author_email='subashchella15@gmail.com',
    packages=find_packages(),
    install_requires=[get_requirements('requirements.txt')]

)