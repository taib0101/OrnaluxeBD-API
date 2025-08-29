import uuid

def unique_id():
    unique_id = uuid.uuid1()
    return str(unique_id)

