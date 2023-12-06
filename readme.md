# Kofi Backend

## Description

Kofi Backend is a backend API for a coffee shop management application. This API facilitates CRUD (Create, Read, Update, Delete) operations on products, handling orders, and managing customer information.

## Features

- Product Management: Add, update, delete, and list products.
- Order Management: Create, update, and track orders.
- Customer Management: Register and manage customer information.

## Technologies Used

- Flask: A micro web framework for Python.
- Firebase: For data storage and authentication.
- Python 3: The primary programming language.

## Installation

To install and run Kofi Backend on your local environment, follow these steps:

1. Clone the Repository:

   ```
   git clone https://github.com/NoeOsorio/kofi-backend.git
   ```

2. Set Up a Virtual Environment (optional, but recommended):

   ```
   python -m venv venv
   source venv/bin/activate
   ```

   (On Windows use)

   ```
   venv\Scripts\activate
   ```

3. Install Dependencies:

   ```
    pip install -r requirements.txt
   ```

4. Set Up Firebase:

   - Obtain your Firebase project credentials and save them in a `firebase_settings.json` file.
   - Ensure the file is located correctly or update the path in the application settings.

5. Run the Application:
   ```
   flask --app app.py run
   ```

## Usage

Provide instructions on how to use the API, including endpoints and example requests, if applicable.

## Contributing

Contributions to Kofi Backend are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information on how to contribute.

## License

This project is licensed under the [MIT License](LICENSE).
