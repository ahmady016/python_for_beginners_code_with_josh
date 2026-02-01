# build a function to get http status message from http status code:
# input the http status code
# and match the http status code with the http status message
# return the http status message
# test the function with different http status codes
################################################################
def get_http_status_message(http_status_code):
    match http_status_code:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 202:
            return "Accepted"
        case 204:
            return "No Content"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 405:
            return "Method Not Allowed"
        case 409:
            return "Conflict"
        case 500:
            return "Internal Server Error"
        case 501:
            return "Not Implemented"
        case 503:
            return "Service Unavailable"
        case 504:
            return "Gateway Timeout"
        case 505:
            return "HTTP Version Not Supported"
        case _:
            return "Unknown Status Code"
##############################################################
print("##############################################################")
print("Program to get http status message from http status code")
print("##############################################################")
##############################################################
try:
    http_status_code = int(input("Enter the http status code: "))
    print("----------------------------------------------------")
    http_status_message = get_http_status_message(http_status_code)
    print(f"http error: {http_status_code} {http_status_message}")
    print("----------------------------------------------------")
except ValueError as error:
    print(error)
    print("you must enter a valid number")
finally:
    print("##############################################")
    print("Program Completed Successfully")
    print("##############################################")
##############################################################
