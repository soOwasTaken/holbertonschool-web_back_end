#!/usr/bin/env python3
"""Module BasicAuth"""
from api.v1.auth.auth import Auth
from typing import TypeVar, Tuple, Optional
from models.user import User
import base64


class BasicAuth(Auth):
    """BasicAuth class inherits from Auth"""

    def extract_base64_authorization_header(
        self, authorization_header: Optional[str]
    ) -> Optional[str]:
        """Returns Base64 part of Authorization header"""
        if not (isinstance(authorization_header, str) and
                authorization_header.startswith('Basic ')):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: Optional[str]
    ) -> Optional[str]:
        """Decodes and returns value of a Base64 string"""
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: Optional[str]
    ) -> Tuple[Optional[str], Optional[str]]:
        """Returns user email and password from decoded value"""
        if not (isinstance(decoded_base64_authorization_header, str) and
                ':' in decoded_base64_authorization_header):
            return None, None
        user_email, user_password = decoded_base64_authorization_header.split(
            ':', 1)
        return user_email, user_password

    def user_object_from_credentials(
        self, user_email: Optional[str], user_pwd: Optional[str]
    ) -> Optional[TypeVar('User')]:
        """Returns User instance based on email and password."""
        if not (isinstance(user_email, str) and isinstance(user_pwd, str)):
            return None

        users = User.search({"email": user_email})
        if not users:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the User instance for a request"""
        authorization_header = self.authorization_header(request)
        base64_auth_header = self.extract_base64_authorization_header(
            authorization_header)
        decoded_base64 = self.decode_base64_authorization_header(
            base64_auth_header)
        user_email, user_pwd = self.extract_user_credentials(decoded_base64)
        return self.user_object_from_credentials(user_email, user_pwd)
