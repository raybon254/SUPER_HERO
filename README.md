## Superheroes API
A Flask-based API for managing superheroes and their unique superpowers, complete with robust validations, relationships, and CRUD functionality.

## Description
This project provides a fully functional backend API that allows users to manage superheroes, their powers, and their associated strengths. It uses a well-structured relational model with clear validations and leverages Flask, SQLAlchemy, and Flask-Migrate.

## Features

# Heroes
List all heroes
View individual hero details including powers

# Powers
View all superpowers
View and update a specific power (with validation)

# Hero Powers
Associate heroes with powers via a join model (HeroPower)
Assign strength levels to each hero-power combination

# Validations
Enforces minimum character length for power descriptions
Strength values must be one of: 'Strong', 'Weak', 'Average'

# Error Handling
Returns appropriate JSON error messages for invalid data
Handles 400 and 404 errors gracefully

# Project Structure
├── server/
│   ├── app.py            
│   ├── models/                    
│   ├── migrations/       
│   └── instance/
│       └── superheroesapi.db 
│
├── seed.py
├── Pipfile                
├── Pipfile.lock
└── README.md

## Setup Instructions
git clone
cd super-heroes-api
Install Dependencies:

pipenv install
pipenv shell
Initialize the Database:
cd server
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Seed the Database

## Start the Server
python app.py
Access the API at: http://localhost:5555/

## API Endpoints

# Heroes
Method Endpoint         Description
GET /heroes                 Get all heroes
GET /heroes/<id>         Get a hero and their powers

# Powers
Method Endpoint
GET /powers            Get all powers
GET /powers/<id> -        Get a specific power
PATCH /powers/<id> -     Update power description

# Hero Powers
Method Endpoint
POST /hero_powers    Create a new hero-power relationship with strength

# Data Models
Hero
id: Primary key
name: Real name of the hero
super_name: Alias or superhero name

## Power
id: Primary key
name: Name of the superpower
description: Description of the power (min 20 characters)

## HeroPower
id: Primary key
strength: Must be 'Strong', 'Average', or 'Weak'
hero_id: Foreign key to Hero
power_id: Foreign key to Power

## Validations
Power description must be at least 20 characters long
HeroPower strength must be one of: 'Strong', 'Weak', 'Average'
Invalid input returns 400 Bad Request with a meaningful error message

## Response Codes
# Description
200 Success
201 Resource Created
400 Validation or Input Error
404 Resource Not Found

## Technologies Used
Python 3.8
Flask
Flask SQLAlchemy
Flask Migrate
Pipenv