import time
from PIL import Image, ImageDraw, ImageFont
from Joystick import Joystick
from Keeper import Keeper


class Kicker:
    def __init__(self, position):
        self.joystick = Joystick()
        self.background = Image.open('background.png')
        self.position = position

    def kick(self, flag, save, command=None):
        keeper = Keeper((75, 30), self.background)
        k_position = list(keeper.position)
        position = list(self.position)
        self.save = save
        if command['kick'] == True:
            if flag == 0:  # 정면으로 찼을 때
                while (position[1] > 50):  # 골대안에 공이 들어갈 때까지 반복
                    if save == 1:  # 키퍼가 왼쪽으로 막는 경우
                        keeper.left()
                    elif save == 2:  # 키퍼가 오른쪽으로 막는 경우
                        keeper.right()
                    position[1] -= 5  # 공 정면으로 움직이기
                    position[3] -= 5
                    background = self.background.copy()
                    keeper_move = Keeper(keeper.position, background)  # 골키퍼 움직이기
                    background.paste(keeper_move.shape, keeper_move.position)
                    draw = ImageDraw.Draw(background)
                    draw.ellipse(position, fill=(0, 0, 0))
                    self.joystick.disp.image(background)
                time.sleep(2)  # 2초간 재생
                position = list(self.position)
                background = self.background.copy()
                keeper = Keeper((75, 30), background)  # 골키퍼 원위치
                background.paste(keeper.shape, keeper.position)
                draw = ImageDraw.Draw(background)  # 공 원위치
                draw.ellipse(position, fill=(0, 0, 0))
                self.joystick.disp.image(background)

            elif flag == 1:  # 왼쪽으로 찼을 때
                while (position[1] > 50):  # 골대안에 공이 들어갈 때까지 반복
                    if save == 1:  # 키퍼가 왼쪽으로 막는 경우
                        keeper.left()
                    elif save == 2:  # 키퍼가 오른쪽으로 막는 경우
                        keeper.right()

                    position[0] -= 3  # 공 왼쪽으로 움직이기
                    position[2] -= 3
                    position[1] -= 5
                    position[3] -= 5
                    background = self.background.copy()
                    keeper_move = Keeper(keeper.position, background)  # 골키퍼 움직이기
                    background.paste(keeper_move.shape, keeper_move.position)
                    draw = ImageDraw.Draw(background)  # 공 제자리로 움직이기
                    draw.ellipse(position, fill=(0, 0, 0))
                    self.joystick.disp.image(background)
                time.sleep(2)
                position = list(self.position)
                background = self.background.copy()
                keeper = Keeper((75, 30), background)  # 골키퍼 원위치
                background.paste(keeper.shape, keeper.position)
                draw = ImageDraw.Draw(background)  # 공 원위치
                draw.ellipse(position, fill=(0, 0, 0))
                self.joystick.disp.image(background)

            elif flag == 2:  # 오른쪽으로 찼을 때
                while (position[1] > 50):  # 골대안에 공이 들어갈 때까지 반복
                    if save == 1:
                        keeper.left()
                    elif save == 2:
                        keeper.right()
                    position[0] += 3  # 공 오른쪽으로 움직이기
                    position[2] += 3
                    position[1] -= 5
                    position[3] -= 5
                    background = self.background.copy()
                    keeper_move = Keeper(keeper.position, background)  # 골키퍼 움직이기
                    background.paste(keeper_move.shape, keeper_move.position)
                    draw = ImageDraw.Draw(background)
                    draw.ellipse(position, fill=(0, 0, 0))
                    self.joystick.disp.image(background)
                time.sleep(2)
                position = list(self.position)
                background = self.background.copy()
                keeper = Keeper((75, 30), background)  # 골키퍼 원위치
                background.paste(keeper.shape, keeper.position)
                draw = ImageDraw.Draw(background)  # 공 원위치
                draw.ellipse(position, fill=(0, 0, 0))
                self.joystick.disp.image(background)

        self.position = tuple(position)