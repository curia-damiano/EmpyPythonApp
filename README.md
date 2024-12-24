# Empty Python App

A fully-configured starter template for Python applications, designed to streamline development and ensure best practices.<br/>
This repository provides a clean slate with everything you need for a modern Python project.


## Getting Started

I have written the following post to show parts of this project:
* [Empty Python App](https://curia.me/empty-python-app/)


## DevContainers:

* Based on Debian image
* Exposing the app on port 5000
* Installing default VS Code extensions
* Setting the PYTHONPATH environment variable
* Running the following commands:
  * Install NPM dependencies
  * Build TypeScript
  * Create the Python venv .venv
  * Activate the Python venv .venv
  * Install Python dependencies for development
  * Install Python dependencies for runtime


## Build & debug pipeline:

* Install NPM dependencies (every time, because of possible changes in package.json)
* Build Typescript
* Install Python dependencies for development (every time, because of changes in requirements-dev.txt)
* Install Python dependencies for runtime (every time, because of changes in requirements.txt)
* Run Ruff
* Run PyLint on 'src' folder
* Run PyLint on 'tests' folder
* Run Python Unit Tests


## Supported IDEs:

* Visual Studio Code


## Ruff

* Support from all IDEs
* Support from command line "ruff check src tests"


## PyLint

* Support from all IDEs
* Support from command line "pylint src"
* Support from command line "pylint tests"


## Unit Tests

* Support from all IDEs
* Support from command line "python -m unittest"
* Support from command line "python -m unittest discover -s tests"


## Others

* CleanAll.sh to clean all files produced from build
* Dockerfile


## Authors

* Curia Damiano - *Initial work* - [curia-damiano](https://github.com/curia-damiano)


## License

This project is licensed under the MIT License.
