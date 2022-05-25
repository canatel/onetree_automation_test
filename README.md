# **Automation Framework for Onetree Technical Test**

## **Preconditions**

To run this project you must have configured the following tools in your computer:

- [Python 3.9](https://www.python.org/downloads/release/python-396/)
- [Pipenv](https://pypi.org/project/pipenv/2021.5.29/)

## **Initial Configuration**

Once you have installed the tools from before, to set up the project locally just clone this repository within your personal computer and run the following commands.

- Open CMD withing the project root folder and run:
  > - pipenv install
  > - pipenv shell

This will set up the environment for you to run the test scenarios.

## **Run the project**

To run the project once you have install the dependencie packages from the step before and opened the python environment where the project is running, execute the following commands to excecute the test scenarios:

- Use this if you just want to run the test scenarios and not have any report

  > behave

- Use this if you want to generate an allure report with the executed test scenarios, once you run this command, you must serve the reports as is indicated next:

  > behave -f allure_behave.formatter:AllureFormatter -o allure/results/ ./features

- This will create the html from the report created on the last command.

  > allure generate allure/results/ -o allure/reports --clean

- This will serve the allure report in a web page for you to review it.

  > allure open allure/reports
