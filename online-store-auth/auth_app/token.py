from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.settings import api_settings


class ThirdPartyAppRefreshToken(RefreshToken):
    token_type = 'oauth2_refresh'
    lifetime = api_settings.REFRESH_TOKEN_LIFETIME

    @property
    def access_token(self):
        access = ThirdPartyAppAccessToken()

        access.set_exp(from_time=self.current_time)

        no_copy = self.no_copy_claims
        for claim, value in self.payload.items():
            if claim in no_copy:
                continue
            access[claim] = value

        return access


class ThirdPartyAppAccessToken(AccessToken):
    token_type = 'oauth2_access'
    lifetime = api_settings.ACCESS_TOKEN_LIFETIME
