<h1 align = center> CONTRIBUTION GUIDELINES </h1>

# Tech Stack

[![Django](https://img.shields.io/badge/Django-3.2-green?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-blue?logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)
[![Python](https://img.shields.io/badge/Python-3.8-blue?logo=python&logoColor=white)](https://www.python.org/)



## Forking the Repository

To contribute to this project, you need to fork the repository to your GitHub account. Follow the steps below:

1. **Fork the repository:**
   - Click on the "Fork" button at the top right of this page. This will create a copy of the repository in your GitHub account.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/Linkscrape.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd Linkscrape
    ```

3. **Create a virtual environment:**

    ```bash
    python -m venv myenv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        .\myenv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source myenv/bin/activate
        ```
        
        - To install all the requirements:
         ```bash
        pip3 install -r requirements.txt
        ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. Visit `http://127.0.0.1:8000/` in your browser.
7. **Database Migrations:**
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
   ```

9. ## Creating Branches and Adding Changes

To contribute to the project, it's recommended to create a new branch for each feature or bug fix. Follow these steps:

1. **Create a new branch:**
   - Navigate to your project's directory:

     ```bash
     cd Linkscrape
     ```

   - Create a new branch for your changes:

     ```bash
     git checkout -b feature-or-bugfix-branch
     ```

2. **Make changes:**
   - Make the necessary changes to the code, add new features, or fix bugs.

3. **Stage and commit your changes:**
   - Stage your changes:

     ```bash
     git add .
     ```

   - Commit your changes with a meaningful message:

     ```bash
     git commit -m "Add your meaningful commit message here"
     ```

4. **Push your branch to your fork:**
   - Push your changes to your forked repository:

     ```bash
     git push origin feature-or-bugfix-branch
     ```

5. **Submit a Pull Request:**
   - Go to your forked repository on GitHub.
   - Click on "Compare & pull request" for the branch you just pushed.
   - Fill in the pull request details and submit it.
