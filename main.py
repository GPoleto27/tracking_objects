from cv2 import cv2

# Altere essa variável para utilizar outros videos ou câmeras
video_source = "video.mp4"

cap = cv2.VideoCapture(video_source)

# MOSSE: mais rápido, menos preciso
#tracker = cv2.TrackerMOSSE_create()

# CSRT: mais lento, maior precisão
# tracker = cv2.TrackerCSRT_create()

# KCF: mais rápido que CSRT, mais preciso que MOSSE
tracker = cv2.TrackerKCF_create()

# Lê o primeiro quadro
success, img = cap.read()

# Cria uma caixa limitante com o input do mouse
bounding_box = cv2.selectROI("Tracking", img, False)

# Inicia um Rastreador
tracker.init(img, bounding_box)


# Função para desenhar a caixa limitante
def drawBox(img, bounding_box):
    x, y, w, h = (int(i) for i in bounding_box)

    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


while True:
    # Lê o frame
    success, img = cap.read()

    # Atualiza o rastreador
    success, bounding_box = tracker.update(img)

    # Se encontrou
    if success:
        drawBox(img, bounding_box)
        cv2.putText(img, "Rastreando", (25, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(img, "Perdido", (25, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    try:
        # Exibe a imagem
        cv2.imshow("Tracking", img)
    except:
        break

    cv2.waitKey(1)
