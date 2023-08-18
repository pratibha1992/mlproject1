from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    HYPEN_E_DOT='-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements



setup(
name='MLPROJECT1',
version='0.0.1',
author='{Pratibha}',
author_email='ckpratibha1@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)