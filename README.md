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
    
## FOR LATER
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
    
