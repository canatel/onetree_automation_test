import os
import json
import logging
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional, Union
from types import SimpleNamespace

from selenium.webdriver import Chrome, ChromeOptions, Remote
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


class BaseConfig:
    def get_from_env(self, prefix: str = ''):
        for attr in self.__dict__.keys():
            if not getattr(self, attr):
                setattr(self, attr, os.getenv(f'{prefix}{attr.upper()}', None))


@dataclass
class System(BaseConfig):
    target_host:        Optional[str] = ''
    platform:           Optional[str] = 'linux'
    browser:            Optional[str] = 'chromium'
    browser_extra_args: Union[str, List[str]] = 'headless,incognito'

    def __post_init__(self):
        self.get_from_env()
        if isinstance(self.browser_extra_args, str):
            self.browser_extra_args = self.browser_extra_args.split(',')
        if isinstance(self.remote, str):
            self.remote = eval(self.remote)
        if isinstance(self.debug, str):
            self.debug = eval(self.debug)


@dataclass
class Config:
    system: System


def get_config_file(filename: Optional[str] = 'behave.json') -> Union[Path, None]:
    path = Path.cwd().joinpath(filename)
    return path if path.exists() else None


def parse_config(filename: str = 'behave.json') -> Union[Config, SimpleNamespace]:
    file = get_config_file(filename)

    if file is None:
        return Config(System())

    stream = open(file, 'r')
    return json.load(stream, object_hook=lambda config: SimpleNamespace(**config))


def build_defaults(config):
    if config.system.platform == 'windows':
        logging.info('Platform is windows, changing to local browser')
        config.system.remote = False
        logging.info('Platform is windows, enabling debug mode')
        config.system.debug = True
    else:
        logging.critical('Invalid platform, please check your settings.')
        raise RuntimeError('Invalid platform')


def build_driver(config, chromium_path='/usr/lib/chromium-browser/chromedriver',
                 options=None):
    path = ''
    if config.system.browser == 'chromium':
        logging.info('Using chromium')
        path = Path(chromium_path)
    elif config.system.browser == 'chrome':
        logging.info('Using chrome')
        path = ChromeDriverManager().install()

    if not path:
        msg = f'Invalid browser {config.system.browser}'
        logging.critical(msg)
        raise RuntimeError(msg)

    return Chrome(path, chrome_options=options)


def build_browser_options(config):
    options = ChromeOptions()

    if config.system.browser_extra_args:
        for arg in config.system.browser_extra_args:
            options.add_argument(f"--{arg}")
    return options


def build_environment(config):
    build_defaults(config)
    options = build_browser_options(config)
    return build_driver(config, options=options)
