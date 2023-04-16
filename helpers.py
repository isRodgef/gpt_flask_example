import openai
import settings
from functools import lru_cache

openai.api_key =  settings.OPENAI_API_KEY

# This function takes in a prompt and a state and returns a response
### add lru_cache_decorator


@lru_cache(maxsize=512)
def get_answer(prompt):
    # Set up the model and prompt

    setup_bot = [{"role" :"system", "content": prompt}]
    
    model_engine = "gpt-3.5-turbo"

    # Generate a response
    completion = openai.ChatCompletion.create(
        model=model_engine,
        messages=setup_bot,
    )

    response = completion.choices[0]["message"]["content"]
    return response

