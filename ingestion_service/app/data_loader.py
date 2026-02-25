from utils import ImageService, SendServie


image = ImageService()
send = SendServie()

import os
def loop_in_file(directory_in_str):
    directory = os.fsencode(directory_in_str)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith('.png'):
            filename = 'data/' + filename 
            data = image.to_kafka(filename)
            print(data)
            send.send_to_kafka(data=data)
            send.send_to_mongodb_loader(data=image.get_image_byts(filename))
         