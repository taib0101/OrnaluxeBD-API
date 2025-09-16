# Project Name

## About
This is a monolithic **E-Commerce API** built with **Django ORM** and **Django REST Framework**, following **SOLID principles** and the **Repository Design Pattern** for clean **CRUD** operations.  
The project uses **Agile methodologies** and is planned to include **CI/CD pipelines** and **Dockerized deployment with Nginx on AWS** for scalability and cloud readiness.

## API DOCS Link
API documentation here: [OpenAPI Docs with Swagger](https://ornaluxebd-api.onrender.com/api/docs/)

## Requirements
- **Python**: 3.11.12
- **Django**: 5.2.5  
- **Django REST Framework**: 3.16.1  
- **DRF-Spectacular**: 0.28.0  
- Full list in `requirements.txt`

## Project Setup
Clone the repository and install dependencies:

```bash
# Clone the project repository
git clone https://github.com/taib0101/OrnaluxeBD-API

# Navigate into the project directory
cd OrnaluxeBD-API


# Update package lists
sudo apt update

# Install required system dependencies for Python and PostgreSQL
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
    libffi-dev liblzma-dev python3-dev

# Install pyenv for managing multiple Python versions
curl https://pyenv.run | bash

# Add to shell config (~/.bashrc or ~/.zshrc)
nano ~/.bashrc
"""
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
"""

# Then reload your ~/.bashrc
source ~/.bashrc

# Install pyenv versions
pyenv install 3.11.12
pyenv local 3.11.12

# Install virtual environment
python -m venv env

# Activate env
source env/bin/activate

# Upgrade pip
python3 -m pip install --upgrade pip

# Install pip tools
pip3 install pip-tools

# Install requirements
pip3 install -r requirements.txt

```

## Database Setup

### Install PostgreSQL on Ubuntu

```bash
# Update package lists
sudo apt update

# Install PostgreSQL and its development libraries
sudo apt install -y postgresql postgresql-contrib libpq-dev

# Start PostgreSQL service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Switch to the postgres user
sudo -i -u postgres

# Open PostgreSQL prompt
psql

# Create the role with superuser privileges
CREATE ROLE root WITH SUPERUSER LOGIN PASSWORD '1234';

# Create Database
CREATE DATABASE mydatabase;

# Give all privileges on the database to your user
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO root;

exit

# TO see databases model
psql -U postgres -W -d mydatabase

```

## Apply Migrations
```bash
python3 manage.py makemigrations development
python3 manage.py migrate development
```

## Setup .env
```bash
DEVELOPMENT_DATABASE_URL=postgres://root:1234@localhost:5432/mydatabase

# $openssl rand -hex 64
DEVELOPMENT_SECRET_TOKEN_KEY=5612e7aa1f36c18b35803622bf28737a8e19880a338ab653993f0125a5b94313d1b28d2e21078842a322e8eb6130ceab53c44618725e8420b8faf27617a907d5

DEVELOPMENT_SECRET_TOKEN_ALGO=HS256

DEVELOPMENT_HOST=127.0.0.1

DEVELOPMENT_BIND_PORT=8000

```

## Run Server
```bash
python3 backend/manage.py runuvicorn development
```

## ER Diagram
<img src="design-assets/er_diagram_chen_notation.drawio.svg" alt="ER_Diagram" width="100%" height="100%"/>

## Monolithic Architecture
<img src="design-assets/api_design_repository.svg" alt="ER_Diagram" width="100%" height="100%"/>