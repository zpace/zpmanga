# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2017-12-05 12:01:21
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2017-12-05 12:19:32

from __future__ import print_function, division, absolute_import


class ZPMaNGAError(Exception):
    """A custom core ZPMaNGA exception"""

    def __init__(self, message=None):

        message = 'There has been an error' \
            if not message else message

        super(ZPMaNGAError, self).__init__(message)


class ZPMaNGANotImplemented(ZPMaNGAError):
    """A custom exception for not yet implemented features."""

    def __init__(self, message=None):

        message = 'This feature is not implemented yet.' \
            if not message else message

        super(ZPMaNGANotImplemented, self).__init__(message)


class ZPMaNGAAPIError(ZPMaNGAError):
    """A custom exception for API errors"""

    def __init__(self, message=None):
        if not message:
            message = 'Error with Http Response from ZPMaNGA API'
        else:
            message = 'Http response error from ZPMaNGA API. {0}'.format(message)

        super(ZPMaNGAAPIError, self).__init__(message)


class ZPMaNGAApiAuthError(ZPMaNGAAPIError):
    """A custom exception for API authentication errors"""
    pass


class ZPMaNGAMissingDependency(ZPMaNGAError):
    """A custom exception for missing dependencies."""
    pass


class ZPMaNGAWarning(Warning):
    """Base warning for ZPMaNGA."""


class ZPMaNGAUserWarning(UserWarning, ZPMaNGAWarning):
    """The primary warning class."""
    pass


class ZPMaNGASkippedTestWarning(ZPMaNGAUserWarning):
    """A warning for when a test is skipped."""
    pass


class ZPMaNGADeprecationWarning(ZPMaNGAUserWarning):
    """A warning for deprecated features."""
    pass
