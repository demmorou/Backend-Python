class HttpErrors:
    """Class to define HTTP Errors"""

    @staticmethod
    def error_400():
        """Define HTTP 400"""

        return {"status_code": 400, "body": {"error": "Bad Request"}}

    @staticmethod
    def error_422():
        """Define HTTP 422"""

        return {"status_code": 422, "body": {"error": "Unprocessable Entity"}}
