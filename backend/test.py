from schemas.claim_schema import ChatMessage, UploadedDocument,CustomerClaimInput
from pydantic import ValidationError
from utils.field_checker import check_missing_fields

sample_claim = CustomerClaimInput(
    customer_name="Rahul Sharma",
    customer_email="rahul@gmail.com",
    policy_number="POL12345",
    claim_type="vehicle",
    claim_amount=85000,
    incident_date="2026-06-01",
    incident_location="Panvel",
    incident_description="My Honda City met with an accident near Panvel.",
    uploaded_documents=[
        UploadedDocument(
            file_name="garage_bill.pdf",
            file_type="pdf",
            file_path="uploads/garage_bill.pdf"
        ),
        UploadedDocument(
            file_name="accident_photo.jpg",
            file_type="jpg",
            file_path="uploads/accident_photo.jpg"
        )
    ],
    chat_history=[
        ChatMessage(
            role="user",
            message="I want to claim vehicle insurance for my accident."
        ),
        ChatMessage(
            role="assistant",
            message="Please provide your policy number, accident location, and claim amount."
        )
    ],
    vehicle_number="MH05AB1234",
    vehicle_model="Honda City",
    garage_name="Sai Auto Works",
    accident_type="road accident"
)

print(sample_claim)
print("\nJSON format:")
print(sample_claim.model_dump_json(indent=4))


try:
    wrong_claim = CustomerClaimInput(
        claim_type="vehicle",
        claim_amount=-5000
    )
    print(wrong_claim)
except ValidationError as e:
    print(e)


claim = CustomerClaimInput(
    customer_name="Rahul Sharma",
    customer_email="rahul@gmail.com",
    policy_number="POL12345",
    claim_type="vehicle",
    claim_amount=85000,
    incident_date="2026-06-01",
    incident_description="My Honda City met with an accident.",
)

missing = check_missing_fields(claim)

print("Missing fields:")
print(missing)