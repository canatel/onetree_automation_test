import os
from behave import Given, When, Then
from truth.truth import AssertThat

# Given Steps


@Given('I am on the login page')
def open_the_browser(context):
    if os.getenv("TARGET_HOST"):
        url = os.getenv("TARGET_HOST")
    else:
        url = f'{context.config.system.target_host}'
    context.driver.maximize_window()
    context.driver.get(url)

# When Steps


@When('I validate elements are displayed')
def validate_elements(context):
    elements_displayed = context.onetree_test.login_page.elements_displayed()
    AssertThat(elements_displayed).IsTrue()


@When('I login with "{}" and "{}" credentials')
def login(context, username, password):
    context.onetree_test.login_page.login(username, password)


# Then Steps


@Then('I validate I am on the home page')
def validate_home_page(context):
    elements_displayed = context.onetree_test.home_page.elements_displayed()
    AssertThat(elements_displayed).IsTrue()


@Then("I logout")
def logout(context):
    context.onetree_test.home_page.logout()


@Then('I can see a message saying "{}"')
def validate_error_message(context, message):
    message_displayed = context.onetree_test.login_page.validate_error_message_displayed(
        message)
    AssertThat(message_displayed).IsTrue()
