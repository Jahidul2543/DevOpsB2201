
aws lambda create-function \
    --function-name token-function-b2201 \
    --runtime python3.9 \
    --zip-file fileb://Archive.zip \
    --handler lambda_function.lambda_handler \
    --role arn:aws:iam::666680140343:role/service-role/myLambdaRole \
    --description "This is a demo function created from CLI"


aws lambda update-function-code \
    --function-name  token-function-b2201 \
    --zip-file fileb://Archive.zip