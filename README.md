## NYC-DOT-Data_Cleaning_Error_Log
 
### Repository Overview

This repository contains a script that generates an error log for any data in the 'accessible-pedestrian-signals.xlsx' that does not clean correctly. NYC DOT's Accessible Pedestrian Signals (APS) are devices affixed to pedestrian signal poles to assist blind or low vision pedestrians in crossing the street. APSs are wired to a pedestrian signal and send audible and vibrotactile indications when pedestrians push a button installed at the crosswalk. The file contains data on the location of these devices and cleaning is required so that the data can be used for geocoding.

### Python 3 Requirements/Dependencies
*pip install jupyterlab
*pip install pandas
*pip install regex
*pip install pyspellchecker

Files in this repository:

> `accessible-pedestrian-signals.xlsx` - test data acquired to develop script.

> `customdict.txt` - a txt file that contains numerical street names and other words that should pass  pyspellcheck.

> `streetdict.txt` - a txt file from NYC Open Data that contains an official NYC Street Name Dictionary.

> `DataCleaningErrorLog.py` - a version of the main script that can be run on terminal.

> `DataCleaningErrorLog.ipynb` - the main script ran on JupyterLab as a notebook that allows user customization and provides more details on the errors. 
