def validate_email(email: str) -> bool:
	"""Return whether email has an @ followed by a dot."""
	if len(email) > 254:
		return False

	at_index = email.find("@")
	return at_index != -1 and email.find(".", at_index + 1) != -1

#It accepts an @ followed by a dot, rejects inputs over 254 characters, and intentionally applies no RFC 5322 rules. Boundary checks and diagnostics pass.