########################################################################################
# HTTP_Error Base Class
########################################################################################
class HttpError:
    def __init__(self, http_status_code, http_status_text, error_message):
        self.http_status_code = http_status_code
        self.http_status_text = http_status_text
        self.error_message = error_message

    def __str__(self):
        return f"{self.http_status_code} {self.http_status_text}: {self.error_message}"
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.http_status_code == other.http_status_code
    def __ne__(self, other):
        return self.http_status_code != other.http_status_code

    def __add__(self, other):
        if isinstance(other, HttpError):
            return self.__str__() + other.__str__()
        return self.__str__()
#########################################################################################
# HTTP_Error derived Classes for 4xx errors
#########################################################################################
class Http400Error(HttpError):
    def __init__(self, error_message):
        super().__init__(400, "Bad Request", error_message)
#########################################################################################
class Http401Error(HttpError):
    def __init__(self, error_message):
        super().__init__(401, "Unauthorized", error_message)
#########################################################################################
class Http403Error(HttpError):
    def __init__(self, error_message):
        super().__init__(403, "Forbidden", error_message)
#########################################################################################
class Http404Error(HttpError):
    def __init__(self, error_message):
        super().__init__(404, "Not Found", error_message)
#########################################################################################
class Http405Error(HttpError):
    def __init__(self, error_message):
        super().__init__(405, "Method Not Allowed", error_message)
#########################################################################################
class Http406Error(HttpError):
    def __init__(self, error_message):
        super().__init__(406, "Not Acceptable", error_message)
#########################################################################################
class Http407Error(HttpError):
    def __init__(self, error_message):
        super().__init__(407, "Proxy Authentication Required", error_message)
#########################################################################################
class Http408Error(HttpError):
    def __init__(self, error_message):
        super().__init__(408, "Request Timeout", error_message)
#########################################################################################
class Http409Error(HttpError):
    def __init__(self, error_message):
        super().__init__(409, "Conflict", error_message)
#########################################################################################
class Http413Error(HttpError):
    def __init__(self, error_message):
        super().__init__(413, "Payload Too Large", error_message)
#########################################################################################
class Http414Error(HttpError):
    def __init__(self, error_message):
        super().__init__(414, "URI Too Long", error_message)
#########################################################################################
class Http415Error(HttpError):
    def __init__(self, error_message):
        super().__init__(415, "Unsupported Media Type", error_message)
#########################################################################################
class Http422Error(HttpError):
    def __init__(self, error_message):
        super().__init__(422, "Unprocessable Entity", error_message)
#########################################################################################
class Http429Error(HttpError):
    def __init__(self, error_message):
        super().__init__(429, "Too Many Requests", error_message)
#########################################################################################
# HTTP_Error derived Classes for 5xx errors
#########################################################################################
class Http500Error(HttpError):
    def __init__(self, error_message):
        super().__init__(500, "Internal Server Error", error_message)
#########################################################################################
class Http501Error(HttpError):
    def __init__(self, error_message):
        super().__init__(501, "Not Implemented", error_message)
#########################################################################################
class Http502Error(HttpError):
    def __init__(self, error_message):
        super().__init__(502, "Bad Gateway", error_message)
#########################################################################################
class Http503Error(HttpError):
    def __init__(self, error_message):
        super().__init__(503, "Service Unavailable", error_message)
#########################################################################################
class Http504Error(HttpError):
    def __init__(self, error_message):
        super().__init__(504, "Gateway Timeout", error_message)
#########################################################################################
class Http505Error(HttpError):
    def __init__(self, error_message):
        super().__init__(505, "HTTP Version Not Supported", error_message)
#########################################################################################
class Http507Error(HttpError):
    def __init__(self, error_message):
        super().__init__(507, "Insufficient Storage", error_message)
#########################################################################################
class Http508Error(HttpError):
    def __init__(self, error_message):
        super().__init__(508, "Loop Detected", error_message)
#########################################################################################
class Http511Error(HttpError):
    def __init__(self, error_message):
        super().__init__(511, "Network Authentication Required", error_message)
#########################################################################################
class Http520Error(HttpError):
    def __init__(self, error_message):
        super().__init__(520, "Origin Is Unreachable", error_message)
##########################################################################################
class Http521Error(HttpError):
    def __init__(self, error_message):
        super().__init__(521, "Origin Is Unreachable", error_message)
##########################################################################################
class Http522Error(HttpError):
    def __init__(self, error_message):
        super().__init__(522, "Origin Is Unreachable", error_message)
##########################################################################################
class Http598Error(HttpError):
    def __init__(self, error_message):
        super().__init__(598, "Network Read Timeout Error", error_message)
#########################################################################################
class Http599Error(HttpError):
    def __init__(self, error_message):
        super().__init__(599, "Network Connect Timeout Error", error_message)
#########################################################################################
