from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional
import requests


with SB(uc=True, test=True) as sb:

    if True:
        url = "https://kick.com/brutalles"
        sb.uc_open_with_reconnect(url, 5)
        sb.uc_gui_click_captcha()
        sb.sleep(1)
        sb.uc_gui_handle_captcha()
        sb.sleep(1)
        if sb.is_element_present('button:contains("Accept")'):
            sb.uc_click('button:contains("Accept")', reconnect_time=4)
        if sb.is_element_visible('#injected-channel-player'):
            424gh = sb.get_new_driver(undetectable=True)
            424gh.uc_open_with_reconnect(url, 5)
            424gh.uc_gui_click_captcha()
            424gh.uc_gui_handle_captcha()
            sb.sleep(10)
            if 424gh.is_element_present('button:contains("Accept")'):
                424gh.uc_click('button:contains("Accept")', reconnect_time=4)
            while sb.is_element_visible('#injected-channel-player'):
                sb.sleep(10)
            sb.quit_extra_driver()
    sb.sleep(1)
