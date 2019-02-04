# login-service
Simple login service allows you to add and delete users.

## Installation
* *Clone repository from Github:*
```
$ git clone https://github.com/mikescor/login-service
```
* *Create and activate virtual env:*
```
(venv) ~/login-service $
```
##### Note
[Info about virtualenv](https://virtualenv.pypa.io/en/stable/)

* *Install requirements:*
```
(venv) ~/login-service $ pip install -r requirements.txt
```
* *Add database path:*
```
(venv) ~/login-service $ export DATABASE_URL='postgresql://<user_name>:<user_password>@localhost/<db_name>'
```
##### Note
[Info about postgresql](https://www.postgresql.org/docs/10/static/manage-ag-createdb.html)

* *Install [elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) on your computer*

* *Add elasticsearch path:*
```
(venv) ~/login-service $ export ELASTICSEARCH_URL=http://localhost:9200
```

* *Apply migrations:*
```
(venv) ~/login-service $ flask db upgrade
```
* *Finnaly, run the app*
```
(venv) ~/login-service $ flask run
```
## Technology stack
* [Flask](http://flask.pocoo.org/docs/1.0/)
* [Postgresql](https://www.postgresql.org/docs/10/static/intro-whatis.html)
* [Elasticsearch](https://www.elastic.co/products/elasticsearch) 