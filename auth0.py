import os
import re
from flower.views.auth import OktaLoginHandler


class Auth0LoginHandler(OktaLoginHandler):
    @property
    def base_url(self):
        return "mclemon.eu.auth0.com"
        #return os.environ.get("FLOWER_OAUTH2_AUTH0_BASE_URL")

    @property
    def _OAUTH_AUTHORIZE_URL(self):
        return f"https://{self.base_url}/oauth/authorize"

    @property
    def _OAUTH_ACCESS_TOKEN_URL(self):
        return f"https://{self.base_url}/login/oauth/token"

    @property
    def _OAUTH_USER_INFO_URL(self):
        return f"https://{self.base_url}/userinfo"
