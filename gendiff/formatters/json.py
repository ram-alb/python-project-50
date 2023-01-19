import json


def json_format(diff):
    json_str = json.dumps(diff, separators=(',', ':'))
    json_str = json_str.replace('"true"', 'true')
    json_str = json_str.replace('"false"', 'false')
    json_str = json_str.replace('"null"', 'null')
    return json_str
