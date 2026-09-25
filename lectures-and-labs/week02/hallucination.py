import pandas as pd

# C:\Python314\python.exe: can't open file 'C:\Users\qahra\OneDrive - Atlantic TU\26-27\ai-assisted-programming-module\Week 1\ai-assisted-programming-module\lectures-and-labs\week02\setup_lab\hallucination.py': [Errno 2] No such file or directory

def load_spreadsheet(filepath: str):
    """Load a spreadsheet using the fast Excel reader."""
    return pd.read_excel_fast(filepath)

# Does pandas.read_excel_fast actually exist?
# No — pandas.read_excel_fast does not exist in the installed pandas version.