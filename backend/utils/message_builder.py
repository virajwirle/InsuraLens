FIELD_LABELS = {
    "customer_name": "customer name",
    "customer_email": "customer email",
    "policy_number": "policy number",
    "claim_type": "claim type",
    "claim_amount": "claim amount",
    "incident_date": "incident date",
    "incident_location": "incident location",
    "incident_description": "incident description",

    "hospital_name": "hospital name",
    "treatment_type": "treatment type",
    "admission_date": "admission date",
    "discharge_date": "discharge date",

    "vehicle_number": "vehicle number",
    "vehicle_model": "vehicle model",
    "garage_name": "garage name",
    "accident_type": "accident type",

    "property_address": "property address",
    "damage_type": "damage type",
    "estimated_repair_cost": "estimated repair cost",

    "travel_booking_id": "travel booking ID",
    "travel_issue_type": "travel issue type",
    "trip_date": "trip date",
}


def build_missing_fields_message(missing_fields: list[str]) -> str:
    if not missing_fields:
        return "All required information is complete. Your claim is ready for processing."

    readable_fields = [
        FIELD_LABELS.get(field, field.replace("_", " "))
        for field in missing_fields
    ]

    fields_text = "\n".join([f"- {field}" for field in readable_fields])

    return f"Please provide the following missing information:\n{fields_text}"