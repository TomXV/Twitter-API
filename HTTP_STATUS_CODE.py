def HTTP_STATUS_CODE(code):
  if code == 200:
  	print('OK\n')
  	print('Success')
  elif code == 201:
      print('OK\n')
      print('Created')
  elif code == 304:
    print('Not Modified\n')
    print('There was no new data to return.')
  elif code == 400:
    print('Bad Request;\n')
    print('The request was invalid or cannot be otherwise served. An accompanying error message will explain further. In API v1.1, requests without authentication are considered invalid and will yield this response.')
  elif code == 401:
    print('Unauthorized\n')
    print('Authentication credentials were missing or incorrect. Also returned in other circumstances, for example all calls to API v1 endpoints now return 401 (use API v1.1 instead).')
  elif code == 403:
    print('Forbidden\n')
    print('The request is understood, but it has been refused or access is not allowed. An accompanying error message will explain why. This code is used when requests are being denied due to update limits.')
  elif code == 404:
    print('Not Found\n')
    print('The URI requested is invalid or the resource requested, such as a user, does not exists. Also returned when the requested format is not supported by the requested method.')
  elif code == 406:
    print('Not Acceptable\n')
    print('Returned by the Search API when an invalid format is specified in the request.')
  elif code == 410:
    print('Gone\n')
    print('This resource is gone. Used to indicate that an API endpoint has been turned off. For example: “The Twitter REST API v1 will soon stop functioning. Please migrate to API v1.1.”')
  elif code == 420:
    print('Enhance Your Calm\n')
    print('Returned by the version 1 Search and Trends APIs when you are being rate limited.')
  elif code == 422:
    print('Unprocessable Entity\n')
    print('Returned when an image uploaded to POST account / update_profile_banner is unable to be processed.')
  elif code == 429:
    print('Too Many Requests\n')
    print('Returned in API v1.1 when a request cannot be served due to the application’s rate limit having been exhausted for the resource. See Rate Limiting in API v1.1. ')
  elif code == 500:
    print('Internal Server Error\n')
    print('Something is broken. Please post to the developer forums so the Twitter team can investigate.')
  elif code == 502:
    print('Bad Gateway\n')
    print('Twitter is down or being upgraded.')
  elif code == 503:
    print('Service Unavailable\n')
    print('The Twitter servers are up, but overloaded with requests. Try again later.')
  elif code == 504:
    print('Gateway timeout\n')
    print('The Twitter servers are up, but the request couldn’t be serviced due to some failure within our stack. Try again later.')
  else:
    print('Error code is not found')
