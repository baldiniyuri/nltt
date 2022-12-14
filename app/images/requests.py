import requests, os


URL = os.getenv('RESIZE_URL')


def Send_Image_For_Resize(request, image_id):

        data = {"user_id_from_request" : request.data["user_id"],"image_id_from_request": image_id, "image_to_resize": request.data['image']}
        
        try:
            requests.post(URL, data)
            return True
        except:
            return False