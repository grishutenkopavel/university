import qrcode


def createQRCode(strData):

    filename = "./string.png"
    # генерируем qr-код
    img = qrcode.make(strData)
    img.show()
    # сохраняем img в файл
    # img.save(filename)

    
    

createQRCode('simple string') 