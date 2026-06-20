from backend.database.sqlite_db import get_connection , create_claims_table



def claim_id_generator():
    """Generate Claim Id"""
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
SELECT claim_id FROM claims ORDER BY created_at DESC LIMIT 1
""")
    
    last_claim = cursor.fetchone()
    conn.close()
     

    if last_claim is None:
        return "CLM-2026-0001"
    else :
        last_claim_id = last_claim[0]
        last_number = last_claim_id.split("-")[-1]

        new_number = int(last_number)+1
        new_claim_id = f"CLM-2026-{new_number:04d}"

        return new_claim_id
    