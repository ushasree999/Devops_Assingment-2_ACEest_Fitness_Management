# ACEest Fitness Management System

## Overview
This is a Flask-based web application for managing fitness and gym-related functionalities. It includes features for logging workouts, viewing summaries, and managing user information.

---

## Setup and Run the Application Locally

1. **Clone the Repository**:
   ```bash
  ## git clone <repository-url>
  ## cd <repository-folder>
   
2. Set Up a Virtual Environment:  
##python -m venv venv
##source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies:  
##pip install -r requirements.txt

4. Run the Application:  
##python app/app.py
##The application will be available at http://127.0.0.1:5000.

5. Execute Tests Locally
##Install Testing Dependencies: Ensure pytest is installed:  
##pip install pytest
##Run Tests:  
##pytest

6. GitHub Actions Pipeline Overview
##Trigger: The pipeline runs on every push to any branch.  
##Build Job:  
##Checks out the code.
##Sets up Python and installs dependencies.
##Runs pytest to execute unit tests.
##Builds the Docker image and runs the container.
##Deploy Job:
##Deploys the Dockerized application to AWS Elastic Beanstalk using the AWS CLI.
##Uses GitHub secrets for AWS credentials and region configuration.