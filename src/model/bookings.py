import pydantic


class Booking(pydantic.BaseModel):
    firstname: str = ""
    lastname: str = ""
    totalprice: int = 0
    depositpaid: bool = False
    additionalneeds: str = ""
