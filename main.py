import cv2
import numpy as np


img = cv2.imread("C:/Users/surao/.spyder-py3/proje/papper_Scanner_uyg/1.jpg")

print(img.shape)

rows, cols = img.shape[:2]
click_count = 0  # 4 adet tıklama yapılacak
cv2.namedWindow("img", cv2.WINDOW_NORMAL)

# Hedef noktalar tanımlanıyor
dst_points = np.float32([
    [0, 0],
    [cols-1, 0],#SAĞ ÜST KÖŞE
    [0, rows-1],#SOL ALT KÖŞE
    [cols-1, rows-1]#SAĞ ALT KÖŞE
])

# Tıklanan noktaları depolamak için boş bir liste
a = [] 

# Çizim fonksiyonu
def draw(event, x, y, flags, param):
    global click_count, a
    if click_count < 4:
        if event == cv2.EVENT_LBUTTONDBLCLK:
            print(click_count)
            print(x, y)
            click_count += 1
            a.append((x, y))
    else:  # Değerleri sıfırla ve perspektif dönüşümü 
        src_points = np.float32([
            [a[0][0], a[0][1]],
            [a[1][0], a[1][1]],
            [a[2][0], a[2][1]],
            [a[3][0], a[3][1]]
        ])
        
        click_count = 0
        a = []
 
        M = cv2.getPerspectiveTransform(src_points, dst_points)

        img_output = cv2.warpPerspective(img, M, (cols, rows))  # cols ve rows sırası düzeltildi
        cv2.imshow("img_output", img_output)
    pass

cv2.setMouseCallback("img", draw)

while True:
    cv2.imshow("img", img)
    
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
