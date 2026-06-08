from utils.message_builder import build_missing_fields_message

missing_fields = [
    "policy_number",
    "claim_amount",
    "vehicle_number",
    "garage_name"
]

message = build_missing_fields_message(missing_fields)

print(message)