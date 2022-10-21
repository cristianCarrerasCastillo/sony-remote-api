# dev by Cristian Carreras

from pysony import SonyAPI, ControlPoint
import time, os

def main():
    search = ControlPoint()
    print("Buscando Camaras")
    cameras =  search.discover(3)

    if len(cameras):
        print("Se encontro una camara")
        camera = SonyAPI(QX_ADDR=cameras[0])
    else:
        print("No se encontraron Camaras disponibles, cerrando el programa")
        quit()
    mode = camera.getAvailableApiList()
        # For those cameras which need it
    if 'startRecMode' in (mode['result'])[0]:
        camera.startRecMode()
        time.sleep(5)

        # and re-read capabilities
        mode = camera.getAvailableApiList()

    camera.startRecMode()
    time.sleep(5)

    # and re-read capabilities
    mode = camera.getAvailableApiList()

    foto = camera.actTakePicture()
    print("foto sacada")
    url =  str(foto['result']).strip("[']")
    url = url.split('\\')
    url = url[0] + url [2] + url[4] + url[6] + url[8]
    link = str(url)
    os.system('wget ' + link + " -P /media")

if __name__ == "__main__":
    main()
    