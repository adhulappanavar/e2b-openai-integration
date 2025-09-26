import sys
import base64
import json
from dotenv import load_dotenv
load_dotenv()
from e2b_code_interpreter import Sandbox
from openai import OpenAI

# Create sandbox
sbx = Sandbox.create()

# Upload the dataset to the sandbox
with open("./dataset.csv", "rb") as f:
    dataset_path_in_sandbox = sbx.files.write("dataset.csv", f)


def run_ai_generated_code(ai_generated_code: str):
    print('Running the code in the sandbox....')
    execution = sbx.run_code(ai_generated_code)
    print('Code execution finished!')

    # First let's check if the code ran successfully.
    if execution.error:
        print('AI-generated code had an error.')
        print(execution.error.name)
        print(execution.error.value)
        print(execution.error.traceback)
        sys.exit(1)

    # Iterate over all the results and specifically check for png files that will represent the chart.
    result_idx = 0
    for result in execution.results:
        if result.png:
            # Save the png to a file
            # The png is in base64 format.
            with open(f'chart-{result_idx}.png', 'wb') as f:
                f.write(base64.b64decode(result.png))
            print(f'Chart saved to chart-{result_idx}.png')
            result_idx += 1

prompt = f"""
I have a CSV file about movies. It has about 10k rows. It's saved in the sandbox at {dataset_path_in_sandbox.path}.
These are the columns:
- 'id': number, id of the movie
- 'original_language': string like "eng", "es", "ko", etc
- 'original_title': string that's name of the movie in the original language
- 'overview': string about the movie
- 'popularity': float, from 0 to 9137.939. It's not normalized at all and there are outliers
- 'release_date': date in the format yyyy-mm-dd
- 'title': string that's the name of the movie in english
- 'vote_average': float number between 0 and 10 that's representing viewers voting average
- 'vote_count': int for how many viewers voted

I want to better understand how the vote average has changed over the years.
Write Python code that analyzes the dataset based on my request and produces right chart accordingly"""

client = OpenAI()
print("Waiting for model response...")

# Define the tools for OpenAI function calling
tools = [{
    "type": "function",
    "function": {
        "name": "run_python_code",
        "description": "Run Python code in a Jupyter notebook cell and return result",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "The Python code to execute in a single cell"
                }
            },
            "required": ["code"]
        }
    }
}]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}],
    tools=tools,
)

# Check if OpenAI wants to call the function
response_message = response.choices[0].message
if response_message.tool_calls:
    for tool_call in response_message.tool_calls:
        if tool_call.function.name == "run_python_code":
            code = json.loads(tool_call.function.arguments)['code']
            print("Will run following code in the sandbox:")
            print(code)
            print("-" * 50)
            # Execute the code in the sandbox
            run_ai_generated_code(code)
else:
    print("OpenAI response:")
    print(response_message.content)

