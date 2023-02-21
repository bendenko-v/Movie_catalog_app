# SkyPro / Coursework 4

Movie catalog application on Flask-RESTX with user registration.

## Usage
- Install dependencies
```shell
pip install -r requirements.txt

pip install -r requirements.dev.txt
```

- Create models (will clear the database and create all the models specified in the import)
```shell
python create_tables.py
```

- Loading data into the database
```shell
python load_fixtures.py
```
The script reads the fixtures.json file and loads the data into the database. If the data has already been loaded, it displays an appropriate message.

## App run

### Bash (Linux/MACOS)
```shell
export FLASK_APP=run.py
export FLASK_ENV='development'
flask run
```

### CMD (Windows)
```shell
set FLASK_APP=run.py
set FLASK_ENV=development
flask run
```

### PowerShell (Windows)
```shell
$env:FLASK_APP = "run"
$env:FLASK_ENV = "development"
flask run
```

## Run tests
```shell
pytest .
```

## Known issues
* Some problems with registration/authorization through the front
* Front not working properly - problems occur when trying to access pages with a specific movie (/movies/id, director (/directors/id, genre (/genres/id)
* The Users API namespace does not yet work as specified in the assignment (old variant)