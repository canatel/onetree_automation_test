"""Set test environment."""
import os
from pathlib import Path
from types import SimpleNamespace

import allure

# Project Modules
from features import pages
from features.utils.settings import parse_config, build_environment
from features.utils.logging_ import build_logger

# Project global configuration
config = parse_config()


def before_all(context):
    """Behave context components."""
    context.driver = build_environment(config)
    context.config = config
    context.logger = build_logger()

    context.onetree_test = SimpleNamespace()

    context.onetree_test.base_page = pages.BasePage(context.driver)
    context.onetree_test.login_page = pages.LoginPage(context)
    context.onetree_test.home_page = pages.HomePage(context)


def after_scenario(context, scenario):
    scenario_status = f'{scenario} :  {scenario.status}'
    context.logger.info(scenario_status.replace('"', '\\"'))


def after_step(context, step):
    if step.status == "failed":
        context.logger.info(f'{step} :  {step.status}')
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        parent_path = Path.cwd()
        os.chdir("failed_scenarios_screenshots")
        screenshot_name = f"{context.scenario.name.replace('/', ' ')} - {step.name.replace('/', ' ')}.png"
        context.driver.get_screenshot_as_file(screenshot_name)
        os.chdir(parent_path)
        try:
            allure.attach(
                context.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        except FileNotFoundError as e:
            context.logger.warn('Not able to attach screenshot')


def after_all(context):
    """Behave final steps."""
    context.driver.close()
