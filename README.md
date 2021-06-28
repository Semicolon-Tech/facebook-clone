# facebook-clone

# Requirements

## Functional
- Users can share, like, comment, delete, update post
- Users can add and remove friends
- Users can change post access to public/private
- Users can see news feeds
- Users can search for friends
- Users can share profile
- Users can delete account

## Non Functional
- Application should be secure
- The application should be available

## Database Design
- POST
    - id: bigint, autoincrement, primary
    - text: text
    - author: USER
    - created_on: datetime
    - updated_on: datetime
    
- POST_MEDIA
    - id: bigint
    - file: varchar(url)
    - post: POST
    - created_on: datetime
    - updated_on: datetime
    
- USER
    - id: bigint, autoincrement, primary
    - username: varchar(20)
    - email: varchar(128)
    - created_on: datetime
    - updated_on: datetime
    
- PROFILE
    - id: bigint, autoincrement, primary
    - owner: USER
    - image: varchar(url)
    - address: ADDRESS
    - created_on: datetime
    - updated_on: datetime

- COMMENT
    - id: bigint, autoincrement, primary
    - text: text
    - author: USER
    - created_on: datetime
    - updated_on: datetime
    
- LIKE
    - id: bigint, autoincrement, primary
    - post: POST
    - owner: USER
    - created_on: datetime
    - updated_on: datetime
    
- FRIEND
    - id: bigint, autoincrement, primary
    - user: USER
    - befriended: USER
    - created_on: datetime
    - updated_on: datetime
    
### FOR LATER
- PROFILE
    - address: ADDRESS
    
- ADDRESS
    - id: bigint, autoincrement, primary
    - zip_code
    - country:
    - created_on: datetime
    - updated_on: datetime
    

## API Design
The api Documentation is hosted [here](https://documenter.getpostman.com/view/9430266/TzefAidZ#d4cff8b9-492b-483a-b77b-9baf40c453cd)

## APP STRUCTURE
- POSTS
    - POST
    - POST_MEDIA
    - COMMENT
    - LIKE
    
- USERS
    - USER
    - FRIEND
    - PROFILE
    
### Tools and Resources
1. Python 3.6+
2. Virtualenv
3. Postgresql 
    1. Download the application [link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads). 
    2. Install Postgresql and set up root (postgres). [link](https://www.postgresqltutorial.com/install-postgresql/)
    3. Set up two databases namely __uuid_db__ and __uuid_test_db__.
    

Make sure to download/clone this repository and navigate to the folder in your terminal. Now follow the instructions below

1. Create the virtual environment.
```
    virtualenv /path/to/venv --python=/path/to/python3
```
You can find out the path to your `python3` interpreter with the command `which python3`.

2. Set up `.env` file by duplicating the `.example.env` file(and editing if required).

3. Activate the environment and install dependencies.
    - #### Linux
    ```
        source /path/to/venv/bin/activate
        pip install -r requirements\dev.linux.txt
    ```

    - #### Windows
    ```
        ./path/to/venv/bin/activate
        pip install -r requirements\dev.windows.txt
    ```

4. Launch the service
```
    uvicorn main:app --workers 1 --host 0.0.0.0 --port 8008
```

## Posting requests locally
When the service is running, try this link in your browser/Postman. send a GET request
```
    127.0.0.1:8008/uuid
```

You can test the project with pytest by running the command. You can check Github Actions for the status of tests [here](https://github.com/iamr0b0tx/uuid-api/actions) 
```
    pytest
```
