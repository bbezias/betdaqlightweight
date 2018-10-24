
class BetdaqError(Exception):
    """Base class for Betdaq Errors"""
    pass


class APIError(BetdaqError):

    def __init__(self, response, method=None, params=None, exception=None):
        if response:
            error_data = response.get('error')
            message = '%s \nParams: %s \nException: %s \nError: %s \nFull Response: %s' % (
                method, params, exception, error_data, response
            )
        else:
            message = '%s \nParams: %s \nException: %s' % (
                method, params, exception
            )
        super(APIError, self).__init__(message)


class StatusCodeError(BetdaqError):
    def __init__(self, status_code, description):
        message = 'Status code error: {} - {}'.format(status_code, description)
        self.status_code = status_code
        super(BetdaqError, self).__init__(message)
