from enum import Enum

def sanitize_cy_number(cy_number):
    return (cy_number or "").strip().upper()

class Status(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    SUCCEEDED = "SUCCEEDED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"