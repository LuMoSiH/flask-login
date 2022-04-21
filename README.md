# flask-login
[Python]

Basic python example login using flask + sqlite3 + session control.
Check the "requirements.txt" file

🛠️ Installation Steps <br>
1 - Create VM (python -m venv venv)<br>
2 - Create db <br>
3 - Create Table <br>
`CREATE TABLE users (
    id       INTEGER       PRIMARY KEY AUTOINCREMENT
                           NOT NULL
                           UNIQUE,
    login    VARCHAR (255) UNIQUE
                           NOT NULL,
    password VARCHAR (255) NOT NULL
);`<br>
4 - Install requeriments.txt