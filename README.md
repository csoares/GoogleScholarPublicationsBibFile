# Retrieve informations from Google Scholar and create a bib file of references

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

This project will automatically retrieve and generate information from the last publications of researchers and store it in a reference.bib file. This file will be used to generate an online page with the last publications of the research team. Thus, it will always be updates since a cron task will retrieving information about the last research on google scholar.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

You need to have python 3 installed, and install the dependencies specified in the requirements.txt file.


### Installing

A step by step series of examples that tell you how to get a development env running.
Install the dependencies.

```
pip3 install -r requirements.txt
```

Duplice the .env.example file to .env, and setup the key to start doing request to google scholar API. Execute the script.

```
python3 main.py
```

## Usage <a name = "usage"></a>

Feel free to ask more information about the usage, or get some great and fresh recommendations.
