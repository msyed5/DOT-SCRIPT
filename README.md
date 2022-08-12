# NYC Department Of Transportation: Data Cleaning Error Log
<a href="url"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/NYCDOT.svg/1200px-NYCDOT.svg.png" align="middle" height="100"></a>

## Repository Overview

This repository contains a script that was developed for the NYC DOT that generates an error log for any data in the 'accessible-pedestrian-signals.xlsx' that does not clean correctly. Accessible Pedestrian Signals (APS) are devices affixed to pedestrian signal poles to assist blind or low vision pedestrians in crossing the street.  The excel file contains information on the location of these devices and data cleaning is required so that the data can be used for further application development.

A sample of the dataset can be downloaded from the [NYC City Goverment Website](https://www1.nyc.gov/html/dot/html/infrastructure/accessiblepedsignals#:~:text=NYC%20DOT's%20Accessible%20Pedestrian%20Signals,button%20installed%20at%20the%20crosswalk.) and is previewed below:

<img src="https://github.com/msyed5/DOT-SCRIPT/blob/main/img/sample-data.png" height="400">

### Files in this repository:
> `DataCleaningErrorLog.ipynb` - the main script ran on Jupyter Notebook that allows provides a full error log. 

> `DataCleaningErrorLog.py` - a version of the main script that can be run on terminal. 

> `customdict.txt` - a txt file that contains numerical street names and custom words that should pass pyspellcheck. User can edit this file to add any words that should pass spell check that is not included in the current dictionaries.

> `streetdict.txt` - a txt file from NYC Open Data that contains an official NYC Street Name Dictionary. Data has been cleaned to remove numeric characters from alphanumeric street names.

> `/img` - images used in README.md file to preview sample data and script.


### Prerequisites
Confirm Python 3 and PIP (package installer for python) are installed on your local machine by running the following commands. If not, refer to the installation documentation for [Python 3](https://www.python.org/downloads/) and [PIP](https://pip.pypa.io/en/stable/installation/)

```bash
python3 --version
pip --version
``` 
Once Python 3 and PIP are installed, clone the project to your desired local directory and install the python dependencies by running the following commands:
   ```sh
   git clone https://github.com/msyed5/DOT-SCRIPT.git
   ```

```bash
pip install notebook
pip install pandas
pip install regex
pip install pyspellchecker
``` 
### Instructions for Usage: Running Jupyter Notebook Script

1. Confirm the target excel file is named 'accessible-pedestrian-signals.xlsx'. Add the file to the project directory using your file manager
2. Use terminal to navigate to the project directory 
   ```sh
    cd DOT-SCRIPT
    pwd
   ```
3. Open the Jupyter Notebook Script 
   ```sh
    jupyter notebook DataCleaningErrorLog.ipynb
   ```
4. Navigate to the Jupyter Notebook menu bar and run the script --> Kernel > Restart and Run All
5. Scroll through the notebook to view error logs for each error type or go to the end of the notebook to view the full error log
6. Errors can be corrected manually or with a seperate Data Cleaning Script (Link here when ready)

## Instructions for Usage: Running Terminal Version of Script
1. Confirm the target excel file is named 'accessible-pedestrian-signals.xlsx'.  Add the file to the project directory using your file manager.
2. Use terminal to navigate to the project directory 
   ```sh
    cd DOT-SCRIPT
    pwd
   ```
3. Run the Python Script 
   ```sh
    python DataCleaningErrorLogTerminal.py
   ```
4. Terminal will output an abridged version of the full error script
6. Errors can be corrected manually or with a seperate Data Cleaning Script (Link here when ready)

### Workflow Overview

The diagram below provides an overall process digram of the script.

![Workflow](img/workflow_overview.png)

### Resources


