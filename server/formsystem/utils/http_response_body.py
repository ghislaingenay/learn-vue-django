from rest_framework.response import Response

def success_response(message, data=None, status_code=200):
    """Standard success response format"""
    response_data = {
        "isSuccess": True,
        "message": message,
    }
    if data:
        response_data["data"] = data
    return Response(response_data, status=status_code)

def error_response(message, errors=None, status_code=400):
    """Standard error response format"""
    response_data = {
        "isSuccess": False,
        "message": message,
    }
    if errors:
        response_data["errors"] = errors
    return Response(response_data, status=status_code)