#'zoom과 pixel이 속성이고, 이를 통해 사진을 촬영한다.'를 camera 클래스로 작성하시오
class camera:
    def __init__(self, zoom, pixel):
        self.zoom = zoom
        self.pixel = pixel
        print("{0}과 {1}이 속성이고, 이를 통해 사진을 촬영한다.".format(self.zoom, self.pixel))

cam1 = camera(400, 10)