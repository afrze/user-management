# User Management

Simple flask framework app

- Install Python 3
- Clone the repo
- Create virtual environtment using `python -m venv venv`
- Activate environment `. venv/Scripts/activate`
- Install packages `pip install flask flask_alchemy`
- Initalize database using python terminal 
  - run `python` to open python terminal and run this line by line
  - `from app import app, db`
  - `app.app_context().push()`
  - `db.create_all()`
- Run the applciation using `python app.py`
