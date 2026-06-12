from schemas.claim_schema import CustomerClaimInput, ChatMessage
from services.claim_intake_service import process_claim_intake


claim = CustomerClaimInput(
    customer_name="Rahul Sharma",
    customer_email="rahul@gmail.com",
    policy_number="POL12345",
    claim_type="vehicle",
    claim_amount=85000,
    incident_date="2026-06-01",
    incident_description="My Honda City met with an accident near Panvel.",
    chat_messages=[
        ChatMessage(
            role="user",
            message="I want to claim vehicle insurance for my Honda City accident."
        )
    ]
)

updated_claim = process_claim_intake(claim)

print(updated_claim.model_dump_json(indent=4))