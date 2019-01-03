# use regex to parse Apache logs
# https://stackoverflow.com/questions/12544510/parsing-apache-log-files

import re
print("simple split into tuple\n")
line = '172.16.0.3 - - [25/Sep/2002:14:04:19 +0200] "GET / HTTP/1.1" 401 - "" "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020827"'
regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'
print(re.match(regex, line).groups()) # tuple

print("\nnext will use an Apache log parser module\n")
# or use https://github.com/rory/apache-log-parser

import apache_log_parser
line_parser = apache_log_parser.make_parser("%h <<%P>> %t %Dus \"%r\" %>s %b  \"%{Referer}i\" \"%{User-Agent}i\" %l %u")
log_line_data = line_parser('127.0.0.1 <<6113>> [16/Aug/2013:15:45:34 +0000] 1966093us "GET / HTTP/1.1" 200 3478  "https://example.com/" "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18)" - -')
print(log_line_data)


'''
outputs:
(base) D:\Go-workspace\walter\coding\python>python parse_apache_logs.py
simple split into tuple

('172.16.0.3', '25/Sep/2002:14:04:19 +0200', 'GET / HTTP/1.1', '401', '', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020827')

next will use an Apache log parser module

{'remote_host': '127.0.0.1', 'pid': '6113', 'time_received': '[16/Aug/2013:15:45:34 +0000]', 'time_received_datetimeobj': datetime.datetime(2013, 8, 16, 15, 45, 34), 'time_received_isoformat': '2013-08-16T15:45:34', 'time_received_tz_datetimeobj':
datetime.datetime(2013, 8, 16, 15, 45, 34, tzinfo='0000'), 'time_received_tz_isoformat': '2013-08-16T15:45:34+00:00', 'time_received_utc_datetimeobj': datetime.datetime(2013, 8, 16, 15, 45, 34, tzinfo='0000'), 'time_received_utc_isoformat': '2013-08-16T15:45:34+00:00', 'time_us': '1966093', 'request_first_line': 'GET / HTTP/1.1', 'request_method': 'GET', 'request_url':
'/', 'request_http_ver': '1.1', 'request_url_scheme': '', 'request_url_netloc': '', 'request_url_path': '/', 'request_url_query': '', 'request_url_fragment': '', 'request_url_username': None, 'request_url_password': None, 'request_url_hostname': None, 'request_url_port': None, 'request_url_query_dict': {}, 'request_url_query_list': [], 'request_url_query_simple_dict': {}, 'status': '200', 'response_bytes_clf': '3478', 'request_header_referer': 'https://example.com/', 'request_header_user_agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18)', 'request_header_user_agent__browser__family': 'Other', 'request_header_user_agent__browser__version_string': '', 'request_header_user_agent__os__family': 'Linux', 'request_header_user_agent__os__version_string': '', 'request_header_user_agent__is_mobile': False, 'remote_logname': '-', 'remote_user': ''}
'''
