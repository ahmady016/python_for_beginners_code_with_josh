#######################################################################################
import secrets
def generate_id(length=10):
    # Generate random secure token hex string of length characters
    return secrets.token_hex(length // 2)
#######################################################################################
