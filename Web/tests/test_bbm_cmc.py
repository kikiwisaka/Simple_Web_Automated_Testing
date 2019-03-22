import pytest

from ..modules.cmc import bbm_cmc
from ..utils import config
from ..utils import custom_logger
from ..utils import helper

logger_helper = custom_logger.LoggerHelper()
json_logger = logger_helper.json_logger()


class TestBBMConnect:

    @pytest.fixture()
    def test_login(self):
        global bbm_driver
        bbm_driver = helper.open_browser_connect(config.Get.bbm_cmc_url())
        bbm_cmc(bbm_driver).login()
        yield
        bbm_driver.close()

    def test_chat_bot_broadcast(self, test_login):
        try:
            json_logger.warning("Test cases: {0}]".format("test_chat_bot_broadcast"))
            bbm_cmc(bbm_driver).navigate_to_channel_detail_page()
            bbm_cmc(bbm_driver).navigate_to_chat_bot()
            bbm_cmc(bbm_driver).send_chat_bot_broadcast()
            json_logger.debug("Test case {0} passed".format("test_chat_bot_broadcast"))
        except AssertionError as e:
            json_logger.error("Test case {0} failed".format("test_chat_bot_broadcast"))
            raise e

    # def test_chat_bot_video_broadcast(self, test_login):
    #     try:
    #         bbm_cmc(bbm_driver).navigate_to_channel_detail_page()
    #         bbm_cmc(bbm_driver).navigate_to_chat_bot()
    #         bbm_cmc(bbm_driver).send_chat_bot_video_broadcast()
    #         helper.send_test_status(True, "test_chat_bot_video_broadcast")
    #
    #     except AssertionError as e:
    #         helper.send_test_status(False, "test_chat_bot_video_broadcast")
    #         raise e
    #
    # def test_regular_post(self, test_login):
    #     try:
    #         bbm_cmc(bbm_driver).navigate_to_channel_detail_page()
    #         bbm_cmc(bbm_driver).send_channel_regular_post()
    #         helper.send_test_status(True, "test_regular_post")
    #
    #     except AssertionError as e:
    #         helper.send_test_status(False, "test_regular_post")
    #         raise e
    #
    # def test_buy_now_post(self, test_login):
    #     try:
    #         bbm_cmc(bbm_driver).navigate_to_channel_detail_page()
    #         bbm_cmc(bbm_driver).send_channel_buy_now_post()
    #         helper.send_test_status(True, "test_buy_now_post")
    #
    #     except AssertionError as e:
    #         helper.send_test_status(False, "test_buy_now_post")
    #         raise e
    #
    # def test_video_post(self, test_login):
    #     try:
    #         bbm_cmc(bbm_driver).navigate_to_channel_detail_page()
    #         bbm_cmc(bbm_driver).send_video_post()
    #         helper.send_test_status(True, "test_video_post")
    #
    #     except AssertionError as e:
    #         helper.send_test_status(False, "test_video_post")
    #         raise e