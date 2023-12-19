# dbproject-projectmanagement

## Steps

1. **Create a .env File**

   Start by creating a new `.env` file in the root directory of your project. This file will be used to store environment variables.

2. **Add PostgreSQL Connection Details**

   Inside the `.env` file, add the following lines to define your PostgreSQL connection details. Replace the placeholder values with your actual database information:

   ```env
   # PostgreSQL Configuration
   DB_NAME=project_management
   DB_USER=postgres
   DB_PASSWORD=root
   DB_HOST=localhost
