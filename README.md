# bookstore-inventory-management-system
A book store management system

Bookstore is an API for managing a book store inventory.

## Technology Stack
**Backend**
* **Language**: [Python](https://www.python.org/)
* **Database**: [PostgreSQL](https://www.postgresql.org/)
* **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
* **REST API**: [Flask](http://flask.pocoo.org/)
## Running with Docker
We are using Docker which means you don't need to install any of the dependencies on your local machine (except for docker itself). If you are already familiar with Docker and the technologies listed above, you can clone the repository to you local machine and bring up the database and back-end together with:

```docker-compose build```

```docker-compose up```

The backend-api will then be available at localhost:5000

If you are not familiar with this style of development, here is a more detailed description:


## Getting Started (Detailed with Docker)
1. Make sure you have the following installed on your machine:
* Git: [Windows](https://git-scm.com/download/win), [Mac](https://git-scm.com/download/mac). (Linux users should install using their system's package manager)
* Docker: [Windows](https://docs.docker.com/docker-for-windows/install/), [Mac](https://docs.docker.com/docker-for-mac/install/), [Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/) (ensure you have the latest version!)

2. Ensure that docker is running on your machine by running ```docker run hello-world``` 

3. Clone (copy to your local machine) the repository using the command:
```git clone https://github.com/outhanchazima/bookstore-inventory-management-system.git```

4. Navigate to the Baobab folder (```cd bookstore-inventory-management-system```)

5. Build the containers using ```docker-compose build``` -  this will build the back-end and database together.
It will take a fair bit of time the first time you do it, subsequently it will be much faster. If you get any errors, check the **troubleshooting** section below. If you get any other errors at this step, please get in touch!  

6. Launch the containers using ```docker-compose up``` - you should see messages like "Starting bookstore-api ... done". You can then navigate to the application in your browser at ```http://localhost:5000/api/v1/docs```. you won't see anything if you navigate to localhost:5000 in your browser) 

7. The first time you run the app, you may need to run the **migrations** to ensure that all the tables are created in the database. While the app is running (after following the previous step), run the following in **another terminal/command prompt**: ```docker-compose run web python ./api/run.py db upgrade --directory api/migrations```


## Getting Started (Detailed without Docker)
1. Make sure you have the following installed on your machine:
* Git: [Windows](https://git-scm.com/download/win), [Mac](https://git-scm.com/download/mac). (Linux users should install using their system's package manager)
* Python 3.8.5 and above
* Postgres Database 13 and above.
* make sure you have pip and virtualenv installed.

### Part One
Intiallizing postgres database
```
CREATE USER bookstore WITH PASSWORD 'bookstore';
CREATE DATABASE bookstore;
GRANT ALL PRIVILEGES ON DATABASE bookstore TO bookstore;
```
### Part Two: Terminal commands
Clone the repo:

```bash
git clone 
```
Change directory
```
cd bookstore-inventory-management-system
```

#### Alternative 1
Note: make sure you have `pip` and `virtualenv` installed.

    Initial installation: make install

    To run test: make tests
`
    To run application: make run

    To run all commands at once : make all

Make sure to run the initial migration commands to update the database.
    
    > python3 manage.py db init

    > python3 manage.py db migrate --message 'initial database migration'

    > python3 manage.py db upgrade

#### Alternative 2
Create virtualenv:
```
python3 -m venv venv
```
Activate the virtual environment
```
source venv/bin/activate
```
Install the requirements
```
pip3 install -r requirements.txt
```
Run the application
```
python3 manage.py run
```
Run the application: PRODUCTION Mode
```
gunicorn manage:app --worker-class gevent --bind 0.0.0.0:5000 --log-level info
```
