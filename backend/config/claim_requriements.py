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


CLAIM_REQUIREMENTS = {
    "health": {
        "required_fields": [
            "hospital_name",
            "treatment_type",
            "admission_date",
            "discharge_date",
        ],
        "required_documents": [
            "hospital_bill",
            "discharge_summary",
        ],
    },

    "vehicle": {
        "required_fields": [
            "vehicle_number",
            "vehicle_model",
            "garage_name",
            "accident_type",
        ],
        "required_documents": [
            "garage_estimate",
            "accident_photo",
        ],
    },

    "property": {
        "required_fields": [
            "property_address",
            "damage_type",
            "estimated_repair_cost",
        ],
        "required_documents": [
            "damage_photos",
            "repair_estimate",
        ],
    },

    "travel": {
        "required_fields": [
            "travel_booking_id",
            "travel_issue_type",
            "trip_date",
        ],
        "required_documents": [
            "booking_receipt",
            "travel_proof",
        ],
    },
}