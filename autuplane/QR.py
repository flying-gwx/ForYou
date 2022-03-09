from MyQR import myqr # 需先安装MyQR库
import zxing
import cv2


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

def Draw_box(image, points):
    image = cv2.imread(image)
    draw_1=cv2.rectangle(image, (int(points[0][0]), int(points[0][1])), (int(points[2][0]),int(points[2][1])), (0,0,255), 10)
    cv2.imwrite('result.jpg',draw_1)


def Read_message(img_path):
    reader = zxing.BarCodeReader()
    barcode = reader.decode(img_path)
    return barcode

Generate_QR('Viliage:xingfucun.Name:wangfuguo',save_name='name.png')

message = Read_message('test2.jpg')

print(f'读出的信息是{message.raw}')
print(f'所有信息：{message}')
#Draw_box('test.jpg',message.points)

