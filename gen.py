import qrcode
# 生成二维码
byt = open("qr_code.txt").readline()
print(byt)
img = qrcode.make(data=byt)
# 将二维码保存为图片
with open('test.png', 'wb') as f:
    img.save(f)