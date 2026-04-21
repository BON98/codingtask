def is_valid_email(email):
    # Handle null or empty input
    if email is None or email == "":
        return False
    # No spaces allowed
    if " " in email:
        return False
    # Must contain '@'
    if "@" not in email:
        return False
    # Split into local and domain parts
    parts = email.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    # Ensure both parts exist
    if not local or not domain:
        return False
    # Domain must contain a dot (e.g., .com)
    if "." not in domain:
        return False
    # Domain should not start or end with a dot
    if domain.startswith(".") or domain.endswith("."):
        return False
    return True