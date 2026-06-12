from pydantic import BaseModel, Field
from typing import Optional , List ,Literal

ClaimType = Literal["health", "travel" , "vehicle", "property"]
UserRole = Literal["admin" ,"customer"]
ChatRole = Literal["user","assistant"]

class ChatMessage(BaseModel):
    role: ChatRole
    message: str


class UploadedDocument(BaseModel):
    file_name: str
    file_type: Optional[str] = None
    file_path: Optional[str] = None
    extracted_text: Optional[str] = None



class CustomerClaimInput(BaseModel):
    #Basic Customer Details
    customer_name: Optional[str]= None
    customer_email: Optional[str]= None
    policy_number: Optional[str]= None


    #Baisc Claim Details
    claim_type: Optional[ClaimType]= None
    claim_amount: Optional[float] = Field(default=None, gt=0)
    incident_date: Optional[str]= None
    incident_location: Optional[str]= None
    incident_description: Optional[str]= None


    #Uploaded Documents
    uploaded_documents: List[UploadedDocument]= Field(default_factory=list)

    #ChatMeassage Support
    chat_meassages: List[ChatMessage]= Field(default_factory=list)
    missing_fields: List[str]= Field(default_factory=list)
    is_ready_to_processing: bool = False


    # Health-specific fields
    hospital_name: Optional[str] = None
    treatment_type: Optional[str] = None
    admission_date: Optional[str] = None
    discharge_date: Optional[str] = None

    # Vehicle-specific fields
    vehicle_number: Optional[str] = None
    vehicle_model: Optional[str] = None
    garage_name: Optional[str] = None
    accident_type: Optional[str] = None

    # Property-specific fields
    property_address: Optional[str] = None
    damage_type: Optional[str] = None
    estimated_repair_cost: Optional[float] = Field(default=None, gt=0)

    # Travel-specific fields
    travel_booking_id: Optional[str] = None
    travel_issue_type: Optional[str] = None
    trip_date: Optional[str] = None











