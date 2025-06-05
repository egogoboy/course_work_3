from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "0eaiB/cyapHswSFl5fGES1Wi6W8tdNRwH2mOuoybMhA"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
