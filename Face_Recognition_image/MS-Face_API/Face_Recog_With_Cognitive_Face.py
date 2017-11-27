# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 20:00:38 2017

@author: dhavalma
"""

import wx

import util


class Rect(object):
    """Face Rectangle."""
    def __init__(self, rect):
        super(Rect, self).__init__()
        self.set_rect(rect)

    def set_rect(self, rect):
        """docstring for set_rect"""
        self.left = int(rect['left'])
        self.top = int(rect['top'])
        self.width = int(rect['width'])
        self.height = int(rect['height'])



class Face(object):
    """Face Model for each face."""
    def __init__(self, res, path, size=75):
        super(Face, self).__init__()
        self.path = path
        img = 'C:/Users/dhavalma/AnacondaProjects/FR_HAA/FaceDetect/test/0_Parade_marchingband_1_709.jpg'
        self.bmp = img.ConvertToBitmap()
        self.name = None
        if res.get('faceId'):
            self.id = res['faceId']
        if res.get('persistedFaceId'):
            self.persisted_id = res['persistedFaceId']
        #for r in res:
        #    self.rect = Rect(res['faceRectangle'])
        #    self.bmp = self.bmp.GetSubBitmap(wx.Rect(
        #        self.rect.left,
        #        self.rect.top,
        #        self.rect.width,
        #        self.rect.height,
        #    ))
        
        if res.get('faceRectangle'):
            self.rect = Rect(res['faceRectangle'])
            self.bmp = self.bmp.GetSubBitmap(wx.Rect(
                self.rect.left,
                self.rect.top,
                self.rect.width,
                self.rect.height,
            ))
        if res.get('faceAttributes'):
            self.attr = Attribute(res['faceAttributes'])
        self.bmp = util.scale_image(
            self.bmp.ConvertToImage(),
            size=size,
        ).ConvertToBitmap()

    def set_name(self, name):
        """Set the name for the face."""
        self.name = name

if __name__ == '__main__':
    unittest.main()