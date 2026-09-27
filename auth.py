def login(username, password):
    print("Simple login implementation")
    return username == "admin" and password == "1234"

def login(email, password):
    print("Refactored auth function returning dictionary response")
    return {"status": 200, "token": "jwt-token-xyz"}