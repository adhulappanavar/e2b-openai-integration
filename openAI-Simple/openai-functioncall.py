# pip install openai e2b-code-interpreter
import json
from openai import OpenAI
from e2b_code_interpreter import Sandbox

from dotenv import load_dotenv
load_dotenv()

# Create OpenAI client
client = OpenAI()
model = "gpt-4o"

# Define the messages
messages = [
    {
        "role": "user",
        "content": "Calculate how many r's are in the word 'strawberry'. Please use the execute_python tool to write code that counts the letters."
    }
]

# Define the tools
tools = [{
    "type": "function",
    "function": {
        "name": "execute_python",
        "description": "Execute python code in a Jupyter notebook cell and return result",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "The python code to execute in a single cell"
                }
            },
            "required": ["code"]
        }
    }
}]

# Generate text with OpenAI
print("=== STEP 1: Sending initial request to OpenAI ===")
print(f"User message: {messages[0]['content']}")
print(f"Available tools: {[tool['function']['name'] for tool in tools]}")

response = client.chat.completions.create(
    model=model,
    messages=messages,
    tools=tools,
)

# Append the response message to the messages list
response_message = response.choices[0].message
messages.append(response_message)

print("\n=== STEP 2: Analyzing OpenAI's response ===")
print(f"AI response content: {response_message.content}")
print(f"Tool calls requested: {len(response_message.tool_calls) if response_message.tool_calls else 0}")
if response_message.tool_calls:
    for i, tool_call in enumerate(response_message.tool_calls):
        print(f"  Tool call {i+1}: {tool_call.function.name}")
        print(f"  Arguments: {tool_call.function.arguments}")

# Execute the tool if it's called by the model
if response_message.tool_calls:
    print("\n=== STEP 3: Executing tool calls ===")
    for tool_call in response_message.tool_calls:
        if tool_call.function.name == "execute_python":
            print(f"Executing Python code for tool call ID: {tool_call.id}")
            
            # Create a sandbox and execute the code
            with Sandbox.create() as sandbox:
                code = json.loads(tool_call.function.arguments)['code']
                print(f"Code to execute:\n{code}")
                print("Executing in sandbox...")
                
                execution = sandbox.run_code(code)
                result = execution.text
                print(f"Execution result: {result}")

            # Send the result back to the model
            tool_message = {
                "role": "tool",
                "name": "execute_python",
                "content": result,
                "tool_call_id": tool_call.id,
            }
            messages.append(tool_message)
            print(f"Added tool result to conversation history")

# Generate the final response
print("\n=== STEP 4: Generating final response ===")
print(f"Total messages in conversation: {len(messages)}")
print("Sending complete conversation history to OpenAI for final response...")

final_response = client.chat.completions.create(
    model=model,
    messages=messages
)

print("\n=== FINAL RESULT ===")
print(final_response.choices[0].message.content)
