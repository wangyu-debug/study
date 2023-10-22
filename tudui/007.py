from torch.utils.tensorboard import SummaryWriter
##"""Writes entries directly to event files in the log_dir to be
##    consumed by TensorBoard.
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")

image_path = "B:\\python_torch\\data\\train\\ants_image\\0013035.jpg"
img_PIl = Image.open(image_path)
image_array = np.array(img_PIl)
print(type(image_array))
print(image_array.shape)

writer.add_image("test",image_array,1,dataformats='HWC')




# y = x
for i in range(100):
    writer.add_scalar("y = 3*x",3*i,i)

##tensorboard --logdir=logs --port=6007 port指定端口，避免冲突
writer.close()


