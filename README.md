# nava-task

Nava Practical Round - 2

Task: 
Create REST APIs in fastAPI for Organization management where the admin can perform some tasks described below.

1. Create an API using which the admin can create an Organization with some information
In the backend, you create a Dynamic DB of that organization with the admin user and store that Dynamic DB information in our Master Database.

Example:
API Endpoint: Org/create - Create Organization with admin
Payload: email, password, organization_name



2. API endpoint: Org/get - Get organization By name
Payload: organization_name


3. API endpoint: admin/login - The user that we created can log in
Payload - admin, password
Response: JWT token

4. Create a Docker file for all services


NOTE: 
A. Use a clean and global project structure.
