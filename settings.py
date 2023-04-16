import os
from dotenv import load_dotenv

load_dotenv()

# Now you can access the environment variables defined in the .env file
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
