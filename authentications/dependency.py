from jose import jwt
from jose.exceptions import JOSEError
from fastapi import HTTPException
from database.connection import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


from database.models import Student

security = HTTPBearer()


async def has_access(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    """
        Function that is used to validate the token in the case that it requires it
    """
    token = credentials.credentials
    try:
        payload = jwt.decode(token, key='secret', options={"verify_signature": False,
                                                           "verify_aud": False,
                                                           "verify_iss": False})
        print("payload => ", payload)


    except JOSEError as e:  # catches any exception
        raise HTTPException(
            status_code=401,
            detail=str(e))

    user_email = payload.get('sub')
    user_id = db.query(Student).filter(Student.email == user_email).first()
    return user_id