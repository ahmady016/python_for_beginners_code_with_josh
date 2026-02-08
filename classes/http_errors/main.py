# build a http error classes using inheritance to handle various http errors:
# create the base http error class that contains
# the http status code, http status text and the error message
# for each http error create a http error classes that inherits from the base http error
# and each one assigns a specific http status code, http status text and error message
#########################################################################################
# test the http error classes with different http errors
# by creating each http error object and give it an example error message
# you can use random modules for random error messages and codes
#########################################################################################
from random import randint, choices
from http_error import *
#########################################################################################
ERROR_MAP = {
    400: (Http400Error, "Opps, you entered an invalid request"),
    401: (Http401Error, "Opps, you are not authorized to access this page"),
    403: (Http403Error, "Opps, you do not have permission to access this page"),
    404: (Http404Error, "Opps, the page you are looking for something not found"),
    405: (Http405Error, "Opps, the request method is not allowed"),
    406: (Http406Error, "Opps, the request was not acceptable"),
    407: (Http407Error, "Opps, you must authenticate first"),
    408: (Http408Error, "Opps, the request has timed out"),
    409: (Http409Error, "Opps, the request could not be completed due to a conflict"),
    422: (Http422Error, "Opps, the request was unprocessable"),
    429: (Http429Error, "Opps, you have exceeded the rate limit"),
    500: (Http500Error, "Opps, the server has encountered an error"),
    502: (Http502Error, "Opps, the server is acting as a proxy and could not handle the request"),
    503: (Http503Error, "Opps, the server is temporarily unavailable"),
    504: (Http504Error, "Opps, the server is acting as a gateway and the upstream server is timing out"),
    505: (Http505Error, "Opps, the server does not support the HTTP protocol version used in the request"),
    507: (Http507Error, "Opps, you may used insufficient storage"),
    508: (Http508Error, "Opps, you may caused an infinite loop"),
    511: (Http511Error, "Opps, you must authenticate first"),
    520: (Http520Error, "Opps, the server is acting as a web server and could not handle the request"),
    521: (Http521Error, "Opps, the server is acting as a web server and could not handle the request"),
    522: (Http522Error, "Opps, the server is acting as a web server and could not handle the request"),
    598: (Http598Error, "Opps, you may cased a network connect timeout error"),
    599: (Http599Error, "Opps, you may cased a network connect timeout error"),
}
#########################################################################################
print("###############################################")
print("HTTP Errors Mapper Program Started Successfully")
print("###############################################")
#########################################################################################
codes = list(set(choices(list(ERROR_MAP.keys()), k=randint(5, 10))))
for status_code in codes:
    ErrorClass, error_message = ERROR_MAP.get(status_code)
    print(ErrorClass(error_message))
#########################################################################################
print("#################################################")
print("HTTP Errors Mapper Program Completed Successfully")
print("#################################################")
#########################################################################################
