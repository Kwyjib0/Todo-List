
# <h1><div align="center">To-Do List</div></h1>  
<br>
## Python / Django App for creating and editing a todo list


## <div align="center">Installation/Requirements</div>
#### <div align="center">To-Do List requires [Python](https://www.python.org/) v3.9+ and [Django](https://www.djangoproject.com/) to run.</div>
***

# How to run To-Do List:

## In your Terminal:
### 1. Create a directory where you will run a virtual environment. The files for running the virtual environment will be saved in this directory:
```
mkdir <name-of-your-directory>
cd <name-of-your-directory>
```
### 2. Create a virtual environment:
Inside the root folder of the repository, `<name-of-your-directory>`, run:
```
python -m venv <name-of-your-virtual-environment>
or 
python3 -m venv <name-of-your-virtual-environment>
```
### 3. Run the virtual environment:
##### On Windows:

```
<name-of-your-directory>\Scripts\activate.bat  
or  
<name-of-your-directory>\Scripts\activate.ps1
```
##### On Unix, Linux or MacOS:
```
source <name-of-your-virtual-environment>/bin/activate
```
### 4. Install Django:
Inside the root folder of the repository, `<name-of-your-directory>`, run:
```
pip install django
```
### 5. Install dependencies:
Inside the root folder of the repository, `<name-of-your-directory>`, run:
```
pip install -r requirements.txt
or 
pip freeze > requirements.txt
```
### 6. Run Open Studios:
Make sure your virtual environment is running, then in the directory containing manage.py, run:
```
python manage.py runserver
```
go to  http://127.0.0.1/8000 to launch the Open Studios app

### 7. To deactivate the virtual environment when done:
```
deactivate
or
<name-of-your-directory>\Scripts\deactivate.bat
or
<name-of-your-directory>\Scripts\deactivate.ps1
```
---
## Using the To-Do List app:
### 1. This app requires user registration and log in
### 2. Tasks can be added, edited, and deleted
### 3. Tasks can be viewed as a list and individually with a more detailed description



---
***

Copyright (c) 5/12/2021 Chris Linton


