## NYC Department Of Transportation: Data Cleaning Error Log
<a href="url"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/NYCDOT.svg/1200px-NYCDOT.svg.png" align="middle" height="100"></a>

### Repository Overview

This repository contains a Python and Jupyter Notebook script that was developed for the NYC DOT that generates an error log for any data in the 'accessible-pedestrian-signals.xlsx' that does not clean correctly. Accessible Pedestrian Signals (APS) are devices affixed to pedestrian signal poles to assist blind or low vision pedestrians in crossing the street.  The excel file contains data on the location of these devices and data cleaning is required so that the data can be used for further application development.

Software Requirements/Dependencies
---
Confirm if Python 3 and PIP (package installer for python) installed on your local machine by running the following commands. If not, refer to the installation documentation for [Python 3](https://www.python.org/downloads/) and [PIP](https://pip.pypa.io/en/stable/installation/)

```bash
python3 --version
pip --version
``` 
Once Python 3 and PIP are installed, install the following python dependencies by running the following commands:
```bash
pip install notebook
pip install pandas
pip install regex
pip install pyspellchecker
``` 

Files in this repository:
---
> `DataCleaningErrorLog.ipynb` - the main script ran on JupyterLab as a notebook that allows user customization and provides more details on the errors.

> `DataCleaningErrorLog.py` - a version of the main script that can be run on terminal.

> `customdict.txt` - a txt file that contains numerical street names and other words that should pass  pyspellcheck.

> `streetdict.txt` - a txt file from NYC Open Data that contains an official NYC Street Name Dictionary.


