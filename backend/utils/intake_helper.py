from schemas.claim_schema import CustomerClaimInput
from utils.field_checker import  check_missing_fields


def update_claim_readiness(claim: CustomerClaimInput) -> CustomerClaimInput:
    missing_field = check_missing_fields(claim)

    claim.missing_field = missing_field
    claim.is_ready_to_process = len(missing_field) == 0

    return claim