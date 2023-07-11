# About_PDF
codes about PDF processing

## python版本
3.8.10

## 用到的包
  Pillow 9.1.1  
    
  img2pdf 0.4.4
    
  PyPDF 3.0.1
  
  pdfplumber 0.6.2


# 用法
## pdf批量转图片
```cmd
python pdfs2imgs.py F:\pdfs F:\imgs
```
F:\pdfs是pdf所在的目录, F:\imgs是图片文件夹

## 图片转pdf
```cmd
python imgs2pdf.py F:\imgs
```
F:\imgs是图片文件夹，转换完成后，会在F:\imgs生成一个以当前时间为文件名的pdf文件。
