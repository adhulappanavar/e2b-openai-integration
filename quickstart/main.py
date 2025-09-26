from dotenv import load_dotenv
load_dotenv()
from e2b_code_interpreter import Sandbox

sbx = Sandbox.create() # By default the sandbox is alive for 5 minutes
execution = sbx.run_code("print('hello world')") # Execute Python inside the sandbox
print(execution.logs)

files = sbx.files.list("/")
print("Files and directories in /:")
print("-" * 50)
for file in files:
    file_type = "DIR" if file.type.value == "dir" else "FILE"
    size_str = f"{file.size:,} bytes" if file.size > 0 else "0 bytes"
    print(f"{file_type:4} | {file.name:20} | {size_str:12} | {file.permissions}")
