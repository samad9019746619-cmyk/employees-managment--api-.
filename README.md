# Simple API Project (11 lines)

A tiny API with 2 routes: read employees and add an employee.

## How to run
1. `pip install flask`
2. `python app.py`
3. Open `http://127.0.0.1:5000/employees` in the browser (this is a GET request)

## How to test POST (Postman)
- Method: POST
- URL: `http://127.0.0.1:5000/employees`
- Body -> raw -> JSON:
  `{"id": 2, "name": "Sara", "department": "HR"}`
- Click Send -> you get status 201 and `{"message": "added"}`
- Now open the GET link again -> Sara is in the list

Note: the data is kept in a Python list, so it resets when the app restarts.
In a bigger project this list would be a database.

---

## The code, line by line
1. `from flask import ...` - bring in Flask (the tool to build the API)
2. `app = Flask(__name__)` - create my app
3. `employees = [...]` - my data, a list with one employee
4. `@app.route("/employees", methods=["GET"])` - when someone sends a GET to /employees, run the function below
5. `def get_employees():` - the function
6. `return jsonify(employees)` - send the list back as JSON
7. `@app.route("/employees", methods=["POST"])` - when someone sends a POST to /employees, run the function below
8. `def add_employee():` - the function
9. `employees.append(request.get_json())` - take the JSON the user sent and add it to my list
10. `return jsonify({"message": "added"}), 201` - reply "added" with status 201 (created)
11. `app.run(debug=True)` - start the server

---

## What to say (about 4 minutes)

### 1. What is an API? (30 seconds)
"API means Application Programming Interface. In simple words, it is a
messenger between two programs.

Think about a restaurant. I am the customer. I don't go inside the kitchen.
I tell the waiter what I want, the waiter takes my order to the kitchen and
brings the food back to me. The waiter is the API. The kitchen is the server.
The customer is the website or the app."

### 2. How does an API work? (1 minute)
"Every API works in two steps: a request and a response.

The client sends a request. The server sends back a response.

A request has three main things:
- the URL, which is the address, it tells where to go
- the method, which tells what I want to do
- sometimes a body, which is the data I am sending

There are 4 common methods:
- GET means read data
- POST means add new data
- PUT means update data
- DELETE means remove data

The response has a status code and the data. The status code tells if it worked.
200 means OK, 201 means created, 404 means not found, 500 means the server
had an error.

The data usually comes in JSON format. JSON is just simple text for data,
like name: Ali, department: IT."

### 3. My project (1 minute 30 seconds)
"I made a small API in Python using Flask. It is 11 lines.

I have a list of employees. And I made 2 routes. A route is a URL plus a
method, connected to a function.

First route is GET /employees. When someone sends a GET request, my function
returns the employee list as JSON.

Second route is POST /employees. When someone sends data with POST, my
function adds that employee to the list and replies with 'added' and
status 201.

Let me show it." (Open the browser link, show Ali. Then Postman POST Sara.
Then open the link again, show Sara.)

### 4. Where it fits in a real project (30 seconds)
"In a full project there are 3 parts. Frontend is HTML and CSS, what the user
sees. Backend is Python, where my API is. Database is where the data is saved.

The frontend sends a request to the API. The API checks it, talks to the
database, and sends the response back. The frontend never talks to the
database directly. The API is the middle layer, so it is safer."

### 5. Types of API (30 seconds)
"Public API is open for everyone, like a weather API. Private API is only used
inside the company, like mine. Partner API is shared only with approved
business partners, with a key."

---

## Questions he may ask
- **What is an endpoint?** The URL of the API, like /employees.
- **What is a route?** In Flask, the line that connects a URL and a method to a function.
- **GET vs POST?** GET reads data. POST sends new data to save.
- **What is JSON?** A simple text format for data that both Python and JavaScript understand.
- **What is a REST API?** An API that uses URLs for things and methods (GET, POST...) for actions. Mine is like that.
- **What is 404? What is 500?** 404 = URL not found. 500 = error inside the server code.
- **Why use an API?** So many apps (website, mobile app) can use the same backend.
- **What would you add next?** DELETE and PUT routes, a real database, and a login or API key.
