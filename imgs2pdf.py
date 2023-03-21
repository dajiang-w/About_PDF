import os #导入os库
import time #导入时间库生成时间戳
import img2pdf #导入img2pdf库， 安装命令：pip install img2pdf
from PIL import Image


def imgs2pdf(imgspath: str): 
    '''
    转换JPG图片为PDF   
    如果不是jpg，先使用下面的compressimgs函数转为JPG
    '''
    localtime = time.localtime() #获取本地时间
    timesign = time.strftime("%Y%m%d%H%M%S", localtime) #格式化时间为 202209031212 
    print(time.strftime("%Y%m%d%H%M%S", localtime)) #打印格式化时间
    try:
        with open(os.path.join(imgspath,timesign + '.pdf'), 'wb+') as f:   #创建以二进制读写模式 ‘PDF‘’加时间戳的PDF文件
            imgs =[] #创建图片路径保存列表
            for fname in os.listdir(imgspath): #遍历图片文件夹里面的文件
                if not (fname.endswith(('.jpg','.JPG','.jpeg','.JPEG'))): #遍历文件格式为jpg的图片文件
                    continue
                path = os.path.join(imgspath, fname) #读取图片文件路径
                if os.path.isdir(path):
                    continue
                imgs.append(path)  #添加图片路径到imgs列表
            f.write(img2pdf.convert(imgs)) #转换imgs列表里面所有图片为一个PDF文件
            print("文件保存至" + imgspath) #打印PDF转换成功
    except OSError as err:
        print("OS error: {0}".format(err))  #打印转换出错

def compressimgs(imgspath: str,compresspath: str,quality: int):
    for img in os.listdir(imgspath):
        imgpath = os.path.join(imgspath,img)
        im = Image.open(imgpath)
        im = im.convert('RGB')
        # im = im.convert('JPEG')
        # im.thumbnail((200,200))
        im.save(os.path.join(compresspath,img.split(".")[0] + ".jpg"),optimize=True,quality=quality)
        print( "压缩完成" + compresspath,img.split(".")[0] + ".jpg" )
        
if __name__ == "__main__":
    imgspath = 'F:/code/img/'  #设置图片文件夹
    # compresspath = 'F:/code/compress/'
    # compressimgs(imgspath,compresspath,quality=50)
    imgs2pdf(imgspath)