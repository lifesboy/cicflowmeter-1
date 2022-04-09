import uuid
from itertools import islice, zip_longest
from datetime import datetime
from .util.logger import log

import hashlib
import numpy


def marked_done(file: str) -> bool:
    f = open(file, 'w')
    f.write(str(datetime.now()))
    f.close()
    return True


def get_output_file_of_batch(files: []) -> str:
    return '%s.csv' % hashlib.sha256('_'.join(files).encode('utf-8')).hexdigest()


def get_marked_done_file_name(file: str) -> str:
    return '.%s.done.cic' % hashlib.sha256(file.encode('utf-8')).hexdigest()


def grouper(iterable, n, max_groups=0, fillvalue=None):
    """Collect data into fixed-length chunks or blocks"""

    if max_groups > 0:
        iterable = islice(iterable, max_groups * n)

    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def random_string():
    return uuid.uuid4().hex[:6].upper().replace("0", "X").replace("O", "Y")


def get_statistics(alist: list):
    """Get summary statistics of a list"""
    iat = dict()
    try:
        if len(alist) > 1:
            iat["total"] = sum(alist)
            iat["max"] = max(alist)
            iat["min"] = min(alist)
            alist_float = list(map(float, alist))
            iat["mean"] = numpy.mean(alist_float)
            iat["std"] = numpy.sqrt(numpy.var(alist_float))
        else:
            iat["total"] = 0
            iat["max"] = 0
            iat["min"] = 0
            iat["mean"] = 0
            iat["std"] = 0
    except Exception as e:
        log.error('statistics %s error: %s', alist, e)
        raise e

    return iat
