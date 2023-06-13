# DevOps-Test

This project is for testing purpose only.

## Development Notes

- Always create a branch from the main branch and then create a pull-request for your changes, you need at least 1 approve
- When creating a branch, use the following naming convention: `<issue name>` or `feature` or `refactor`

This project also has been set up to support the use of `pipenv` to allow developers and pipelines to run the tests and builds with the same set of Python packages. It's **HIGHLY** recommended that when you are doing any development work, that you do them inside a `virtualenv` that has been set up by `pipenv`.

### Setting up virtualenv

Firstly you will obviously need to have `python3` and `python3-pip` installed on your development environment. This document won't go into detail about how to do this for your chosen development environment, but it should be pretty straightforward.

Installing `pipenv` is as simple as running `pip3 install -U pipenv`. Once you have it installed, you are ready to set up your Python `virtualenv` and get started with running or testing this code.

Running `pipenv install` will create a `virtualenv` and also install all the packages listed as dependencies in the Pipfile you can find in the top level of this project. The following packages will be installed into the virtualenv:

```text
[packages]
PyInstaller = "5.12.0"
pytest = "7.1.3"
pynput = "1.7.6"
```

Once the command has finished running, you are ready to launch the `virtualenv` by running `pipenv shell`.

From now on you can run the application by running `python main.py`

To run the PyTests run `python.exe -m pytest`

To build the project run `pyinstaller main.py --onefile`
