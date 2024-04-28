import random
import uuid
from datetime import datetime

def generate_id()->str:
    return (str(uuid.uuid4())+str(int(datetime.timestamp(datetime.now())))+str(random.randint(11111,99999))).replace('-','')
