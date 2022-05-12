
aws cloudformation create-stack \
    --stack-name app-b2201 \
    --template-body file://template.yaml \
    --parameters file://parameters.json

aws cloudformation update-stack \
    --stack-name app-b2201 \
    --template-body file://template.yaml \
    --parameters file://parameters.json

aws cloudformation validate-template --template-body file://template.yaml