import os

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"

#allows to access environment that ur running on and u can grab things from it
current_env = os.environ.get("ENV_NAME", DEVELOPMENT)

if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
# checking against code_space AND local
elif current_env in [CODE_SPACE, LOCAL]:
    print("Codespace or local environment")
else:
    print("Unknown environment")

#type export *variable name*='jfkdjfkl' in the terminal to change the variable locally