#!/usr/bin/env python3

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth method
        Determines if a route requires authentication or not
        Args:
            path (str): the path of the request
            excluded_paths (List[str]): a list of paths that do not require authentication
        Returns:
            bool: True if authentication is required, False otherwise
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        for excluded in excluded_paths:
            if excluded[-1] == '*':
                if path.startswith(excluded[:-1]):
                    return False
            elif path == excluded:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header method
        Returns the value of the Authorization header in a request
        Args:
            request (flask.Request): the request object
        Returns:
            str: the value of the Authorization header, or None if it is not present
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user method
        Returns the current user making the request
        Args:
            request (flask.Request): the request object
        Returns:
            TypeVar('User'): the current user, or None if there is no user
        """
        return None
