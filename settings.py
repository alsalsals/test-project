from typing import Literal, Optional
import dotenv
from pydantic_settings import BaseSettings
from test_project.utils import path

BrowserType = Literal['chrome', 'firefox']


class Settings(BaseSettings):
    base_url: str = 'https://evvve.net/'
    driver_name: BrowserType = 'chrome'
    window_width: int = 1024
    window_height: int = 768
    timeout: float = 3.0
    headless: bool = False

    selenoid_login: str = None
    selenoid_password: str = None

    remote_url: Optional[str] = None
    remote_version: Optional[str] = None
    remote_platform: Optional[str] = None
    remote_enableVNC: bool = True
    remote_screenResolution: str = '1920x1080x24'
    remote_enableVideo: bool = False
    remote_enableLog: bool = True

    hold_browser_open: bool = False
    save_page_source_on_failure: bool = True
    author: str = "QA-Automation"


dotenv.load_dotenv()
config = Settings(_env_file=dotenv.find_dotenv())
