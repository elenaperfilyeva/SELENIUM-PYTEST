# SELENIUM-PYTEST

This is an example of Selenium-pytest test automation framework with database (sqlite3) usage for a web application.

### Setup (Windows):
Activate virtual environment to run tests (run in PowerShell)
```
py -m venv env 
env/Scripts/activate
```

### Run e2e tests:
```
pytest --alluredir=reports -n 8
```

### Generate report
```
allure serve reports
```

#### Additional options

parallel execution
```
pytest -n 8
```

execute marked tests
```
-m display
-m search
```

browsers
```
--browser=chrome
--browser=firefox
```
