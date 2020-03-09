# myproject-calculator-service-python

## Functional Requirements
- Basic calculations (add, subtract, multiply, divide)
- Advanced calculations (square root, cube root, power, factorial)
- Calculator triggered by developers via a web api

## API Endpoints
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

## Prerequisites
- Docker, Python, Flask, Git, Virtualenv https://github.com/jrdalino/development-environment-setup
- Setup CI/CD using https://github.com/jrdalino/myproject-aws-codepipeline-calculator-service-terraform. This will create CodeCommit Repo, ECR Repo, CodeBuild Project, Lambda Function and CodePipeline Pipeline 
- You may also create the repositories individually
```
$ aws codecommit create-repository --repository-name myproject-calculator-service
$ aws ecr create-repository --repository-name myproject-calculator-service
```

## Usage
- Clone CodeCommit Repository and navigate to working directory
```
$ cd ~/environment
$ git clone https://git-codecommit.ap-southeast-2.amazonaws.com/v1/repos/myproject-calculator-service
$ cd ~/environment/myproject-calculator-service-python
```

- Follow folder structure
```
~/environment/myproject-calculator-service-python
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

- Activate virtual environment, install flask and flask-cors
```
$ cd ~/environment/calculator-backend
$ python3 -m venv venv
$ source venv/bin/activate
$ venv/bin/pip install flask
$ venv/bin/pip install flask-cors
```

- Add .gitignore file ~/environment/myproject-customer-service-python/.gitignore
```
venv
*.pyc
```

- Create calculator class ~/environment/myproject-customer-service-python/calculator.py
- Add ~/environment/myproject-customer-service-python/app.py


- Generate requirements.txt
```
pip freeze > requirements.txt
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

- Add Unit Tests and Run Tests
```bash
$ chmod a+x test_calculator.py
$ ./test_calculator.py -v
```

- Run locally before dockerizing
```bash
$ chmod a+x app.py
$ ./app.py
$ curl http://localhost:5000
```

- Test using curl scripts ~/environment/myproject-customer-service-python/curl_scripts.md

- Add Docker File ~/environment/myproject-calculator-service-python/Dockerfile

- Build, Tag and Run the Docker Image locally. (Replace AccountId and Region)
```
$ docker build -t myproject-calculator-service .
$ docker tag myproject-calculator-service:latest 222337787619.dkr.ecr.ap-southeast-2.amazonaws.com/myproject-calculator-service:latest
$ docker run -d -p 5000:5000 myproject-calculator-service:latest
```

- Test using curl scripts ~/environment/myproject-calculator-service-python/curl_scripts.md

- Push our Docker Image to ECR and validate
```bash
$ $(aws ecr get-login --no-include-email)
$ docker push 222337787619.dkr.ecr.ap-southeast-2.amazonaws.com/myproject-calculator-service:latest
$ aws ecr describe-images --repository-name myproject-calculator-service
```

- Add Buildspec Yaml file ~/environment/myproject-calculator-service-python/buildspec.yml

- Add Kubernetes Deployment and Service Yaml files ~/environment/myproject-calculator-service-python/kubernetes/deployment.yml and ~/environment/myproject-calculator-service-python/kubernetes/service.yml

- Make changes, commit and push changes to CodeCommit repository to trigger codepipeline deployment to EKS
```bash
$ git add .
$ git commit -m "Initial Commit"
$ git push origin master
```

- Test using curl scripts ~/environment/myproject-calculator-service-python/curl_scripts.md

## (Optional) Clean up
```
$ aws ecr delete-repository --repository-name myproject-calculator-service --force
$ aws codecommit delete-repository --repository-name myproject-calculator-service
$ rm -rf ~/environment/myproject-calculator-service
```
