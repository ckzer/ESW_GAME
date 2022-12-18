from PIL import Image, ImageDraw, ImageFont
import time
import random
import os
import sys
import cv2 as cv
from colorsys import hsv_to_rgb
from Kicker import Kicker
from Keeper import Keeper
from Joystick import Joystick


def restart():  # 재시작
    os.execl(sys.executable, sys.executable, *sys.argv)


def main():
    joystick = Joystick()
    my_image = Image.open('background.png')
    my_draw = ImageDraw.Draw(my_image)
    background = my_image.copy()
    my_draw.ellipse((110, 180, 140, 210), fill=(0, 0, 0))
    kicker = Kicker((110, 180, 140, 210))
    keeper = Keeper((75, 30), background)
    my_image.paste(keeper.shape, (keeper.position[0], keeper.position[1]))
    flag = 0  # 방향(0은 정면, 1은 왼쪽, 2는 오른쪽)
    kicker_flag = 0  # 공격(0은 user, 1은 ai)
    joystick.disp.image(my_image)
    user_goal = 0  # 유저 골
    user_cnt = 0  # 유저 찬 횟수
    ai_goal = 0  # ai 골
    ai_cnt = 0  # ai 골
    cnt = 0  # 전체 찬 횟수

    def Win():
        ending = Image.open("win.png").convert("RGBA")
        my_image_end = my_image.copy()
        my_image_end = Image.alpha_composite(my_image_end, ending)
        joystick.disp.image(my_image_end)
        time.sleep(3)
        restart()  # 재시작

    def Lose():
        ending = Image.open("lose.png").convert("RGBA")
        my_image_end = my_image.copy()
        my_image_end = Image.alpha_composite(my_image_end, ending)
        joystick.disp.image(my_image_end)
        time.sleep(3)
        restart()  # 재시작

    while True:
        command = {'kick': False}

        if not joystick.button_U.value:  # up pressed
            flag = 0

        if not joystick.button_L.value:  # left pressed
            flag = 1

        if not joystick.button_R.value:  # right pressed
            flag = 2

        if not joystick.button_A.value:  # A pressed
            command['kick'] = True

        if command['kick'] == True and kicker_flag == 0:  # 유저가 찰 때
            save = random.randint(0, 2)  # ai가 막는 방향 랜덤함수 이용
            kicker.kick(flag, save, command)
            kicker_flag = 1
            user_cnt += 1  # 유저 찬 횟수 증가
            if flag != save:  # 골인이면 user goal +1
                user_goal += 1

        elif command['kick'] == True:  # AI가 찰 때
            save = random.randint(0, 2)  # ai가 차는 방향 랜덤함수 이용
            kicker.kick(save, flag, command)
            kicker_flag = 0
            ai_cnt += 1  # ai 찬 횟수 증가
            if flag != save:  # 골인이면 ai goal +1
                ai_goal += 1

        # user가 전부 득점하고 ai가 실패해도 ai를 못이길 경우
        if (5 - user_cnt) + user_goal < ai_goal and user_cnt <= 5:
            Lose()

        # ai가 전부 득점하고 user가 실패해도 user를 못이길 경우
        elif (5 - ai_cnt) + ai_goal < user_goal and ai_cnt <= 5:
            Win()

        # ai와 user 찬 횟수 10회가 넘거나 서로 5번차서 승보가 안난 경우 서로 1번씩 더 차서 승부를 겨룸
        elif (user_cnt + ai_cnt >= 10) and ((user_cnt + ai_cnt) % 2 == 0):
            if user_goal > ai_goal:  # 유저 승리
                Win()

            elif user_goal < ai_goal:  # ai 승리
                Lose()


if __name__ == '__main__':
    main()