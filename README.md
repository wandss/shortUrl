# shortUrl Project

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
3. Activate the created virtualenv
4. Inside project's root directory run:
```
pip install -r requirements.txt
```

5. Inside project's directory (sevenGeese directory), same level as **manage.py** script run:
```
python manage.py migrate
```
6. Set redis addres in settings.py
- In **file settings.py**, add the addres to you redis server in **CACHES** property:
```
'LOCATION': 'redis://<your-redis-server-address>'
```
### How to run the project
1. Inside the same directory from step 5 above, run:
```
python manage.py runserver
```
**Take note at the address showed at prompt**

2. Open a web browser
3. Access the address showed at the prompt, probably **http://127.0.0.1:8000/graphql**

### Querying the API through the provided interface
#### Querying urls:
```
{urls(url:"7geese.com/features/objectives-and-key-results-okrs/"){
  	shortUrl
	}
}
```
*The shortened url will be retrieved*

#### Accessing the short url:
On the browser, access the address for the running server, attaching the short url at the end like:
```
http://127.0.0.1:8000/<returned-url>
```
The system will redirect you for the url associated to the short url.
