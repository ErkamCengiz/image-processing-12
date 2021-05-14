import cv2

kamera=cv2.VideoCapture(0)

def cozunurluk_1080():
    kamera.set(3,1920)
    kamera.set(4,1080)
def cozunurluk_720():
    kamera.set(3,1280)
    kamera.set(4,720)
def cozunurluk_480():
    kamera.set(3,640)
    kamera.set(4,480)
def coz_belirle(widht, height):
    kamera.set(3, widht)
    kamera.set(4, height)

cozunurluk_720()
def scalalama(frame , percent=75): ## resmin yüzde kaçlık bölümünü göstertmek istersek onu sağlatıyoruz ½75 lik kısmını götertiyoruz
    width=int(frame.shape[1]*percent/100)
    height = int(frame.shape[0] * percent / 100)
    boyut=(width,height)
    return cv2.resize(frame,boyut,interpolation=cv2.INTER_AREA)

while True:
    ret, frame= kamera.read()
    frame75=scalalama(frame,75)
    cv2.imshow('goruntu',frame)
    cv2.imshow('frame',frame75)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()