# POC.ECS.Python.App

1. Create the virtual environment (Python 3.6.8)

2. `pip install -r requirements.txt`



Commands
========
`docker tag poc-ecs-python-app 019179091045.dkr.ecr.eu-west-1.amazonaws.com/poc-ecs-python-app`

`aws ecr get-login --no-include-email`

`docker push 019179091045.dkr.ecr.eu-west-1.amazonaws.com/poc-ecs-python-app:latest`

