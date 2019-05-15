# Backend Python Flask RestAPI  Calculator

The Backend Project Layout will look like this:

```
~/environment/calculator-backend
├── aws-cli/
│   ├── artifacts-bucket-policy.json
│   ├── code-build-project.json
│   └── eks-calculator-codebuild-codepipeline-iam-role.yml
├── app.py
├── buildspec.yml
├── calculator.py
├── kubernetes/
│   ├── deployment.yml
│   └── service.yml
├── requirements.txt
├── test_calculator.py
├── venv/
├── Dockerfile
├── README.md
└── .gitignore
```

## Step 1: Create Backend using Python Flask REST API
- Basic calculations (add, subtract, multiply, divide)
- Advanced calculations (square root, cube root, power, factorial)
- Calculator triggered by developers via a web api

```
HTTP METHOD | URI                                                         | Action
-----------   -----------------------------------------------------------   --------------------------------------------------
POST        | http://[hostname]/add {"argument1":a, "argument2":b }       | Adds two numbers (a + b)
POST        | http://[hostname]/subtract {"argument1":a, "argument2":b }  | Subracts two numbers (a - b)
POST        | http://[hostname]/multiply {"argument1":a, "argument2":b }  | Multiplies two numbers (a * b)
POST        | http://[hostname]/divide {"argument1":a, "argument2":b }    | Divides two numbers (a / b)
POST        | http://[hostname]/sqrt {"argument1":a }                     | Gets the square root of a number (a)
POST        | http://[hostname]/cbrt {"argument1":a }                     | Gets the cube root of a number (a)
POST        | http://[hostname]/exp {"argument1":a, "argument2":b }       | Gets the the exponent of a raised to b
POST        | http://[hostname]/factorial {"argument1":a }                | Get the factorial of number 5! = 5 * 4 * 3 * 2 * 1 
```

### Step 1.1: Create a CodeCommit Repository
```
$ aws codecommit create-repository --repository-name calculator-backend
```

### Step 1.2: Clone the repository
```
$ cd ~/environment
$ git clone https://git-codecommit.us-east-1.amazonaws.com/v1/repos/calculator-backend
```

### Step 1.3: Setup .gitignore
```
$ cd ~/environment/calculator-backend
$ vi .gitignore
```
```
venv
*.pyc
```

### Step 1.4: Test access to repo by adding README.md file and push to remote repository
```
$ cd ~/environment/calculator-backend
$ echo "calculator-backend" >> README.md
$ git add .
$ git commit -m "Adding README.md"
$ git push origin master
```

### Step 1.5: Navigate to working directory
```
$ cd ~/environment/calculator-backend
$ python3 -m venv venv
$ source venv/bin/activate
$ venv/bin/pip install flask
$ venv/bin/pip install flask-cors
```

### Step 1.6 Create Calculator Class Calculator.py
```
$ cd ~/environment/calculator-backend
$ vi calculator.py
```
```
#!/usr/bin/env python
import math

class Calculator:
    def __init__(self):
        pass

    def add(self, arg1, arg2):
        return float(arg1) + float(arg2)

    def subtract(self, arg1, arg2):
        return float(arg1) - float(arg2)

    def multiply(self, arg1, arg2):
        return float(arg1) * float(arg2)

    def divide(self, arg1, arg2):
        return float(arg1) / (arg2)

    def sqrt(self, arg1):
        return math.sqrt(float(arg1))

    def cbrt(self, arg1):
        return round(float(arg1)**(1.0/3))

    def exp(self, arg1, arg2):
        return float(arg1) ** float(arg2)

    def factorial(self, arg1):
       if arg1 == 1:
          return arg1
       else:
          return float(arg1)*self.factorial(float(arg1)-1)
```

### Step 1.7: Add app.py
```
$ cd ~/environment/calculator-backend
$ vi app.py
```
```
#!/usr/bin/env python
from flask import (Flask, jsonify, request, abort, render_template, logging)
from flask_cors import CORS
from calculator import Calculator

app = Flask(__name__)
CORS(app)

@app.route('/')
def index_page():
    return "This is a RESTful Calculator App built with Python Flask! - testing my CI/CD Pipeline"

@app.route('/add', methods=['POST'])
def add_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        calculator = Calculator()
        answer = calculator.add(arg1, arg2)
        app.logger.info('{ "operation": "add", "arg1": "%s", "arg2": "%s", "answer": "%s" }', arg1, arg2, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/subtract', methods=['POST'])
def subtract_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        calculator = Calculator()
        answer = calculator.subtract(arg1, arg2)
        app.logger.info('{ "operation": "subtract", "arg1": "%s", "arg2": "%s", "answer": "%s" }', arg1, arg2, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/multiply', methods=['POST'])
def multiply_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        calculator = Calculator()
        answer = calculator.multiply(arg1, arg2)
        app.logger.info('{ "operation": "multiply", "arg1": "%s", "arg2": "%s", "answer": "%s" }', arg1, arg2, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/divide', methods=['POST'])
def divide_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        calculator = Calculator()
        answer = calculator.divide(arg1, arg2)
        app.logger.info('{ "operation": "divide", "arg1": "%s", "arg2": "%s", "answer": "%s" }', arg1, arg2, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)
    except ZeroDivisionError:
        abort(400)

@app.route('/sqrt', methods=['POST'])
def sqrt_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        calculator = Calculator()
        answer = calculator.sqrt(arg1)
        app.logger.info('{ "operation": "sqrt", "arg1": "%s", "arg2": "none", "answer": "%s" }', arg1, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/cbrt', methods=['POST'])
def cbrt_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        calculator = Calculator()        
        answer = calculator.cbrt(arg1)
        app.logger.info('{ "operation": "cbrt", "arg1": "%s", "arg2": "none", "answer": "%s" }', arg1, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/exp', methods=['POST'])
def exponent_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        arg2 = request.json['argument2']
        calculator = Calculator()        
        answer = calculator.exp(arg1, arg2)
        app.logger.info('{ "operation": "exp", "arg1": "%s", "arg2": "%s", "answer": "%s" }', arg1, arg2, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

@app.route('/factorial', methods=['POST'])
def factorial_args():
    if not request.json:
        abort(400)
    try:
        arg1 = request.json['argument1']
        calculator = Calculator()          
        answer = calculator.factorial(arg1)
        app.logger.info('{ "operation": "factorial", "arg1": "%s", "arg2": "none", "answer": "%s" }', arg1, answer)
        return (jsonify({'answer':answer}), 200)
    except KeyError:
        abort(400)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

### Step 1.8: Create the requirements.txt file
```
$ cd ~/environment/calculator-backend
$ vi requirements.txt
```
```
flask
flask_restful
flask_cors
```

### Step 1.9: Run Locally and Test
```
$ cd ~/environment/calculator-backend
$ chmod a+x app.py
$ ./app.py
$ curl http://localhost:5000
```

### Step 1.10: Backend Unit Tests
```
$ cd ~/environment/calculator-backend
$ vi test_calculator.py
```
```
#!/usr/bin/env python
import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    calculator = Calculator()
    
    def test_add(self):
        self.assertEqual(4, self.calculator.add(2,2))

    def test_subtract(self):
        self.assertEqual(2, self.calculator.subtract(3,1))
        self.assertEqual(-2, self.calculator.subtract(1,3))

    def test_multiply(self):
        self.assertEqual(12, self.calculator.multiply(3,4))
        self.assertEqual(13.5, self.calculator.multiply(3,4.5))

    def test_divide(self):
        self.assertEqual(3, self.calculator.divide(9,3))
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(3,0) 
    
    def test_sqrt(self):
        self.assertEqual(4, self.calculator.sqrt(16))

    def test_cbrt(self):
        self.assertEqual(4, self.calculator.cbrt(64))

    def test_exp(self):
        self.assertEqual(32, self.calculator.exp(2,5))

    def test_factorial(self):
        self.assertEqual(120, self.calculator.factorial(5))

if __name__ == "__main__":
    unittest.main()
```

### Step 1.11: Run Unit Tests
```
$ chmod a+x test_calculator.py
$ ./test_calculator.py -v
```

### Step 1.12 Save changes to remote git repository
```
$ git add .
$ git commit -m "Initial"
$ git push origin master
```

### Step 1.13: Create the Dockerfile
```
$ cd ~/environment/calculator-backend
$ vi Dockerfile
```
```
# Set base image to python
FROM python:3.7

# Copy source file and python req's
COPY . /app
WORKDIR /app

# Install requirements
RUN pip install -r requirements.txt

# Set image's main command and run the command within the container
ENTRYPOINT ["python"]
CMD ["app.py"]
```

### Step 1.14: Build, Tag and Run the Docker Image locally
Replace:
- AccountId: 707538076348
- Region: us-east-1

```
$ docker build -t calculator-backend .
$ docker tag calculator-backend:latest 707538076348.dkr.ecr.us-east-1.amazonaws.com/calculator-backend:latest
$ docker run -d -p 5000:5000 calculator-backend:latest
```

### Step 1.15: Test Math Operations
- Test Add
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":2, "argument2":1 }' http://localhost:5000/add
{
  "answer": 3
}
```

- Test Subtract
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":4, "argument2":3 }' http://localhost:5000/subtract
{
  "answer": 1
}
```

- Test Multiply
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":2, "argument2":3 }' http://localhost:5000/multiply
{
  "answer": 6
}
```

- Test Divide
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":12, "argument2":4 }' http://localhost:5000/divide
{
  "answer": 3
}
```

- Test Square Root
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":9 }' http://localhost:5000/sqrt
{
  "answer": 3
}
```

- Test Cube Root
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":64 }' http://localhost:5000/cbrt
{
  "answer": 4
}
```

- Test Power
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":2, "argument2":3 }' http://localhost:5000/exp
{
  "answer": 8
}
```

- Test Factorial
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":5 }' http://localhost:5000/factorial
{
  "answer": 120
}
```

### Step 1.16: Create the ECR Repository
```
$ aws ecr create-repository --repository-name calculator-backend
```

### Step 1.17: Run login command to retrieve credentials for our Docker client and then automatically execute it (include the full command including the $ below).
```
$ $(aws ecr get-login --no-include-email)
```

### Step 1.18: Push our Docker Image
```
$ docker push 707538076348.dkr.ecr.us-east-1.amazonaws.com/calculator-backend:latest
```

### Step 1.19: Validate Image has been pushed
```
$ aws ecr describe-images --repository-name calculator-backend
```

### (Optional) Clean up
```
$ aws ecr delete-repository --repository-name calculator-backend --force
$ aws codecommit delete-repository --repository-name calculator-backend
$ rm -rf ~/environment/calculator-backend
```
