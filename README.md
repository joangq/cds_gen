<div align='center'>
<img src="assets/lyra.svg" style="width: 700px;" />
</div>

Lyra is a Python library for parsing and transforming JSON-based forms into Python code. It provides tools to parse form definitions and generate corresponding Python code, facilitating the handling of data from the Climate Data Store (CDS) in Python applications.

## Installation

To install Lyra, clone the repository and install the required dependencies:

```sh
git clone https://www.github.com/joangq/lyra
cd lyra
pip install -r requirements.txt
```

## Usage

Here's an example of how to use Lyra to parse and transform a form:

```python
from lyra.parser import parse_form
from lyra.transformer import transform_form

# Load a form JSON file
with open('data/satellite-lai-fapar-form.json', 'r') as f:
    form_json = json.load(f)

# Parse the form
ast = parse_form(form_json)

# Transform the form
transformed_ast = transform_form(ast)
```

## Repository Structure

The Lyra repository is organized as follows:

```python
Lyra/
├── src/                     # Main code (notebooks + library)
│   ├── lyra/                # Library code
│   │   ├── parser/          # - Contains functions to parse form JSON into an abstract syntax tree (AST).
│   │   ├── transformer/     # - Provides functionality to transform the AST into Python code.
│   │   └── auth/            # - Contains a wrapper to provide dotenv-based authentication
├── data/                    # Example forms from the CDS.
├── tests/                   # Unit tests
├── assets/                  # Graphical assets
└── .env                     # Expected environament variables file.
```