import glob
import sys
import time
from PIL import Image, ImageDraw, ImageFont

from utils import *
from image import letterbox_image, correct_yolo_boxes
from darknet import Darknet

globals()["namesfile"] = "coco.names"

def detect(m, cfgfile, weightfile, imgfile, destfile):
	m = Darknet(cfgfile)
	
    m.print_network()
    m.load_weights(weightfile)
    print('Loading weights from %s... Done!' % (weightfile))
    
    use_cuda = torch.cuda.is_available()
    if use_cuda:
        m.cuda()

    img = Image.open(imgfile).convert('RGB')
    sized = letterbox_image(img, m.width, m.height)

    start = time.time()
    boxes = do_detect(m, sized, 0.5, 0.4, use_cuda)
    correct_yolo_boxes(boxes, img.width, img.height, m.width, m.height)

    finish = time.time()
    print('%s: Predicted in %f seconds.' % (imgfile, (finish-start)))

    class_names = load_class_names(namesfile)
    plot_boxes(img, boxes, destfile, class_names)
