# Django Scripts Repository

This repository contains scripts related to Django development. Each script is designed to simplify and automate common tasks in Django projects. Relevant instructions for using each script can be found in the respective subfolder.

## Available Scripts

### 1. Update Static Paths
- **Description:** This script updates static file paths in your HTML templates by replacing `../static/` references with Django's `{% static %}` template tag. This helps ensure that your static files are correctly referenced across your project.
- **Instructions:** See the `update_static_paths/` folder for detailed usage instructions.


### 2. Create Default User
- **Description:**  This script creates a default user in your database if it doesn't already exist. It either takes the username, password, and email of the user from your environment or via command line arguments.
- **Instructions:** See the `create_default_user/` folder for detailed usage instructions.

## Usage

To get started with any of the scripts:

1. Clone the repository:

   ```bash
   git clone https://github.com/abdulahadakram/django-scripts.git
   cd django-scripts
