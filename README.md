# Upgrade Python Version on AWS Elastic Beanstalk Using pyenv
This project demonstrates how to deploy a Python application(Flask) on AWS Elastic Beanstalk and upgrade the Python version on the server using pyenv.

## Local Development
To use this project, you should have Python and pip installed on your local machine.

1. Clone the repository:
```
git clone https://github.com/your-username/python-pyenv-upgrade-on-elasticbeanstalk.git
```
2. Navigate to the project directory:
```
cd python-pyenv-upgrade-on-elasticbeanstalk
```
3. Create a virtual environment:
```
python -m venv venv
```
4. Activate the virtual environment:
On Windows:
```
venv\Scripts\activate.bat
```
On Linux and macOS:
```
source venv/bin/activate
```
5. Install the dependencies:
```
pip install -r requirements.txt
```
6. Run the application:
```
python app.py
```
7. Open http://localhost:5000 in your browser.
8. The application should be running. The home page will display the Python version on the server.

## Usage
To deploy the Flask application on Elastic Beanstalk:
1. Create an Elastic Beanstalk environment using the AWS Management Console or the AWS CLI.
2. Configure environment variables in the AWS Management Console:
  - Navigate to the Elastic Beanstalk environment dashboard and click on the "Configuration" tab.
  - Under "Software", click on "Edit".
  - Scroll down to the "Environment properties" section.
  - Add the following environment variables:
    - `PYTHON_VERSION`: The Python version to be installed on the server.
    - `PYTHONPATH`: The path to the virtual environment for the application. This is set by default by Elastic Beanstalk to `/var/app/venv/staging-LQM1lest/bin`.
2. Deploy the new application version to the Elastic Beanstalk environment using the AWS Management Console or eb CLI.
```
eb deploy
```
3. Open the application URL in your browser.
4. The application should be running. The home page will display the Python version on the server.

## How it works on Elastic Beanstalk
The `00_upgrade_python.config` file in the `.ebextensions` directory is used to upgrade the Python version on the server to a specified version using pyenv. The following steps are performed:
1. Install pyenv.
2. Install the specified Python version.
3. Set the Python version as the global version.
4. Update the virtual environment path to the new Python version.
