from schemas.claim_schema import CustomerClaimInput
from config.claim_requriements import COMMON_REQUIRED_FIELDS , CLAIM_REQUIREMENTS

def check_missing_fields(claim: CustomerClaimInput)-> list[str]:
    missing_fields =[]

    for field in COMMON_REQUIRED_FIELDS:
        value = getattr(claim, field)
        if value is None or value == "" :
            missing_fields.append(field)

    if claim.claim_type:
        claim_specific_fields = CLAIM_REQUIREMENTS.get(
            claim.claim_type, {}
        ).get("required_fields", [])

    for field in claim_specific_fields:
        value = getattr(claim,field)
        if value is None or value == "":
            missing_fields.append(field)

    return missing_fields



def is_claim_ready(claim: CustomerClaimInput) -> bool:
    missing_fields = check_missing_fields(claim)
    return len(missing_fields) == 0
