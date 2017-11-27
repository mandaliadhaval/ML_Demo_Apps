# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 18:18:35 2017

@author: dhavalma
"""

import cognitive_face as CF

KEY = 'efb47541d86b4786a87d8d495aa84b95'
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
#img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
image = 'C:/Users/dhavalma/AnacondaProjects/FR_HAA/FaceDetect/test/0_Parade_marchingband_1_709.jpg'
#result = CF.face.detect(img_url)
result = CF.face.detect(image)
#assertIsInstance(result, list)
print (result)


