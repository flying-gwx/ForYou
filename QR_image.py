from MyQR import myqr # 需先安装MyQR库

def QR_myqr(url,  save_name,QR_picture= None):
    if QR_picture ==None:
        myqr.run(
       # 'https://flying-gwx.github.io/ForYou/page.html', # 二维码指向链接，或无格式文本（但不支持中文）
        url,
        version = 5, # 大小1~40
        level='H', # 纠错级别
      #  picture = QR_picture, # 底图路径
        colorized = True, # 彩色
        contrast = 1.0, # 对比度
        brightness = 1.0, # 亮度
        save_name = save_name, # 保存文件名
        
    )
    else:
        myqr.run(
        # 'https://flying-gwx.github.io/ForYou/page.html', # 二维码指向链接，或无格式文本（但不支持中文）
            url,
            version = 5, # 大小1~40
            level='H', # 纠错级别
            picture = QR_picture, # 底图路径
            colorized = True, # 彩色
            contrast = 1.0, # 对比度
            brightness = 1.0, # 亮度
            save_name = save_name, # 保存文件名
            
        )

def Generate_QR(message,  save_name):
    myqr.run(
        message, # 二维码贮存信息
        version = 5, # 大小1~40
        level='H', # 纠错级别
      #  picture = QR_picture, # 底图路径
        colorized = True, # 彩色
        contrast = 1.0, # 对比度
        brightness = 1.0, # 亮度
        save_name = save_name, # 保存图片的名字
        
    )



QR_myqr('https://flying-gwx.github.io/ForYou/3dPhoto.html',  QR_picture= './data/2.jpg', save_name='3dPhoto_QR.png')
QR_myqr('https://flying-gwx.github.io/ForYou/FullPhoto.html',  QR_picture= './data/4.jpg', save_name='FullPhoto_QR.png')

# QR_myqr('LaoRen_test,LianhuaCun',save_name='name.png')

