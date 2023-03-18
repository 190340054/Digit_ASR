import os
from dotenv import load_dotenv

load_dotenv()

#sample testing for correct path
# print(os.environ['train_path'])

def check_folder():
    """
    this is documenation space 
    """
    #check does we have cleaning dir
    if os.path.exits(os.environ[clean_path]):
        #we will do something
        pass
    else:
        os.mkdir(os.environ[clean_path])

def read_files():
    """
    this is documenation space
    """
