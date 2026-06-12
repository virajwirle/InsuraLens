from schemas.claim_schema import CustomerClaimInput , ChatMessage
from utils.intake_helper import update_claim_readiness
from utils.message_builder import build_missing_fields_message


def process_claim_intake(claim : CustomerClaimInput) -> CustomerClaimInput:
    """
    Updates claim readiness and adds assistant response
    based on missing fields.
    """

    update_claim = update_claim_readiness(claim)

    assisent_message = build_missing_fields_message(
        update_claim.missing_fields
    ) 


    update_claim.chat_meassages.append(
        ChatMessage(
            role = "assistant",
            message=assisent_message
        )
    )

    return update_claim