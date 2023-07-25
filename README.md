# Farmer-to-Consumer-Application
Farm-to-Consumer-Application is a digital platform that connects farmers directly with consumers, bypassing intermediaries and reducing the overall cost of food products. The platform allows farmers to list their produce, and consumers can purchase quality food at lower prices.

## Table of Contents
- [Introduction](#farm-to-consumer-platform)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## Features

- User registration and login with JWT authentication
- Farmers can list their products with images
- Consumers can browse and place orders for products
- Data pagination for product listings
- Swagger API documentation
- Multi-user authentication with role-based access
- Error handling and data validation
- CI/CD integration for code quality checks
- Human-readable date formatting

## Installation

1. Clone the repository:
git clone https://github.com/RichardMiruka/Farmer-to-Consumer-App


2. Install the required dependencies:
pip install -r requirements.txt


3. Set up environment variables:

Create a `.env` file in the root directory and add the following:

SECRET_KEY=your_secret_key_here
CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret
SENDGRID_API_KEY=your_sendgrid_api_key


## Usage

1. Run the application:

python run.py


2. Access the application in your web browser at `http://localhost:5000`.

3. Register as a farmer or consumer to start using the platform.

## API Endpoints

- POST `/register`: Register as a new user (farmer or consumer).
- POST `/login`: Log in and receive an access token for authentication.
- POST `/products`: Create a new product listing (farmers only).
- GET `/products`: Get a paginated list of available product listings.
- POST `/orders`: Place an order for a product (consumers only).
- GET `/orders`: Get a list of orders placed by the authenticated consumer.

## Technologies Used

- Python and Flask framework for the backend.
- Flask-RESTx for API documentation.
- Flask-JWT-Extended for JWT authentication.
- Flask-WTF for form handling and validation.
- SQLAlchemy for database management.
- Cloudinary for image uploads and storage.
- Sendgrid for email notifications.
- Frontend technologies (HTML, CSS, JavaScript) for the user interface.

## Contributing

Contributions to the Farm-to-Consumer Platform are welcome! Please follow the standard guidelines for contributing to open-source projects.

## License

This project is licensed under the [MIT License](LICENSE).

## Authors
<details>
<summary>Authors</summary>

* [**@Richard Miruka**](https://github.com/RichardMiruka)

</details>
