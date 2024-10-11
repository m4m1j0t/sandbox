# About

Create a new virtual environment (if you do not already have one)
```sh
python3 -m venv .venv
```

Activate it (either like below or via VSCode plugin)
```sh
source .venv/bin/activate
```
Succsessful activation is indicated by `(.venv)` in the left corner of the terminal.

Install requirements to your local environment
```sh
pip install - requirements.txt
```

Launch the tests
```sh
pytest .
```