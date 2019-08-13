# encoding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

from .utils import get_config, get_logger


NAME = 'zpmanga'


# Loads config
config = get_config(NAME)


# Inits the logging system. Only shell logging, and exception and warning catching.
# File logging can be started by calling log.start_file_logger(path).
log = get_logger(NAME)


__version__ = '1.0.0'


from .core import exceptions
from .elines import _elines as elines
from .spec_tools import _spec_tools as spec_tools
