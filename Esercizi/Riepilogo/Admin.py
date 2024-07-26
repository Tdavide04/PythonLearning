def check_access(username: str, password: ..., is_active: bool) -> str:
    if username == "admin" and password == "12345" and is_active == True:
        return "Accesso consentito"
    else: 
        return "Accesso negato"
    
print(8/0)