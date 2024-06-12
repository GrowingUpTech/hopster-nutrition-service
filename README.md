# hopster-nutrition-service

Brief description or introduction to your project.

## Prerequisites

- Python 3.10
- Docker

## Add .env to project before start

1. Create a `.env` file in the root directory of your project with the following content:

   ```bash
    SECRET_KEY=your_secret_key_here

## Getting Started without Docker

1. Clone the repository:

   ```bash
   git clone https://github.com/GrowingUpTech/hopster-nutrition-service.git
   cd hopster-nutrition-service

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate

3. Install dependencies:

    ```bash
    pip install -r requirements.txt

4. Run migrations:

    ```bash
    python manage.py makemigrations nutrition_service_api
    python manage.py migrate

5. Start the Django server:

    ```bash
    python manage.py runserver 8080

## Docker
Alternatively, you can use Docker to run the project:

1. Build the Docker image:

    ```bash
    docker build -t nutrition-service-api .

2. Run the Docker container

    ```bash
    docker run -p 8080:8080 nutrition-service-api

## Environment Variables
- SECRET_KEY: Django secret key

## Contributing
We use the following branching strategy for contributions:

- `main`: The main branch represents the production-ready code.
- `dev`: The development branch is where feature development occurs. It's a work in progress and may be unstable at times.
- `release`: The release branch is created from dev when preparing for a release. It undergoes testing and bug fixes before merging into main.

To contribute, follow these steps:
1. Clone the repository
2. Create a new branch   
    2.1 Feature branch: (git checkout -b feature/branch)   
    2.2 Fix branch: (git checkout -b fix/branch)  
3. Make your changes
4. Commit your changes (git commit -am 'Add new feature')
5. Push to the branch 
6. Create a new Pull Request