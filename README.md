# To-Do-FlaskApp

# Running the Flask App with Docker Compose

This guide will walk you through running your Flask application using Docker Compose. Ensure that you have Docker and Docker Compose installed on your system.

## Clone the Repository

If you haven't already, clone the repository containing your Docker Compose configuration file (`docker-compose.yml`) and your application code.

git clone <repository_url>
cd <repository_directory>

Start the Application

To run the application, follow these steps:

    Build and Start the Containers:

    Navigate to the directory where your docker-compose.yml file is located and execute the following command:

    bash

docker-compose up --build

This command will build the Docker images for your frontend and backend services, create and start the containers, and set up the PostgreSQL database.

Access the Application:

    The frontend application will be available at http://localhost:5001. You can access it in your web browser.

    The backend application will be available at http://localhost:5000.

Stopping the Application:

To stop the application and remove the containers, press Ctrl + C in the terminal where Docker Compose is running.

Alternatively, you can run the following command to stop and remove the containers:
  docker-compose down
Environment Variables

    Frontend:
        SECRET_KEY: Set to 'Friends'.
        BACKEND_URL: Set to 'http://backend:5000' to connect to the backend service.

    Backend:
        DATABASE_URI: PostgreSQL database connection URL.
        SECRET_KEY: Set to 'TheBigBangTheory'.

Database Configuration

The PostgreSQL database is set up with the following configurations:

    Username: postgres
    Password: password123
    Database Name: todo_db

Cleaning Up

To remove all containers and volumes created by Docker Compose, you can use the following commands:

bash

docker-compose down -v

This will stop and remove the containers and also delete the associated volumes. Use this command with caution, as it will delete all database data if you have any.

Feel free to customize the environment variables and configurations as needed for your specific application. Happy coding!


