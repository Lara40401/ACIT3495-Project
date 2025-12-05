# ACIT3495-Project2

## Run the command as following order:
### Mysql
1. `kubectl apply -f pwd-config.yaml`
2. `kubectl apply -f mysql-initdb-configmap.yaml`
3. `kubectl apply -f mysql-svc.yaml`
### MongoDB
4. `kubectl apply -f mongo-initdb-configmap.yaml`
5. `kubectl apply -f mongo-deployment.yaml`
6. `kubectl apply -f mongo-svc.yaml`
### Wait for databases to be ready
7. `kubectl wait --for=condition=ready pod -l app=mysql --timeout=120s`
8. `kubectl wait --for=condition=ready pod -l app=mongo --timeout=120s`
### Auth_service and Data entry services
9. `kubectl apply -f auth_service_deployment.yaml`
10. `kubectl apply -f auth_service_svc.yaml`
11. `kubectl apply -f data_entry_deployment.yaml`
12. `kubectl apply -f data_entry_svc.yaml`
### Analytics and show_results services
13. `kubectl apply -f analytics-deployent.yaml`
14. `kubectl apply -f show_results_deployment.yaml`
15. `kubectl apply -f show_results_svc.yaml`

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
