# -*- coding: utf-8 -*-

import re

from jinja2 import nodes
from jinja2.ext import Extension

import re

def _space_numbers(match):
    return f'{match.group(1)} {match.group(2)} {match.group(3)}'

def _add_word_boundaries_to_numbers(string):
    pattern = re.compile(r'([a-zA-Z])(\d+)([a-zA-Z]?)')
    return pattern.sub(_space_numbers, string)

def _to_camel_init_case(string, init_case):
    string = _add_word_boundaries_to_numbers(string)
    string = string.strip(" ")
    n = ""
    cap_next = init_case
    for v in string:
        if (v >= 'A' and v <= 'Z') or (v >= '0' and v <= '9'):
            n += v
        if v >= 'a' and v <= 'z':
            if cap_next:
                n += v.upper()
            else:
                n += v
        if v == '_' or v == ' ' or v == '-':
            cap_next = True
        else:
            cap_next = False
    return n

def to_camel(string):
    return _to_camel_init_case(string, True)


class ToCamelCaseExtension(Extension):
    """An extension for converting string case to CamelCase in jinja2 templates."""

    def __init__(self, environment):
        super(ToCamelCaseExtension, self).__init__(environment)
        environment.filters['to_camel'] = to_camel
