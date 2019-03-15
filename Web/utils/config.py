import json
import os
from pathlib import Path


class Get(object):
    @staticmethod
    def data_by_path(json_path: str):
        data = json.load(open(json_path))
        return data

    @staticmethod
    def base_config():
        d = Path().resolve()
        config_data = os.path.join(d, 'Web/config.json')
        return json.load(open(config_data))

    @staticmethod
    def chrome_driver():
        return Get.base_config()['configuration']['chromeDriver']

    @staticmethod
    def bbm_cmc_url():
        return Get.base_config()['configuration']['cmc_url']

    @staticmethod
    def bbm_cmc_email():
        return Get.base_config()['configuration']['cmc_email_address']

    @staticmethod
    def bbm_cmc_password():
        return Get.base_config()['configuration']['cmc_password']


    @staticmethod
    def parent_path():
        return Path().resolve()

    @staticmethod
    def discover(obj):
        return obj['discover']

    @staticmethod
    def services():
        d = Get.parent_path()
        config_data = os.path.join(d, 'Web/services_config/services.json')
        return json.load(open(config_data))

    @staticmethod
    def bbm_connect():
        d = Get.parent_path()
        config_data = os.path.join(d, 'Web/services_config/bbm_connect.json')
        return json.load(open(config_data))

    @staticmethod
    def cmc_repository():
        return Get.object_repository()['cmc']

    @staticmethod
    def object_repository():
        d = Get.parent_path()
        config_data = os.path.join(d, 'Web/services_config/repository_connect.json')
        return json.load(open(config_data))

    @staticmethod
    def datadog_config():
        d = Get.parent_path()
        config_data = os.path.join(d, 'Web/utils/env.json')
        return json.load(open(config_data))