# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 18:22:52 2020

@author: LKUPSSINSKU
"""

#to install the library:
#pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI

from pycocotools.coco import COCO
import numpy as np
import imageio as io

dataDir='../dataset/jandaira/pixel/'
dataType='train2014'
annFile='../dataset/jandaira/pixel/jandaira.json'.format(dataDir,dataType)

coco=COCO(annFile)



catIds = coco.getCatIds(catNms=['Fracture'])
imgIds = coco.getImgIds(catIds=catIds );
imgIds = coco.getImgIds(imgIds = imgIds[0])
img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]
I = io.imread('../dataset/jandaira/pixel/'+img['file_name'])


cat_ids = coco.getCatIds()
anns_ids = coco.getAnnIds(imgIds=img['id'], catIds=cat_ids, iscrowd=None)
anns = coco.loadAnns(anns_ids)
anns_img = np.zeros((img['height'],img['width']))
for ann in anns:
    anns_img = np.maximum(anns_img,coco.annToMask(ann)*ann['category_id'])
io.imwrite('../dataset/jandaira/mask/jandaira.png', anns_img)