from datetime import datetime
def toHuman(timestamp): return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
