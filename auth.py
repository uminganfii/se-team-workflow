def login(username, password):
    print("Refactored auth function returning dictionary response")
    if username == "admin" and password == "1234":
        return {"status": 200, "token": "jwt-token-xyz"}
    return {"status": 401, "error": "Unauthorized"}