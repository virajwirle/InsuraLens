from schemas.claim_schema import CustomerClaimInput


COMMON_REQUIRED_FIELDS = [
    "customer_name",
    "customer_email",
    "policy_number",
    "claim_type",
    "claim_amount",
    "incident_date",
    "incident_location",
    "incident_description",
]


CLAIM_TYPE_REQUIRED_FIELDS = {
    "health": [
        "hospital_name",
        "treatment_type",
        "admission_date",
        "discharge_date",
    ],
    "vehicle": [
        "vehicle_number",
        "vehicle_model",
        "garage_name",
        "accident_type",
    ],
    "property": [
        "property_address",
        "damage_type",
        "estimated_repair_cost",
    ],
    "travel": [
        "travel_booking_id",
        "travel_issue_type",
        "trip_date",
    ],
}

def check_missing_fields(claim: CustomerClaimInput)-> list[str]:
    missing_fields =[]

    for field in COMMON_REQUIRED_FIELDS:
        value = getattr(claim, field)
        if value is None or value == "" :
            missing_fields.append(field)

    if claim.claim_type:
        claim_specific_fields = CLAIM_TYPE_REQUIRED_FIELDS.get(claim.claim_type, [])

    for field in claim_specific_fields:
        value = getattr(claim,field)
        if value is None or value == "":
            missing_fields.append(field)

    return missing_fields

