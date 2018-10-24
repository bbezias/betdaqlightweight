from betdaqlightweight.exceptions import StatusCodeError
from dateutil.parser import parse
from datetime import datetime
import pytz
from suds.sudsobject import Object as SudObject


def check_status_code(response):
    """
    Checks response.status_code is in codes.

    :param requests.request response: Requests response
    :raises: StatusCodeError if code invalid
    """

    if response['ReturnStatus']['Code'] != 0:
        raise StatusCodeError(response['ReturnStatus']['Code'], response['ReturnStatus']['Description'])


def parse_time_str(time_str):
    return parse(time_str)


def make_tz_naive(date):
    if isinstance(date, str):
        try:
            date = parse_time_str(date).strftime('%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            pass
    if isinstance(date, datetime):
        date = date.astimezone(pytz.UTC).replace(tzinfo=None).strftime('%Y-%m-%d %H:%M:%S.%f')
    return date


def to_dict(obj, client):
    if isinstance(obj, SudObject):
        temp = client.dict(obj)
    else:
        temp = obj

    if isinstance(temp, dict):
        response = dict()
        for k, v in temp.items():
            key = k[1:] if k[0:1] == '_' else k
            if isinstance(v, list):
                val = [to_dict(i, client) for i in v]
            elif isinstance(v, SudObject) or isinstance(v, dict):
                val = to_dict(v, client)
            elif isinstance(v, datetime) and v.tzinfo is not None:
                # Make all the dates naive and UTC
                val = v.astimezone(pytz.utc).replace(tzinfo=None)
            else:
                val = v
            response[key] = val
    else:
        response = temp
    return response
