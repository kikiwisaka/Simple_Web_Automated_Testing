from ..utils import helper
from ..utils.datadog import DataDogHelper
from ..utils.custom_logger import LoggerHelper

datadog_helper = DataDogHelper()
#logger_helper = helper.LoggerHelper()
custom_logger = LoggerHelper().json_logger()


class MetricHelper(object):
    @staticmethod
    def send_metric(metric_name: str, val: float, function_name: str):
        if val == 0.0:
            custom_logger.debug('Send data to datadog about successfully {0}'.format(metric_name))
        elif val == 1.0:
            custom_logger.critical('Send to datadog about failure {0}'.format(metric_name))
        else:
            custom_logger.debug('Send data to datadog {0} {1}'.format(metric_name, val))
        datadog_helper.send_metric(metric_name, val, tagservice=function_name)

    @staticmethod
    def send_metric_functions(metric_name: str, val: float, function_name: str):
        if val == 0.0:
            custom_logger.debug('Send data to datadog about successfully {0}'.format(metric_name))
        elif val == 1.0:
            custom_logger.critical('Send to datadog about failure {0}'.format(metric_name))
        else:
            custom_logger.debug('Send data to datadog {0} {1}'.format(metric_name, val))
        datadog_helper.send_metric(metric_name, val, tagservice=function_name)
