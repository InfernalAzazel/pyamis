import subprocess
import os
import shutil

def remove_dir(dir_path: str):
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        shutil.rmtree(dir_path)
        print(f"Removed directory: {dir_path}")
    else:
        print(f"Directory does not exist: {dir_path}")

def remove_file(file_path):
    if os.path.exists(file_path) and os.path.isfile(file_path):
        os.remove(file_path)
        print(f"Removed file: {file_path}")
    else:
        print(f"File does not exist: {file_path}")



def run_pytest():
    try:
        subprocess.run([
            'pytest',
            '--cov=./tests',
            '--cov-report=html:./outputs/cov-report',
            '--cov-report=term-missing',
            '--html=./outputs/test-report.html'
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    remove_dir('./outputs')
    remove_file('./.coverage')
    run_pytest()
    remove_file('./.coverage')