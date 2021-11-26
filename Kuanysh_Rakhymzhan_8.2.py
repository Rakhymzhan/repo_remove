import re

with open('data/nginx_logs.txt', 'r', encoding='utf-8') as f:
    data = f.read().splitlines()
    pattern = re.compile(r'(?P<remote_addr>\d+\.\d+\.\d+\.\d+).+'
                         r'\[(?P<request_datetime>[\d\w/: \+]+)\] "'
                         r'(?P<request_type>[A-Z]+) '
                         r'(?P<requested_resource>/\w+/\w+) \w+/\d\.\d" '
                         r'(?P<response_code>\d+) '
                         r'(?P<response_size>\d+)')
    for line in data:
        result = pattern.findall(line)
        if result:
            print(tuple(result)[0])
