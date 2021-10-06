from MyQR import myqr # 需先安装MyQR库

def QR_myqr():
    myqr.run(
        'https://flying-gwx.github.io/ForYou/test.gif', # 二维码指向链接，或无格式文本（但不支持中文）
        version = 5, # 大小1~40
        level='H', # 纠错级别
       # picture = 'img.jpg', # 底图路径
        colorized = True, # 彩色
        contrast = 1.0, # 对比度
        brightness = 1.0, # 亮度
        save_name = 'save.jpg', # 保存文件名
        
    )


QR_myqr()