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


class ZpmangaError(Exception):
    """A custom core Zpmanga exception"""

    def __init__(self, message=None):

        message = 'There has been an error' \
            if not message else message

        super(ZpmangaError, self).__init__(message)


class ZpmangaNotImplemented(ZpmangaError):
    """A custom exception for not yet implemented features."""

    def __init__(self, message=None):

        message = 'This feature is not implemented yet.' \
            if not message else message

        super(ZpmangaNotImplemented, self).__init__(message)


class ZpmangaAPIError(ZpmangaError):
    """A custom exception for API errors"""

    def __init__(self, message=None):
        if not message:
            message = 'Error with Http Response from Zpmanga API'
        else:
            message = 'Http response error from Zpmanga API. {0}'.format(message)

        super(ZpmangaAPIError, self).__init__(message)


class ZpmangaApiAuthError(ZpmangaAPIError):
    """A custom exception for API authentication errors"""
    pass


class ZpmangaMissingDependency(ZpmangaError):
    """A custom exception for missing dependencies."""
    pass


class ZpmangaWarning(Warning):
    """Base warning for Zpmanga."""


class ZpmangaUserWarning(UserWarning, ZpmangaWarning):
    """The primary warning class."""
    pass


class ZpmangaSkippedTestWarning(ZpmangaUserWarning):
    """A warning for when a test is skipped."""
    pass


class ZpmangaDeprecationWarning(ZpmangaUserWarning):
    """A warning for deprecated features."""
    pass
