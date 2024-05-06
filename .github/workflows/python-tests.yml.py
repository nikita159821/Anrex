name: Python Selenium Tests

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install selenium
        # Добавьте здесь любые другие зависимости, необходимые для вашего теста
    - name: Run Selenium tests
      run: |
        python -m unittest discover -s tests -p 'test_*.py'
