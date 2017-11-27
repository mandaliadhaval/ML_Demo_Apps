import cv2
import sys
import demo

#%pwd
#import os
#os.chdir('C:/Users/dhavalma/AnacondaProjects/FR_HAA/FaceDetect')
# Get user supplied values
#imagePath = './test/Testing/53_Raid_policeraid_53_782.jpg'
#imagePath = './test/Testing/0_Parade_marchingband_1_709.jpg'
#imagePath = './test/Testing/44_Aerobics_Aerobics_44_460.jpg'
#imagePath = './test/Testing/41_Swimming_Swimming_41_59.jpg'
#imagePath = './test/Testing/40_Gymnastics_Gymnastics_40_340.jpg'
#imagePath = './test/Testing/No_Face.jpg'
#imagePath = './test/Testing/No_Face_1.jpg'
#imagePath = './test/Testing/No_Face_2.jpg'


#cascPath = "lbpcascade_front_Face.xml"
# Create the haar cascade
demo.run_training(imagePath)
