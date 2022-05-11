from inspect import getsourcefile
import os.path
import sys

def ch():
    current_path = os.path.abspath(getsourcefile(lambda:0))
    current_dir = os.path.dirname(current_path)
    parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

    sys.path.insert(0, parent_dir)
    import GHOSTKILLER
    
ch()
