
import os
import booking.constants as const
from selenium import webdriver


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"/home/mrawal/Downloads/chromedriver",teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

