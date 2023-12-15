Very stripped down and simplified app to explore how to specify a custom `--auth_provider` outside the Flower codebase. Requires Redis running on `localhost:6379`.

Set up a venv and `pip install -r requirements.txt`. The goal is to find the appropriate value to supply to `--auth_provider` so that the `Auth0LoginHandler` class in `auth0.py` module is used and we get redirected to Auth0:

    celery -A tasks flower --loglevel=INFO --pool=solo --auth_provider="Auth0LoginHandler" --auth=".*@gmail.com" --oauth2_key="97UAeebqVse1xHRe0rjCZqECK5hcpuEB" --oauth2_secret="client-secret-not-important" --oauth2_redirect_uri="http://localhost:5555/login"

I've tried:
- `--auth_provider="auth0.Auth0LoginProvider"`
- `--auth_provider="Auth0LoginProvider"`

But when I open localhost:5555 I get a 500 error, and the app prints a stack trace with `ModuleNotFoundError: No module named 'Auth0LoginHandler'`

Note that I've not supplied the client secret so when the app "works" we'll get redirected to Auth0 but we'll be presented with an error page on their side. That is fine, the main thing is ensuring the provider gets picked up by Flower.