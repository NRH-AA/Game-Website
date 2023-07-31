This project was created for use with the latest The Forgotten Server (TFS). Seperate branches will be made for compatibility with other servers and versions. If you would like a branch designed for a specific server or version create an issue in the issue tab. 

The title should be:
Server Name - Server version

Please include any information on the differences in database structure, ect. (not required)

If there is enough interest in the version and server it will be added to development.

<br></br>
Windows Required Downloads: <br>
[NodeJS](https://nodejs.org/en)<br>
[Python 3.11.4 or higher](https://www.python.org/downloads/)<br>
[pip](https://pypi.org/project/pip/#files)


<br></br>
Linux Required Downloads:<br>
`sudo apt update && sudo apt upgrade` <br>
`sudo apt install nodejs`<br>
`sudo apt-get install python3.6`<br>
`sudo apt install python3-pip`<br>
`sudo pip install --upgrade pip`

<br></br>
Running the server (backend):<br>
`pipenv install` <br>
`pipenv install Flask python-dotenv wtforms Flask-WTF SQLAlchemy Flask-SQLAlchemy alembic Flask-Migrate` <br>
`pipenv run flask run`

Running the server (frontend):<br>
`cd frontend`<br>
`npm i`<br>
`npm start`
