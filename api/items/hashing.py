from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"])
def hash_maker(password):
    return pwd_cxt.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_cxt.verify(plain_password, hashed_password)