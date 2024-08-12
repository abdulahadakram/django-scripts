# Update Static Paths Script

This Django management command updates static file paths in your HTML templates by replacing `../static/` references with Django's `{% static %}` template tag. This ensures that static file references are correctly managed within your Django project.

## Prerequisites

- Python 3.x
- Django

## Installation

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone <repository_url>
   cd <repository_directory>

2. **Add the Script to Your Django Project and Run It**

   1. **Locate or Create the Management Commands Directory:**

      Within one of your Django apps, create the following directory structure if it doesn't already exist:

      ```
      your_app/
          management/
              commands/
                  __init__.py
                  fix_static_references.py
      ```

      - `your_app/`: This is the directory of your Django app.
      - `management/commands/`: This is where Django management commands are stored.
      - `fix_static_references.py`: This is the script you cloned.

   2. **Copy the Script:**

      Copy the `fix_static_references.py` file from the cloned repository to the `management/commands/` directory in your Django app.

   3. **Ensure the `__init__.py` Files Exist:**

      Ensure that both the `management/` and `commands/` directories contain an `__init__.py` file. This file can be empty but is necessary for Python to treat the directories as packages.

   4. **Run the Script Using Django's `manage.py`**

      Use the following command to execute the script:

      ```bash
      python manage.py fix_static_references --directory /path/to/your/templates --backup
      ```

      - `--directory`: Specifies the directory to search for HTML files. If not provided, the script will use the first template directory specified in your Django settings.
      - `--backup`: If included, creates a backup of each file before modification.

      **Example Without Backup:**

      ```bash
      python manage.py fix_static_references --directory /path/to/your/templates
      ```

      **Example With Backup:**

      ```bash
      python manage.py fix_static_references --backup
      ```

      If no `--directory` is specified, the script will use the default template directory from your Django settings.
