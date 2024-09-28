Flask Nginx Example with Docker and Docker Compose
This project demonstrates a simple Flask application with two endpoints: /good and /bad. The /good endpoint returns a success message, while the /bad endpoint crashes the container by exiting the main process.

Requirements
Docker
Docker Compose
Project Structure
bash
Copy code
/nginx-endpoints/
├── Dockerfile           # Dockerfile to build the Flask application
├── app.py               # Python Flask app with two endpoints
├── docker-compose.yml   # Docker Compose file to run the container
└── README.md            # Project documentation
How to Run
1. Clone the Repository
bash
Copy code
git clone <repository-url>
cd nginx-endpoints
2. Build and Run the Container with Docker Compose
To build the Docker image and run the container, simply run:

bash
Copy code
docker-compose up --build
This command will:

Build the Docker image using the Dockerfile.
Start the Flask app inside the container and map port 8080 on your local machine to port 80 inside the container.
3. Access the Application
Once the container is running, you can access the Flask application through the following endpoints:

/good: Returns a success message.

Open your browser or use curl to access:
bash
Copy code
curl http://localhost:8080/good
Expected response:
bash
Copy code
Todo va bien en /good
/bad: This endpoint will crash the container by exiting the main process.

Open your browser or use curl to access:
bash
Copy code
curl http://localhost:8080/bad
The container will immediately stop due to os._exit(1) being called.
Docker Compose will automatically restart the container thanks to the restart: always policy.
4. Stopping the Application
To stop and remove the running containers, press Ctrl+C in the terminal where Docker Compose is running, or run:

bash
Copy code
docker-compose down
Additional Information
The application is written in Python using Flask, a lightweight web framework.
The Dockerfile installs Flask and runs the application on port 80 inside the container.
Docker Compose is configured to restart the container automatically when it crashes, which happens when you access the /bad endpoint.