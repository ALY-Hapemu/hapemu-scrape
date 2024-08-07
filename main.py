import subprocess

def run_script(script_name):
    try:
        subprocess.run(['python', script_name], check=True)
        print(f"{script_name} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute {script_name}: {e}")

# Execute scripts in the specified order
run_script('antutu.py')
run_script('dxomark.py')
run_script('gsmarena.py')
run_script('upload_data.py')
