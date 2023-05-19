import pika, json

def upload(f,fs,channel,access):
    try:
        fid = fs.put(f)
    except Exception as err:
        return "internal server error",500
    
    message = {
        "video_f":str(fid),
        "mp3_fid":None,
        "username":access["username"],
    }

    #!Putting the message on the Queue
    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties = pika.BasicProperties(
            pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except:
        fs.delete(fid)
        return "internal server error",500
    

