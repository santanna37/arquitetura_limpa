

class HttpRequest:
    def __init__(
        self,
        headers = None,
        body = None, 
        query_params = None,
        url = None, 
        ipv4 = None, 
        path_params = None
    ) -> None: 
        self.headers = headers
        self.body = body
        self.query_params = query_params
        self.url = url 
        self.ipv4 = ipv4
        self.path_params = path_params