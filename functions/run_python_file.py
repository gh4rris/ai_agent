import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    absolute_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(absolute_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    if not os.path.isfile(target_file) and not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        commands = ["python", target_file]
        if args:
            commands.extend(args)
        result = subprocess.run(commands, timeout=30, capture_output=True, cwd=working_directory, text=True)
        output = []
        if result.stdout:
            output.append(f"STDOUT: \n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR: \n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files within working directory and returns output from the interpreter",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The filepath of the python file to execute",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional argument element to pass to the Python file"
                ),
                description="Optional list of arguments to pass to the Python file",
            ),
        },
    ),
)