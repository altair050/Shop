from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.settings import api_settings


class AppRefreshToken(RefreshToken):
    token_type = 'app_refresh'
    lifetime = api_settings.REFRESH_TOKEN_LIFETIME

    @property
    def access_token(self):
        access = AppAccessToken()

        access.set_exp(from_time=self.current_time)

        no_copy = self.no_copy_claims
        for claim, value in self.payload.items():
            if claim in no_copy:
                continue
            access[claim] = value

        return access


class AppAccessToken(AccessToken):
    token_type = 'app_access'
    lifetime = api_settings.ACCESS_TOKEN_LIFETIME
