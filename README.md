<div align='center'>
<img src="assets/lyra.svg" style="width: 700px;" />
</div>

Lyra is a Python library for parsing and transforming JSON-based forms into Python code. It provides tools to parse form definitions and generate corresponding Python code, facilitating the handling of data from the Climate Data Store (CDS) in Python applications.

## Installation

To install Lyra, clone the repository and install the required dependencies:

```sh
git clone https://github.com/joangq/lyra
cd lyra
pip install -r requirements.txt
```

## Usage

Here's a simple example of how to use Lyra to download data using the `cds_collections` module:

```python
from lyra import cds_collections

cds_collections.reanalysis_era5_single_levels.download(
    product_type = "reanalysis",
    data_format  = "netcdf",
    variable     = "2m_temperature",
    year         = "2020",
    month        = "01",
    day          = "01",
    time         = "12:00",
)
```

This example demonstrates how to use the generated functions in `cds_collections` to request data directly from the CDS and save it to a file.

## How It Works

Lyra processes JSON form definitions from the CDS and transforms them into Python code that can be used to interact with the CDS API. The process involves three main components:

- **Parser**: The parser, implemented in `lyra.parser`, reads the JSON form definitions and creates an abstract syntax tree (AST) representation.

- **Transformer**: The transformer, found in `lyra.transformer`, takes the AST and transforms it into an intermediate representation suitable for code generation.

- **Translator**: The translator, located in `lyra.translator`, generates Python code from the intermediate representation, producing a set of functions that mirror the data request forms on the CDS.

This automated process allows users to interact with the CDS programmatically, without having to manually construct API requests.

## Repository Structure

The Lyra repository is organized as follows:

```python
Lyra/
├── src/                     # Main code (notebooks + library)
│   └── lyra/                # Library code
│       ├── parser/          # - JSON Form to AST parser
│       ├── transformer/     # - AST to intermediate representation
│       ├── translator/      # - IR to Python code (target cds_collections/)
│       ├── cds_collections/ # - Autogenerated target
│       └── auth/            # - Wrapper for dotenv-based authentication
├── data/                    # Example forms from the CDS.
├── tests/                   # Unit tests
├── assets/                  # Graphical assets
└── .env                     # Expected environament variables file.
```

---
<div align='right'>
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/joangq/lyra">lyra</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/joangq">Joan Gonzalez</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>
</div>
