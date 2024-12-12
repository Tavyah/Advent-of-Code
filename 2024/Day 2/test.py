import sys
import os

# Legg til 'Modules'-mappen til sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Modules')))
print(sys.path)  # Verifiser at stien er lagt til

from filehandler_helper import *
print("Import successful!")
