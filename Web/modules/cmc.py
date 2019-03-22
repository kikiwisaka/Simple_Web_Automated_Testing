import time

from ..screens.screen import Screen
from ..utils import helper
from ..utils import config
from ..utils import datadog
from ..utils.helper import Get

datadog_helper = datadog.DataDogHelper()
logger_helper = helper.LoggerHelper()
custom_logger = logger_helper.json_logger()


class bbm_cmc(object):

    def __init__(self, driver):
        self.driver = driver
        self.screen = Screen(driver)
        self.object = Get.cmc_repository()
        self.random_string = helper.random_id(5)

    def login(self):
        custom_logger.warning("{0}]".format("login"))
        self.screen.wait_until_element_visible(self.object["bbm_logo"]["by"], self.object["bbm_logo"]["locator"])
        self.screen.find_element_and_input_javascript(self.object["email_address"]["by"],
                                                      self.object["email_address"]["locator"], 5,
                                                      config.Get.bbm_cmc_email())
        self.screen.find_element_and_input(self.object["password"]["by"], self.object["password"]["locator"], 5,
                                           config.Get.bbm_cmc_password())
        if self.screen.click_element(self.object["sign_in_button"]["by"],
                                     self.object["sign_in_button"]["locator"]):
            if self.screen.wait_until_element_visible(self.object["create_new_channel"]["by"],
                                                      self.object["create_new_channel"]["locator"], 15):
                custom_logger.debug("Test case {0} passed]".format("login"))
                assert True, "User is able to login successfully"
            else:
                custom_logger.warning("{0}]".format("Home page after sign in is not displayed"))
                assert False, "Home page after sign in is not displayed"
        else:
            custom_logger.error("Test case {0} failed]".format("login"))
            assert False, "Click on Sign button is failed"

    def logout(self):
        if self.screen.wait_until_element_visible("xpath",
                                                  "//div[text()='Login']"):
            self.screen.click_element("xpath", "//div[text()='Login']")
            self.screen.wait_until_element_visible("xpath",
                                                   "//div[@class='q-item-main q-item-section']//div[contains(.,'Account')]")
            self.screen.click_element("xpath", "//div[@class='q-item-main q-item-section']//div[contains(.,'Account')]",
                                      4)
            self.screen.wait_until_element_visible("xpath",
                                                   "//div[@class='q-btn-inner row col items-center justify-center']//div[contains(.,'Logout')]")
            self.screen.click_element("xpath",
                                      "//div[@class='q-btn-inner row col items-center justify-center']//div[contains(.,'Logout')]",
                                      5)
            if self.screen.wait_until_element_visible("xpath",
                                                      "//div[@class='q-btn-inner row col items-center justify-center']//div[contains(.,'Get Started')]",
                                                      5):
                assert True
            else:
                assert False
        else:
            self.screen.wait_until_element_visible("xpath",
                                                   "//div[@class='q-item-main q-item-section']//div[contains(.,'Account')]")
            self.screen.click_element("xpath", "//div[@class='q-item-main q-item-section']//div[contains(.,'Account')]",
                                      4)
            self.screen.wait_until_element_visible("xpath",
                                                   "//div[@class='q-btn-inner row col items-center justify-center']//div[contains(.,'Logout')]")
            self.screen.click_element("xpath",
                                      "//div[@class='q-btn-inner row col items-center justify-center']//div[contains(.,'Logout')]",
                                      5)
            if self.screen.wait_until_element_visible("xpath",
                                                      "//div[@class='q-btn-inner row col items-center justify-center']//div[contains(.,'Get Started')]",
                                                      5):
                assert True
            else:
                assert False

    def navigate_to_channel_detail_page(self):
        custom_logger.warning("{0}]".format("navigate_to_channel_detail_page"))
        try:
            self.screen.wait_until_element_visible(self.object["create_new_channel"]["by"]
                                                   , self.object["create_new_channel"]["locator"])
            if self.screen.click_element(self.object["channel_selambe"]["by"],
                                         self.object["channel_selambe"]["locator"], 5):
                if self.screen.wait_until_element_visible(self.object["selambe_details_page"]["by"],
                                                          self.object["selambe_details_page"]["locator"]):
                    assert True
                else:
                    custom_logger.error("{0}]".format("Selambe channel details page is not displayed"))
                    assert False, "Selambe channel details page is not displayed"
            else:
                custom_logger.error("{0}]".format("Click Selambe channel is failed"))
                assert False, "Click Selambe channel is failed "
        except AssertionError as e:
            custom_logger.error("{0} failed]".format("navigate_to_channel_detail_page"))
            raise e

    def navigate_to_chat_bot(self):
        custom_logger.warning("{0}]".format("navigate_to_chat_bot"))
        try:
            self.screen.wait_until_element_visible(self.object["chat_bot_icon"]["by"]
                                                   , self.object["chat_bot_icon"]["locator"])
            if self.screen.click_element(self.object["chat_bot_icon"]["by"],
                                         self.object["chat_bot_icon"]["locator"], 5):
                if self.screen.wait_until_element_visible(self.object["chat_bot_settings"]["by"],
                                                          self.object["chat_bot_settings"]["locator"]):
                    assert True
                else:
                    custom_logger.error("{0} failed]".format("Chat Bot tab is displayed"))
                    assert False, "Chat Bot tab is displayed"
            else:
                custom_logger.error("{0} failed]".format("Click Chat Bot tab is failed"))
                assert False, "Click Chat Bot tab is failed "
        except AssertionError as e:
            custom_logger.error("{0} failed]".format("navigate_to_chat_bot"))
            raise e

    def send_chat_bot_video_broadcast(self):
        try:
            self.screen.wait_until_element_visible(self.object["video_broadcast"]["by"]
                                                   , self.object["video_broadcast"]["locator"])
            if self.screen.click_element(self.object["video_broadcast"]["by"],
                                         self.object["video_broadcast"]["locator"], 5):
                if self.screen.wait_until_element_visible(self.object["video_link"]["by"],
                                                          self.object["video_link"]["locator"]):
                    self.screen.find_element_and_input(self.object["video_link"]["by"],
                                                       self.object["video_link"]["locator"], 5,
                                                       "https://www.vidio.com/watch/1257896")
                    if self.screen.click_element(self.object["fetch_button"]["by"],
                                                 self.object["fetch_button"]["locator"], 5):
                        time.sleep(2)
                        if self.screen.click_element(self.object["video_preview_button"]["by"],
                                                     self.object["video_preview_button"]["locator"], 5):
                            if self.screen.click_element(self.object["video_broadcast_button"]["by"],
                                                         self.object["video_broadcast_button"]["locator"], 5):

                                self.screen.wait_until_element_visible(self.object["broadcast_sent"]["by"]
                                                                       , self.object["broadcast_sent"]["locator"])
                                assert True
                            else:
                                assert False, "Click Broadcast is failed"
                        else:
                            assert False, "Click Preview is failed"
                    else:
                        assert False, "Click Fetch button is failed"

                else:
                    assert False, "Video Broadcast form is not displayed "
            else:
                assert False, "Click Chat Bot Video   broadcast tab is failed "
        except AssertionError as e:
            raise e

    def send_chat_bot_broadcast(self):
        custom_logger.warning("{0}]".format("send_chat_bot_broadcast"))
        try:
            self.screen.wait_until_element_visible(self.object["chat_bot_broadcast_icon"]["by"]
                                                   , self.object["chat_bot_broadcast_icon"]["locator"])
            if self.screen.click_element(self.object["chat_bot_broadcast_icon"]["by"],
                                         self.object["chat_bot_broadcast_icon"]["locator"], 5):
                if self.screen.wait_until_element_visible(self.object["broadcast_title"]["by"],
                                                          self.object["broadcast_title"]["locator"]):
                    self.screen.find_element_and_input(self.object["broadcast_title"]["by"],
                                                       self.object["broadcast_title"]["locator"], 5,
                                                       "Chat Broadcast")
                    self.screen.find_element_and_input(self.object["broadcast_message"]["by"],
                                                       self.object["broadcast_message"]["locator"], 5,
                                                       "Chat Broadcast at "
                                                       + time.strftime('%d/%m/%Y %H:%M:%S')
                                                       + " - Partner Monitoring")
                    self.screen.find_element_and_input(self.object["broadcast_button_label"]["by"],
                                                       self.object["broadcast_button_label"]["locator"], 5,
                                                       "Broadcast Link")
                    self.screen.find_element_and_input(self.object["broadcast_button_url"]["by"],
                                                       self.object["broadcast_button_url"]["locator"], 5,
                                                       "https://www.google.com")
                    if self.screen.click_element(self.object["broadcast_preview_button"]["by"],
                                                 self.object["broadcast_preview_button"]["locator"], 5):
                        if self.screen.click_element(self.object["broadcast_button"]["by"],
                                                     self.object["broadcast_button"]["locator"], 5):
                            self.screen.wait_until_element_visible(self.object["broadcast_sent"]["by"]
                                                                   , self.object["broadcast_sent"]["locator"])
                            assert True

                        else:
                            assert False, "Click Broadcast is failed"
                    else:
                        assert False, "Click Preview button is failed"

                else:
                    assert False, "Broadcast form is not displayed "
            else:
                assert False, "Click Chat Bot  broadcast tab is failed "
        except AssertionError as e:
            raise e

    def send_channel_regular_post(self):
        try:
            self.screen.wait_until_element_visible(self.object["tab_posts"]["by"]
                                                   , self.object["tab_posts"]["locator"])
            if self.screen.click_element(self.object["tab_posts"]["by"],
                                         self.object["tab_posts"]["locator"], 5):
                self.screen.find_element_and_input(self.object["regular_post_title"]["by"],
                                                   self.object["regular_post_title"]["locator"], 5,
                                                   "Title : Post at " + time.strftime('%d/%m/%Y %H:%M:%S'))
                self.screen.find_element_and_input(self.object["regular_post_message"]["by"],
                                                   self.object["regular_post_message"]["locator"], 5,
                                                   "Message: Test posting at "
                                                   + time.strftime('%d/%m/%Y %H:%M:%S')
                                                   + " - Partner Monitoring")
                if self.screen.click_element(self.object["regular_post_button"]["by"],
                                             self.object["regular_post_button"]["locator"], 5):
                    self.screen.wait_until_element_visible(self.object["past_last_bcast"]["by"]
                                                           , self.object["past_last_bcast"]["locator"].format(
                            "Title : Post at " + time.strftime('%d/%m/%Y %H:%M:%S')))
                    assert True
                else:
                    assert False, "Regular Post was not successfull"
            else:
                assert False, "Tab Post was not successfull"

        except AssertionError as e:
            raise e

    def send_channel_buy_now_post(self):
        try:
            self.screen.wait_until_element_visible(self.object["tab_posts"]["by"]
                                                   , self.object["tab_posts"]["locator"])
            if self.screen.click_element(self.object["tab_posts"]["by"],
                                         self.object["tab_posts"]["locator"], 5):
                self.screen.wait_until_element_visible(self.object["buy_now_tab"]["by"],
                                                       self.object["buy_now_tab"]["locator"])
                if self.screen.click_element(self.object["buy_now_tab"]["by"],
                                             self.object["buy_now_tab"]["locator"], 5):

                    self.screen.find_element_and_input(self.object["regular_post_title"]["by"],
                                                       self.object["regular_post_title"]["locator"], 5,
                                                       "Title : Buy Now Post at " + time.strftime('%d/%m/%Y %H:%M:%S'))

                    self.screen.find_element_and_input(self.object["regular_post_message"]["by"],
                                                       self.object["regular_post_message"]["locator"], 5,
                                                       "Message: Buy now post at "
                                                       + time.strftime('%d/%m/%Y %H:%M:%S')
                                                       + " - Partner Monitoring")

                    self.screen.find_element_and_input(self.object["link_caption"]["by"],
                                                       self.object["link_caption"]["locator"], 5,
                                                       "https://www.google.com")

                    self.screen.find_element_and_input(self.object["buy_now_caption"]["by"],
                                                       self.object["buy_now_caption"]["locator"], 5,
                                                       "!")

                    self.screen.click_element_javascript(self.object["buy_now_post_button"]["by"], self.object["buy_now_post_button"]["locator"])

                    assert True

                else:
                    assert False, "Tap Tab Buy Now Post was not successful"
            else:
                assert False, "Tab Post was not successful"

        except AssertionError as e:
            raise e

    def send_video_post(self):
        try:
            self.screen.wait_until_element_visible(self.object["tab_posts"]["by"]
                                                   , self.object["tab_posts"]["locator"])
            if self.screen.click_element(self.object["tab_posts"]["by"],
                                         self.object["tab_posts"]["locator"], 5):
                self.screen.wait_until_element_visible(self.object["post_video_tab"]["by"],
                                                       self.object["post_video_tab"]["locator"])
                if self.screen.click_element(self.object["post_video_tab"]["by"],
                                             self.object["post_video_tab"]["locator"], 5):

                    self.screen.find_element_and_input(self.object["post_video_link"]["by"],
                                                       self.object["post_video_link"]["locator"], 5,
                                                       "https://www.vidio.com/watch/1573094-laga-terakhir-liliyana-natsir-di-bulu-tangkis")

                    self.screen.click_element(self.object["post_video_fetch"]["by"],
                                                         self.object["post_video_fetch"]["locator"])

                    if self.screen.wait_until_element_visible(self.object["post_video_thumbnail"]["by"]
                                                           , self.object["post_video_thumbnail"]["locator"]):

                        self.screen.find_element_and_input(self.object["regular_post_title"]["by"],
                                                           self.object["regular_post_title"]["locator"], 5,
                                                           " (" + time.strftime('%d/%m/%Y %H:%M:%S') + ")")

                        self.screen.click_element_javascript(self.object["post_video_post_button"]["by"],
                                                             self.object["post_video_post_button"]["locator"])
                        assert True

                    else:
                        assert False, "Invalid Link"
                else:
                    assert False, "Tap Tab Buy Now Post was not successful"
            else:
                assert False, "Tab Post was not successful"

        except AssertionError as e:
            raise e

