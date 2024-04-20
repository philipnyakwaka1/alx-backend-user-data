#!/usr/bin/env python3
"""Obfuscates a log message
"""
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated
    """
    for field in fields:
        pattern = re.compile(r'({}=).+?({})'.format(re.escape(field),
                                                    re.escape(separator)))
        message = re.sub(pattern, r'\1{}{}'.format(redaction,
                                                   separator), message)
    return message
