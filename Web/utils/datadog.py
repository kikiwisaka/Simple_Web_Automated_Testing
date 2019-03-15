from datadog import initialize, ThreadStats
from ..utils import config

class DataDogHelper():
    def __init__(self):
        pass

    @staticmethod
    def send_metric(metric_name: str, data_value: float, **kwargs):
        tags = ['metric_submission:threadstats']
        if kwargs is not None:
            for key, value in kwargs.items():
                if 'tag' in key:
                    tags.append('{0}:{1}'.format(key[3:], value))

        api_key = config.Get().datadog_config()['api_key']
        app_key = config.Get().datadog_config()['app_key']
        options = {'api_key': '' + api_key + '',
                   'app_key': '' + app_key + ''}

        initialize(**options)

        stats = ThreadStats()
        stats.start()
        try:
            stats.gauge(metric_name,
                        value=data_value,
                        tags=tags)
            return True
        except Exception as e:
            print(e)
            return False
