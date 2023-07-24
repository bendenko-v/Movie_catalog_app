# Movie Catalog App

This is a Movie Catalog App that allows users to explore movies, directors, and genres.
The backend is built with Flask-RESTx and provides functionalities like user registration, login, and authentication
using JWT tokens.
The frontend is developed with React and provides an intuitive user interface to interact with the movie catalog.

![Main page](https://habrastorage.org/webt/i0/1a/qn/i01aqntzdkhdw5ou2ekdo27ct-i.jpeg)

## Usage

1. Install dependencies `pip install -r requirements.txt`
2. Create a `.env` file with the following parameters:
    ```
    SECRET_KEY=<secret key for flask app>
    FLASK_APP=run.py
    FLASK_ENV=production
    TOKEN_EXPIRE_MINUTES=<minutes>
    TOKEN_EXPIRE_DAYS=<days>
    HASH_ITERATIONS = <hash iterations>
    SALT=<salt>
    ```
3. To run the backend, use the following command: `flask run`.
4. The backend will be accessible at http://localhost:5000.
5. The frontend is hosted in a Docker container. To set up the frontend, follow these steps:
    - Download the Docker image using the command: `docker pull painassasin/node_cource_project:latest`
    - Run the container on port 80 using: `docker run -p 80:80 painassasin/node_cource_project`
6. Open the frontend in your web browser by visiting http://localhost

## Functionality

The Movie Catalog App provides the following functionalities:

- User Registration and Login:
- Users can create an account and log in to access personalized features.
- JWT Token Authentication: Authentication is handled using JWT tokens for secure access to protected routes.
- User Profile: Users can view and edit their profile information, including name, surname, and favorite genre.
- Change Password: Users can change their account password securely.
- Movie Catalog: The app displays a list of movies starting with the latest releases.
- Genres and Directors: Users can explore genres and directors available in the movie catalog.
- Favorites: Users can add movies to their favorites list. (Note: Frontend functionality for favorites is still in
  progress.)
