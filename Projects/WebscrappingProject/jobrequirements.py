from userinfo import access_token, return_url, key, secret
from linkedin import linkedin

authentication = linkedin.LinkedInDeveloperAuthentication(
    key,
    secret,
    access_token,
    return_url,
    linkedin.PERMISSIONS.enums.values()
)
print(authentication.user_secret)
application = linkedin.LinkedInApplication(authentication)
print(application)