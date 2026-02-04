from pydantic import BaseModel

class RuleCreate(BaseModel):
    
    name: str
    field: str
    operator: str
    value: str
    # condition: str | None = None
    action: str | None = None
    active: bool = True
    

class RuleOut(RuleCreate):
    id: int

    class Config:
        from_attributes = True
