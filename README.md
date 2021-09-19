# COCCIEP
## cs50-final-project
### Final Project for CS50 - 2021

Authors: albertoturrion and brunosra
### Instructions
#### Clone project:
`git clone https://github.com/brunosra/cs50-final-project.git`

#### Create Virtual Environment:
Mac: `python3 -m venv venv`
Windows: `py -3 -m venv venv`

#### Activate Virtual Environment:
Mac: `. venv/bin/activate`
Windows: `venv\Scripts\activate`

#### Install dependencies:
`pip install -r requirements.txt`
#### Quit ENV:
`deactivate`
#### Activate Virtual Environment Again:
Mac: `source venv/bin/activate`
Windows: `venv\Scripts\activate`
#### Prepare variables:
`export FLASK_APP=cocciep FLASK_ENV=development`
#### Create DB:
`flask db init`
#### Run Latest Migration:
`flask db upgrade`
#### Run Project:
`flask run`