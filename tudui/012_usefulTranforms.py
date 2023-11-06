from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("logs")

img_path = "B:\\python_torch\\data\\train\\ants_image\\0013035.jpg"
img = Image.open(img_path)
print(img)

##ToTensor()
trans_totensor = transforms.ToTensor()
img_tensor = trans_totensor(img)
writer.add_image("Totensor",img_tensor)

##Normalize 归一化
print(img_tensor[0][0][0])
trans_norm = transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
img_norm = trans_norm(img_tensor)
print(img_tensor[0][0][0])
writer.add_image("Nomalize",img_norm)

##Resize 等比缩放
print(img.size)
tran_size = transforms.Resize((512,512))
img_resize = tran_size(img)
print(img_resize)
img_resize  = trans_totensor(img_resize)
writer.add_image("img_resize",img_resize,0)


writer.close()

























