# playwright-qa-framework-v2

A personal repo for learning Playwright and pytest through hands-on test automation against [Sauce Demo](https://www.saucedemo.com/).

## Tech Stack

- Python 3.x
- Playwright 1.60.0
- pytest 9.1.0
- pytest-playwright 0.8.0

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

## Running Tests

```bash
pytest                      # run all tests
pytest tests/test_login.py  # run a specific file
pytest --headed             # run with browser visible
pytest -v                   # verbose output
```