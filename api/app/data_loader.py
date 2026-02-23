from utilis import ImageService, SendServie


image = ImageService()
send = SendServie()

import os
def loop_in_file(directory_in_str):
    directory = os.fsencode(directory_in_str)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith('.png'):
            filename = 'data/' + filename 
            print(filename)
            data = image.to_kafka(filename)
            send.send_to_kafka(data=data)

loop_in_file('data')            