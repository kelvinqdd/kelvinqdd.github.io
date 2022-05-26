import cv2
path = r'C:\Users\dudu\Desktop\cv2\\'
for i in range(1,501):
    if len(str(i))==1:
        s = "000"+str(i)
    elif len(str(i))==2:
        s = "00"+str(i)
    elif len(str(i))==3:
        s = "0"+str(i)
    else:
        s = str(i)
    img = cv2.imread(path+r"\input\\"+s+".jpg")
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

    canny = cv2.Canny(img, 50, 100)

    cv2.imwrite(path+r"\ans\\"+str(i)+".png", canny)
    cv2.waitKey(0)