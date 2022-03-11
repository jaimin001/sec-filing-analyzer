# sec-filing-analyzer

This Repository contains the Sec Filing Analyzer for Inter-IIT 10.0 by IITJ's team


Procedure:

- Install [python](https://www.python.org/downloads/) in your environment(pre-installed on Ubuntu).
- Navigate to the cloned repository.
  ```
  cd <project_directory_name>     #   Prometeo
  ```
- Create a new virtual environment and activate it.
  ```
  python -m venv env
  .\env\Scripts\activate
  ```
- Use pip to install other dependencies from `requirements.txt`
  ```
  pip install -r requirements.txt
  ```
- Copy .env file
  ```
  cp .env.example .env
  ```
- Make database migrations
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```
- Collect static files
  ```
  python manage.py collectstatic
  ```
- Create a superuser
  ```
  python manage.py createsuperuser
  ```
- Run development server on localhost
  ```
  python manage.py runserver
  ```
