def replace_domain(email, domain, old_domain="kaaj.com"):
    """
    This function takes email, domain and old domain
    as 3 input. If email contains the old domain then
    it changes it to the new domain. Then it returns the
    email with a comment regarding wheater the email has been
    changed or not.
    """
    new_email = ""
    index = -1
    for char in range(len(email)):
        if email[char] == "@":
            index = char
            break

    if index == -1:
        return "Incorrect E-Mail Adress!"

    new_email = email[: index + 1]

    if old_domain in email:
        new_email += domain
        comment = "Changed"
    else:
        new_email += domain
        comment = "Unchanged"

    return f"{comment}: {new_email}"


print(replace_domain("alice@kaaj.com", "sheba.xyz", "kaaj.com"))
print(replace_domain("bob@sheba.xyz", "sheba.xyz"))
print(replace_domain("bobsheba.xyz", "sheba.xyz"))

# print(replace_domain.__doc__)   # Acess Docstring.
