
# ACIT3495-Project1

## Set up and installation

1. Clone repository
https://github.com/Lara40401/ACIT3495-Project1.git

2. `cd` into the directory that contains the `docker-compose.yml` file.

3. Start the services with Docker compose
`docker-compose up --build`

4. Verify all containers are running: `docker ps`
There should be six containers running:
- "project1_data_entry"
- "project1_results_service"
- "project1_auth_service"
- "project1_analytics_service"
- "project1_mongo"
- "project1_mysql"

## Usage

1. Enter data web app: `http://localhost:5000`
2. Show results web app: `http://localhost:5003/show_results`


## Sources used


- https://www.datacamp.com/tutorial/running-mongodb-in-docker

- https://www.geeksforgeeks.org/python/how-to-fetch-data-from-mongodb-using-python/

- https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/

- https://dvmhn07.medium.com/jwt-authentication-in-node-js-a-practical-guide-c8ab1b432a49 

- https://www.geeksforgeeks.org/python/flask-creating-first-simple-application/

- https://flask.palletsprojects.com/en/stable/quickstart/ 

- https://www.geeksforgeeks.org/cloud-computing/what-is-dockerfile/

- https://docs.docker.com/reference/compose-file/
