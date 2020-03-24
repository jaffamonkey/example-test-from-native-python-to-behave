## python-selenium-page-object-behave-test
Example tests from native Python to Behave

### Setup

#### Install virtual enc 
```python3 -m pip install --user virtualenv```
#### Create new env
```python3 -m venv env```
#### Activiate env
```source env/bin/activate```

#### Download latest Chromedriver
```
curl -SL https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_mac64.zip > chromedriver.zip
unzip chromedriver.zip -d bin/
```

### Run Python UI tests
```
python3 python3-selenium-headless.py
python3 python3-selenium.py
```

### Run Pytest API tests
```pytest```

### Run Behave tests
```behave```

### Run Performance tests
#### Run Flash API server
```python ./api/flask_mock_service.py```
#### Run Performance test
```python ./api/perf_test_rest_api.py```
