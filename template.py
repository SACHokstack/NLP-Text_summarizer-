import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s:')

project_name = 'TextSummarizer'

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "paras.yaml",
    "app.py",
    "main.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "README.md"  # Add README.md file to the list
]

# Content for the README.md
readme_content = f"""
# {project_name}

## Project Overview
**{project_name}** is a Python project designed to summarize text documents. The project is modular and well-structured, following best practices in software engineering.

## Project Structure
The project contains the following major components:
- **src/**: Contains the main source code for the project.
  - **utils/**: Utility functions and common methods.
  - **config/**: Configuration management.
  - **pipeline/**: Text summarization pipeline.
  - **logging/**: Custom logging utilities.
  - **entity/**: Contains entities for data handling.
  - **constants/**: Contains project constants.
- **config/config.yaml**: Configuration file for the project.
- **app.py**: Main application script.
- **main.py**: Entry point for the project.
- **research/**: Contains research notebooks.

## Getting Started

1. Clone the repository:
    ```bash
    git clone <repo-url>
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the main application:
    ```bash
    python main.py
    ```

## Requirements
- Python 3.x
- Dependencies listed in `requirements.txt`
"""

# Loop through the list of files and create them
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Check if the file is README.md and write content to it
    if filename == "README.md":
        with open(filepath, 'w') as f:
            f.write(readme_content)
        logging.info(f"Creating README.md with project information")
    # For all other files, create them if they do not exist or are empty
    elif not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
