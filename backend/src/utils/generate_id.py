import uuid

def unique_id():
    unique_id = str(uuid.uuid4()).split("-")
    unique_id = "".join([value for value in unique_id])
    return unique_id[:20]

