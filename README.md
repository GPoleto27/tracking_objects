# tracking_objects
Aplicação em Python usando OpenCV para tracking de objetos em vídeo.

# Instalação e execução

## Clonando o Repositório
    $ git clone https://github.com/GPoleto27/tracking_objects

## Instalando as dependências, configurações e pesos da rede
    $ sudo chmod +x setup.sh
    $ ./setup.sh

## Execute a aplicação
    $ ./main.py

# Customização da aplicação

## Alterando a fonte do vídeo
Dentro de _main.py_ edite
> Altere essa variável para utilizar outros videos ou câmeras.

    video_source = "video.mp4"
Você pode usar seu próprio arquivo de vídeo ou webcam.

Para arquivo, apenas modifique o nome do arquivo, para usar sua webcam, altere para um inteiro que irá indicar o índice de sua webcam.
> (Normalmente, se há apenas uma câmera, basta utilizar o valor 0).

## Alterando o algoritmo
Dentro de _main.py_ edite

    # MOSSE: mais rápido, menos preciso
    #tracker = cv2.TrackerMOSSE_create()

    # CSRT: mais lento, maior precisão
    # tracker = cv2.TrackerCSRT_create()

    # KCF: mais rápido que CSRT, mais preciso que MOSSE
    tracker = cv2.TrackerKCF_create()

Descomente o método desejado e comente o atual

Para mais informações e outros métodos, consulte [OpenCV Object Tracking](https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/).

# TODO
- Multitracking
- Rodar em GPU