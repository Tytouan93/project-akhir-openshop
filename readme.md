# Project Akhir OpenShop 🛒

Welcome to the **Project Akhir OpenShop** repository! This project serves as a practical learning experience for beginners in back-end development using Python. It is designed to help you understand how to build a RESTful API using Django, one of the most popular frameworks for web development.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Links](#links)

## Introduction

This repository is part of the **Dicoding** learning program, focusing on back-end development for beginners. The goal is to create a functional online shop where users can browse products, add them to their cart, and make purchases. The project covers essential back-end concepts and practical skills, including API design, database management, and server-side logic.

## Features

- User authentication and management
- Product listing and detail views
- Shopping cart functionality
- Order processing
- RESTful API for easy integration
- Comprehensive documentation

## Technologies Used

This project utilizes the following technologies:

- **Python**: The primary programming language for back-end development.
- **Django**: A high-level Python web framework that encourages rapid development.
- **Django REST Framework**: A toolkit for building Web APIs.
- **SQLite**: A lightweight database for development and testing.
- **Git**: Version control system for tracking changes.

## Installation

To get started with the project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Tytouan93/project-akhir-openshop.git
   ```

2. Navigate to the project directory:

   ```bash
   cd project-akhir-openshop
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

6. Run database migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

Now, you can access the application at `http://127.0.0.1:8000/`.

## Usage

Once the server is running, you can explore the API endpoints. Use tools like Postman or cURL to interact with the API. Here are some common tasks you can perform:

- **Get all products**: Send a GET request to `/api/products/`.
- **Get a single product**: Send a GET request to `/api/products/{id}/`.
- **Create a new product**: Send a POST request to `/api/products/` with the required data.
- **Update a product**: Send a PUT request to `/api/products/{id}/` with the updated data.
- **Delete a product**: Send a DELETE request to `/api/products/{id}/`.

## API Endpoints

### Products

- **GET /api/products/**: Retrieve a list of products.
- **GET /api/products/{id}/**: Retrieve details of a specific product.
- **POST /api/products/**: Create a new product.
- **PUT /api/products/{id}/**: Update an existing product.
- **DELETE /api/products/{id}/**: Delete a product.

### Users

- **POST /api/users/**: Register a new user.
- **POST /api/token/**: Obtain a token for authentication.

### Orders

- **GET /api/orders/**: Retrieve a list of orders.
- **POST /api/orders/**: Create a new order.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Create a pull request.

Please ensure that your code adheres to the project's coding standards and that you include tests for any new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Links

You can find the latest releases of this project [here](https://github.com/Tytouan93/project-akhir-openshop/releases). Download and execute the files as needed to get the most recent updates.

For more information, visit the [Releases](https://github.com/Tytouan93/project-akhir-openshop/releases) section in the repository.

![Django](https://img.shields.io/badge/Django-3.2-green)
![Python](https://img.shields.io/badge/Python-3.9-blue)

## Conclusion

Thank you for checking out the **Project Akhir OpenShop** repository! We hope this project serves as a valuable resource in your journey to becoming a proficient back-end developer. Happy coding!