from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os


# Load the environment variables
load_dotenv()

api_key = os.getenv("API_KEY")

# Initialize Mira Client
client = MiraClient(config={"API_KEY": api_key})

# Load the flow configuration
flow = Flow(source="fashion_flow.yaml")

# Prepare test input
input_dict = {
    "wardrobe_items": "T-shirt, jeans, jacket, scarf",
    "season": "winter",
    "style_preference": "trendy"
}

# Test the flow
response = client.flow.test(flow, input_dict)

# Output the test results
print("Test Output:", response)
