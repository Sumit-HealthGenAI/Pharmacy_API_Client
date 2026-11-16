# Pharmacy API Client

A Python-based REST API client that demonstrates how to interact with HTTP APIs using CRUD concepts.

The application includes API request handling, input validation, exception handling, modular code organization, and automated testing with pytest.

It uses JSONPlaceholder as a mock API to practise API integration and software engineering fundamentals.

## Features

- Retrieves data from a REST API using HTTP GET requests.
- Validates medicine IDs before making API requests.
- Handles HTTP errors and network-related exceptions.
- Uses a reusable request-handling function with a 10-second timeout.
- Follows a modular architecture, separating API communication, input validation, menu handling, and application logic.
- Provides a command-line interface (CLI) for user interaction.
- Includes automated tests using pytest and mocking to test functionality without making real API calls.

## Technologies Used

- **Python 3.13** — Main programming language.
- **Requests** — HTTP library used to communicate with REST APIs.
- **Pytest** — Testing framework for automated tests.
- **unittest.mock** — Python standard-library module used to mock API requests and responses during testing.
- **Git** — Version control system.
- **GitHub** — Platform for hosting the project repository.
- **JSONPlaceholder** — Mock REST API used for practising API interactions.

## Project Structure

```text
Pharmacy_API_Client/
│
├── api_client.py       # API communication and input validation
├── main.py             # Main application entry point
├── menu.py             # Command-line menu handling
├── test_api_client.py  # Automated tests
├── requirements.txt    # Project dependencies
├── .gitignore          # Files excluded from Git
├── CHANGELOG.md        # Project change history
└── README.md           # Project documentation
```

## Installation

### Prerequisites

- Python 3.13 or later
- Git

### Steps

**1. Clone the repository**

```bash
git clone https://github.com/Sumit-HealthGenAI/Pharmacy_API_Client.git
```

**2. Navigate to the project directory**

```bash
cd Pharmacy_API_Client
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment (Windows)**

```powershell
venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Run the application**

```bash
python main.py
```

## Usage

Run the application:

```bash
python main.py
```

The application displays a command-line menu:

```text
--- Pharmacy API Client ---
1. Get medicine
2. Exit

Enter your choice:
```

### Retrieving data

1. Select option `1`.
2. Enter a valid positive integer ID.
3. The application sends a GET request to JSONPlaceholder.
4. The returned mock API data is displayed in the terminal.

Example:

```text
Enter your choice: 1
Retrieving medicine...
Enter medicine ID: 1

{'userId': 1, 'id': 1, 'title': '...', 'body': '...'}
```

### Exiting the application

Select option `2` to terminate the application.

```text
Exiting application...
```

**Note:** JSONPlaceholder is a mock REST API. The returned data represents sample blog posts rather than actual medicine records.

## Running Tests

This project uses pytest to run automated tests.

To execute all tests, run:

```bash
pytest -v
```

The `-v` flag enables verbose output, displaying individual test names and their results.

### Example output

```text
test_api_client.py::test_get_medicine PASSED
test_api_client.py::test_send_request PASSED
test_api_client.py::test_send_request_http_error PASSED
test_api_client.py::test_validate_medicine_id PASSED

==================== 4 passed ====================
```

The tests use mocking to simulate API responses, allowing functionality and error handling to be tested without making real API requests.

## Future Improvements

- **Additional HTTP operations:** Implement POST, PATCH, and DELETE operations to support creating, updating, and deleting mock records.
- **Improved input validation:** Add more comprehensive validation and clearer error messages for invalid inputs.
- **Expanded test coverage:** Add automated tests for additional edge cases, invalid inputs, and API failure scenarios.
- **Environment-based configuration:** Move settings such as the API base URL and request timeout into environment variables.
- **Structured logging:** Integrate logging throughout the application with structured log messages to improve debugging and maintenance.

## Author

**Sumit Kharat**

GitHub: [Sumit-HealthGenAI](https://github.com/Sumit-HealthGenAI)