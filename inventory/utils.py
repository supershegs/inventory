from typing import Optional,Any

from rest_framework.response import Response



class ApiResponse(Response):
    def __init__(
        self,
        msg: str,
        data: Optional[Any] = None,
        errors: Optional[Any] = None,
        status: int = 200,
    ):
        resp = {
            "status": status in range(200, 300),
            "message": msg,
            "data": data,
            "errors": errors,
        }
        super().__init__(data=resp, status=status)


class SuccessApiResponse(ApiResponse):
    def __init__(self, msg, data=None, status=None):
        super(SuccessApiResponse, self).__init__(msg, data, status=status)


class FailureApiResponse(ApiResponse):
    def __init__(self, msg, errors=None, status=None):
        super(FailureApiResponse, self).__init__(msg, errors=errors, status=status)


class ServerErrorApiResponse(ApiResponse):
    def __init__(self):
        super(ServerErrorApiResponse, self).__init__("Server error", status=500)
