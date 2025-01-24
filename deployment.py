from mira_sdk import MiraClient, Flow
from mira_sdk.exceptions import FlowError
from dotenv import load_dotenv
import os


# Load the environment variables
load_dotenv()

api_key = os.getenv("API_KEY")

# Initialize Mira Client
client = MiraClient(config={"API_KEY": api_key})

# Load the flow
flow = Flow(source="fashion_flow.yaml")

# Deploy the flow
try:
    client.flow.deploy(flow)
    print("Flow deployed successfully!")
except FlowError as e:
    print(f"Error during deployment: {str(e)}")
