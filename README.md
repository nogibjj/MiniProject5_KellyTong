# IDS 706 Mini Project 5

This repository is for IDS706 mini project week 5. 

## Purpose 
    This repository is for building an ETL-Query pipeline. Github actions such as extract, transform and load, and query are included. A local csv file is extracted from a url and then cleaned and loaded into a .db file. SQLlite is used to query it. 
    
## Important Things included are:
- ``.devcontainer`` includes a Dockerfile and devcontainer.json.
                The 'Dockerfile' within this folder specifies how the container should be built

- ``workflows`` includes CI.yml, which contain configuration files for setting up automated build, test, and deployment pipelines

- ``.gitignore`` is used to specify which files or directories should be excluded from version control when using Git.

- ``Makefile`` is a configuration file used in Unix-based systems for automating tasks and building software. It contains instructions and dependencies for compiling code, running tests, and other development tasks.

- ``README.md`` is the instruction file for the readers.

- ``main.py`` is a Python file. This specific main.py gets the python versions and operation system names. 

- ``requirements.txt`` is to specify the dependencies (libraries and packages) required to run the project.

- ``test_main.py`` is a test file for main.py

## Github actions
Status badges for CI.yml
`CI.yml`
[![CI](https://github.com/nogibjj/Kelly_Tong_miniproject4/actions/workflows/CI.yml/badge.svg)](https://github.com/nogibjj/Kelly_Tong_miniproject4/actions/workflows/CI.yml)

## The Building Process (example) 

`make install`

The building process starts with installing the packages. 

**Make install** calls the command pip install --upgrade pip &&\pip install -r requirements.txt

`make lint`

**Make lint** calls the command pylint --disable=R,C --ignore-patterns=test_.*?py *.py
<img width="457" alt="make lint" src="https://github.com/Kelly0604/miniproject2/assets/142815940/39a19764-a6cc-4eaa-977f-7433b8915dad">

`make test`

**Make test** calls the command python -m pytest -vv --cov=main test_*.py
<img width="851" alt="截屏2023-09-23 21 38 15" src="https://github.com/nogibjj/Kelly_Tong_miniproject4/assets/142815940/e1e570b5-f7b8-4cf3-b9e4-073e91611716">

`make format`

**Make format** calls the command black *.py

<img width="299" alt="make format" src="https://github.com/Kelly0604/miniproject2/assets/142815940/41df08ca-d8f7-4b62-b88b-1f39f1a7d858">
