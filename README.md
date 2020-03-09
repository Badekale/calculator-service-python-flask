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
```bash
$ aws codecommit create-repository --repository-name myproject-calculator-service
$ aws ecr create-repository --repository-name myproject-calculator-service
```

## Usage
- Clone CodeCommit Repository and navigate to working directory
```bash
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
```bash
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $
(venv) $ venv/bin/pip install flask
(venv) $ venv/bin/pip install flask-cors
```

- To deactivate
```bash
(venv) $ deactivate
```

- Add .gitignore file     ~/environment/myproject-calculator-service-python/.gitignore
- Create calculator class ~/environment/myproject-calculator-service-python/calculator.py
- Add app                 ~/environment/myproject-calculator-service-python/app.py
- Add README.md file      ~/environment/myproject-calculator-service-python/README.md
- Generate                ~/environment/myproject-calculator-service-python/requirements.txt
```bash
$ pip freeze > requirements.txt
```

- Add Unit Testing ~/environment/myproject-calculator-service-python/test_calculator.py

- Run Tests
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

- Test using curl scripts ~/environment/myproject-calculator-service-python/curl_scripts.md

- Add Docker File ~/environment/myproject-calculator-service-python/Dockerfile

- Build, Tag and Run the Docker Image locally. (Replace AccountId and Region)
```bash
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
```bash
$ aws ecr delete-repository --repository-name myproject-calculator-service --force
$ aws codecommit delete-repository --repository-name myproject-calculator-service
$ rm -rf ~/environment/myproject-calculator-service
```
