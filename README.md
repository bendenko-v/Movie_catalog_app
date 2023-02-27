# SkyPro / Coursework 4

Movie catalog application on Flask-RESTX with user registration.

## Usage
- Install dependencies
```shell
pip install -r requirements.txt
```

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
* Аdding/removing movies to favorites does not work on the front (redirect to /login)