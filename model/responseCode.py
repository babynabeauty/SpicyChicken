def responseCode(status:int, data, message):
    result = {
        "code":int(status),
        "data":data,
        "message":str(message)
    }
    return result