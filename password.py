import os
from hashlib import pbkdf2_hmac
from typing import Tuple

def get_digest_and_salt(password: str) -> Tuple[bytes, bytes]:
	salt: bytes = os.urandom(3)
	digest: bytes = pbkdf2_hmac(
		'sha256', 
		bytes(password, 'utf-8'), 
		salt, 
		500_000
	)
	return digest, salt


def is_password(attempt: str, digest: bytes, salt: bytes) -> bool:
	return digest == pbkdf2_hmac(
		'sha256', 
		bytes(attempt, 'utf-8'), 
		salt,
		500_000
	)

password = os.environ.get('PASSWORD')
digest, salt = get_digest_and_salt(password)
def validate(attempt: str) -> bool:
  return is_password(attempt, digest, salt)
