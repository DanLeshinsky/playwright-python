# Playwright & Pytest

This project demonstrates a comprehensive setup for Web testing with Allure reports. It's designed to showcase best practices in creating and managing a robust testing environment using advanced technologies and patterns.

## Technologies/Tools used in building the framework
Pycharm - IDE

Python - Programming language

Pytest - Test Management library

Playwright - Web testing framework

Allure Reports - Reporting framework

Git - Version control

## Project Setup Locally
- Clone the project
- Navigate to the project directory
- Install requirements (dependencies) by running the following command:

    `pip install -r requirements.txt`
- Add .env file to the source with LOGIN and PASSWORD

## Run Locally

-  To run all tests locally with chrome browser and in headed mode with allure reports created, run the following command
  
     `pytest -sv --headed --browser chromium --alluredir=allure_results`

-  To see allure reports, run the following command

      `allure serve allure_results`

## Author

- [@DanLeshinsky](https://www.github.com/DanLeshinsky)
- +972-50-6676741

