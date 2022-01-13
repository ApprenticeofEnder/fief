import secrets
from typing import Literal

from jwcrypto import jwk


def generate_jwk(kid: str, use: Literal["sig", "enc"]) -> jwk.JWK:
    return jwk.JWK.generate(kty="RSA", size=2048, use=use, kid=kid)


def load_jwk(json: str) -> jwk.JWK:
    return jwk.JWK.from_json(json)


def generate_account_signature_jwk() -> str:
    key = generate_jwk(secrets.token_urlsafe(), "sig")
    return key.export()
