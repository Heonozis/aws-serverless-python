aws.deploy.common.topics:
	aws sns create-topic --name arn:aws:sns:us-west-2:123456789012:common.health.requested
	aws sns create-topic --name arn:aws:sns:us-west-2:123456789012:common.health.processed

aws.deploy.common.functions:
	zip function.zip .
	aws lambda create-function --function-name health_handler --zip-file fileb://function.zip --handler main.health_handler --runtime python3.7 --role arn:aws:iam::123456789012:role/lambda-ex

aws.deploy.init:
	aws.deploy.common.topics
	aws.deploy.common.functions

aws.deploy.update:
	zip function.zip .
	aws lambda update-function-code --function-name health_handler --zip-file fileb://function.zip
