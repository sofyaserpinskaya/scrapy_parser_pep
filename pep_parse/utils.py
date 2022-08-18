from datetime import datetime


def uri_params(params, *_):
    params['time'] = datetime.now().replace(
        microsecond=0
    ).isoformat().replace(':', '-')
