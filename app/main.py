import boto3
import json
from fastapi import FastAPI

AGENT_REGION = "af-south-1"
INTERFACE_LAMBDA_ARN = "arn:aws:lambda:{region}:{account}:function:{function_name}"

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the API"}

@app.get("/lambda")
def test_lambda():

    print("Connecting to lambda client")
    client = boto3.client("lambda", region_name=AGENT_REGION)

    print("Invoking lambda")
    payload = {"key": "dummy-from-ecs"}

    try:
        response = client.invoke(
            FunctionName=INTERFACE_LAMBDA_ARN,
            InvocationType="RequestResponse",
            Payload=json.dumps(payload)
        )
    except:
        response = {"message": "Error invoking lambda"}

    return response