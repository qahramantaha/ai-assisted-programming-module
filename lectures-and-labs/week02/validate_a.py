import re


def validate_email(email: str) -> bool:
	"""Return whether email has a conventional email address shape."""
	pattern = r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+$"
	return re.fullmatch(pattern, email) is not None

#Verified valid, malformed, and spaced addresses. Pylance reports no errors.