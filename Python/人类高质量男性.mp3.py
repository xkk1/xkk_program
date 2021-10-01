#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# auhor: 小喾苦
# 人类高质量男性
import time
import winsound

A = 1600
B = 800
C = 400
D = 200
E = 100
F = 50
L1 = 262
L2 = 294
L3 = 330
L4 = 349
L5 = 392
L6 = 440
L7 = 493
N1 = 532
N2 = 588
N3 = 660
N4 = 698
N5 = 784
N6 = 880
N7 = 988
H1 = 1046
H2 = 1175
H3 = 1319
H4 = 1397
H5 = 1568
H6 = 1760
H7 = 1976

song_list= [
[N6, E], [N7, E], [H1, E], [H1, E], [N7, E], [N5, E+D], # 我晒干了沉默
[N5, E], [N5, E], [N5, E], [N5, E], [N5, E], [H1, E], # 悔得很冲动
[0, D],
[H1, E], [H1, E], [H1, E], [H2, E], [H1, E], [H3, E], # 就算这是做错
[H3, D], [H2, E], [H1, E], [H3, D], [H1, D], [H1, D+E], # 也只是怕错过
[H5, E], [H5, E], [H3, E], [H1, D], [N7, D+E], # 在一起叫梦
[H5, E], [H5, E], [H2, E], [H2, D], [H1, D+E], # 分开了叫痛
[H5, E], [H5, E], [H3, E], [H3, D], [H2, E], [H2, E], [H2, E],
[H3, E], [H2, E], [H1, E], [N7, D], [H1, D+E], # 是不是说没有做完的梦最痛
]


def play(song_list):
    for f,d in song_list:
        d = d*2
        if f != 0:
            winsound.Beep(f, d)
        else:
            time.sleep(d/1000)

def main():
    play(song_list)


if __name__ == "__main__":
    main()
