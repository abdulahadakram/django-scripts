# Update Static Paths Script

This Django management command creates a default user in your database if it doesn't already exist. It either takes the username, password, and email of the user from your environment or via command line arguments.

## Prerequisites

- Python 3.x
- Django

## Installation

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/abdulahadakram/django-scripts.git
   cd django-scripts

2. **Add the Script to Your Django Project and Run It**

   1. **Locate or Create the Management Commands Directory:**

      Within one of your Django apps, create the following directory structure if it doesn't already exist:

      ```
      your_app/
          management/
              commands/
                  __init__.py
                  create_default_user.py
      ```

      - `your_app/`: This is the directory of your Django app.
      - `management/commands/`: This is where Django management commands are stored.
      - `create_default_user.py`: This is the script you cloned.

   2. **Copy the Script:**

      Copy the `create_default_user.py` file from the cloned repository to the `management/commands/` directory in your Django app.

   3. **Ensure the `__init__.py` Files Exist:**

      Ensure that both the `management/` and `commands/` directories contain an `__init__.py` file. This file can be empty but is necessary for Python to treat the directories as packages.

   4. **Run the Script Using Django's `manage.py`**

      Use the following command to execute the script:

      ```bash
      python manage.py create_default_user --directory /path/to/your/templates --backup
      ```
   5. **Run the Script Using Django's `manage.py`**

         Use the following command to execute the script:

         ```bash
         python manage.py create_default_superuser
         ```
         This will create a superuser with the username, password, and email specified by environment variables or command-line arguments if one does not already exist.
         - `--username`: (Optional) Specifies a custom username for the superuser.
         - `--password`: (Optional) Specifies a custom password for the superuser.
         - `--email`: (Optional) Specifies a custom email for the superuser.
   
   **Example with Custom Arguments:**

      ```bash
      python manage.py create_default_superuser --username new_admin --password new_password --email new_admin@example.com
      ```
      If no `--username`, `--password`, or `--email` is specified, the script will use the default values from the environment variables SU_NAME, SU_PASS, and SU_EMAIL.   