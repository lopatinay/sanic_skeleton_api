# Sanic skeleton RestAPI

## Installation
#### Create `venv` and activate it
```bash
python3.10 -m venv venv
source venv/bin/activate
```

#### Install development requirements
```bash
pip install -r requirements/dev_requirements.txt
```
for production there is `requirements.txt`.  
`dev_requirements.txt` contains all dependencies from `requirements.txt` plus necessary requirements
for development eg PyTest, Flake8 and etc

#### Run Postgres
```bash
docker-compose up -d
```

#### Run server
```bash
python manage.py runserver
```

#### Health check
```bash
curl -v http://0.0.0.0:5001/api/v1/health
```
response:
```bash
...
< HTTP/1.1 200 OK
...
healthy
```

## Put requirements
Add new requirements to `requirements.in` (prod) or `dev_requirements.in` (dev) with version.
Then compile your new requirements
```bash
make compile-versions
```
After that `compile-versions` will create two files `requirements.txt` and `dev_requirements.txt` 
with frozen nested requirements.

## Layers
### Domain
Domain should contains only business logic

### Resources
Resources should contains only implementation of catching request and return response.

### Services
Services should contains only implementation of application/framework utils eg caching, database connections and etc
