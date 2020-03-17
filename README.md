## python-selenium-page-object-behave-test
Example tests from native Python to Behave

### Setup

#### Install virtual enc 
```python3 -m pip install --user virtualenv```
#### Create new env
```python3 -m venv env```
#### Activiate env
```source env/bin/activate```

### Run Functional tests
```pytest```

### Run Behave tests
```behave```

### Run Performance tests
#### Run Flash API server
```python flask_mock_service.py```
#### Run Performance test
```python perf_test_rest_api.py```
