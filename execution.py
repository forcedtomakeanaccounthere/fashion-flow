from mira_sdk import MiraClient
from dotenv import load_dotenv
import os


# Load the environment variables
load_dotenv()

api_key = os.getenv("API_KEY")

# Initialize Mira Client
client = MiraClient(config={"API_KEY": api_key})

# Set version and input data
version = "1.0.0"
input_data = {
    "wardrobe_items": "T-shirt, jeans, jacket, scarf",
    "season": "winter",
    "style_preference": "trendy"
}

# Define flow name
flow_name = f"abhishek/fashion-flow/{version}"

# Execute the flow
result = client.flow.execute(flow_name, input_data)
print("Fashion Recommendations:", result)
