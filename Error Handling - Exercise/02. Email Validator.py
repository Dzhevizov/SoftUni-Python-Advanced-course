from errors import *

while True:
    email = input()

    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split("@")) > 2:
        raise MustContainAtSymbolError("Email must contain only one @ sign")

    name, domain_name = email.split("@")

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    valid_domains = ["com", "bg", "net", "org"]

    if "." not in domain_name:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    domain_name = domain_name.split(".")

    dom_name = ".".join(domain_name[:-1])
    domain = domain_name[-1]

    if dom_name == "" or domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
