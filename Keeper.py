from PIL import Image, ImageDraw, ImageFont


class Keeper:
    def __init__(self, position, background):
        self.position = position
        self.shape = Image.open("Keeper_Front.PNG").convert("RGBA")
        self.shape = self.shape.resize((100, 100))  # 키퍼 이미지 사이즈 확대
        background = background.crop((position[0], position[1], position[0] + 100, position[1] + 100))  # 키퍼 위치 지정
        self.shape = Image.alpha_composite(background, self.shape)  # alpha_composite로 배경 위에 자연스럽게 골키퍼 그리기

    def left(self):  # 왼쪽으로 움직이는 경우
        k_position = list(self.position)
        k_position[0] -= 3
        self.position = tuple(k_position)

    def right(self):  # 오른쪽으로 움직이는 경우
        k_position = list(self.position)
        k_position[0] += 3
        self.position = tuple(k_position)