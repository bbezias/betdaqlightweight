from betdaqlightweight.utils import check_status_code, to_dict
from betdaqlightweight.exceptions import APIError


class BaseEndpoint:

    def __init__(self, parent):
        """
        :param parent: API client.
        """
        self.client = parent

    def run(self, fct_name, param_name, **kwargs):
        try:
            method = getattr(self.client.service, fct_name)
            params = self.create_params(param_name, **kwargs)
            resp = method(params)
        except Exception as e:
            raise APIError(None, fct_name, params=kwargs, exception=e)

        return self.process_response(resp)

    def create_params(self, param_name, **kwargs):
        r = self.client.factory.create(param_name)
        for k, i in kwargs.items():
            setattr(r, k, i)
        return r

    def process_response(self, response):
        resp = to_dict(response, self.client)
        check_status_code(resp)
        return resp
