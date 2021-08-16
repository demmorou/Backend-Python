from typing import Dict


class HttpRequest:
    """Class to http requests representation"""

    def __init__(self, header: Dict = None, body: Dict = None, query: Dict = None):
        self.header = header
        self.body = body
        self.query = query

    def __repr__(self) -> str:
        return (
            f"HttpRequest (header={self.header}, body={self.body}, query={self.query}"
        )


class HttpResponse:
    """Class to http response representation"""

    def __init__(self, status_code: int, body: any):
        self.status_code = status_code
        self.body = body

    def __repr__(self) -> str:
        return f"HttpResponse (status_code={self.status_code}, body={self.body}"
