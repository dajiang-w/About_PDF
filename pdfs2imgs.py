
# C:\Python\paddleocr\Scripts\activate
import pdfplumber as pp
import os


def pdf2pic(pdfspath,imgspath,format,resolution): # format:bmp,png,jpeg,tiff
    pdffiles = os.listdir(pdfspath) # 此文件夹下只保留pdf文件
    print(pdffiles)
    index = 1
    for pdffile in pdffiles:
        pdfpath = os.path.join(pdfspath, pdffile)
        pdf = pp.open(pdfpath)  # 打开pdf
        pages =  pdf.pages  # 获取指定页面
        for page in pages:
            pgimg = page.to_image(resolution = resolution)
            imagefile = os.path.join(imgspath,"Image" + str(index) + "." + format)
            print("\r converting " + imagefile)
            pgimg.save(imagefile,format = format) # PNG无损，也可以用其它格式如tiff,jpeg
            index += 1


if __name__ == "__main__":
    pdf2pic(pdfspath = "F:\\code\\pdfs",imgspath = "F:\\code\\img",format="JPEG",resolution=300)
