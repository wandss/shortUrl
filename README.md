# shortenUrl Project

## Description
This is a Django GraphQL API service, used to create short urls.

Users sends an url address to the backend and a shorted version of this url will be created.

When querying the API for an specific url, it's shorted version will be retrieved.

Trying to access the system with the short version of the url, will redirect the user to the the original url.

## Technical Notes
### Architectural decisions

I decided to divide this project in two, each representing, one architectural option.
- First scenario: Urls are stored and retrieved in Redis. **(branch master)**
- Second scenario: Urls are persisted in relational databases. **(branch version2-no-redis)**

### How to install:
1. [Clone this project](https://github.com/wandss/shortenUrl.git)
2. Create an [virtualenv](https://virtualenv.pypa.io/en/latest/). Not required, but **highly** recommended
3. Inside project's root directory run (after activating virtualenv):
```
pip install -r requirements.txt
```
4. Enter in the project directory (sevenGeese directory), same level as **manage.py** script and run:
```
python manage.py migrate
python manage.py makemigrations urlShortener
python manage.py migrate
```
### How to run the project
1. Inside the same directory from step 4 above, run:
```
python manage.py runserver
```
**Take note at the address showed at prompt**

2. Open a web browser
3. Acces the address showed at the prompt, probably **http://127.0.0.1:8000/graphql**

### Querying the API through the provided interface
#### Querying existents urls:
```
{urls{
    id, normalUrl, shortUrl
  }
}
```
*A list with all available urls will be displayed*
#### Creating an url:
```
mutation{
  createUrl(url:"github.com"){
    url{
      normalUrl
      shortUrl
    }
  }
}
```
#### Retrieving short url for an especific url:
```
{
  url(url:"github.com"){
    shortUrl
  }
}
```
#### Retrieving normal url for an especific short url:
```
{
  url(url:"7gs.9"){
    normalUrl
  }
}
```
#### Accessing the short url:
On the browser, access the address for the running server, attaching the short url at the end like:
```
http://127.0.0.1:8000/7gs.9
```
The system will redirect you for the url associated to the short url.
