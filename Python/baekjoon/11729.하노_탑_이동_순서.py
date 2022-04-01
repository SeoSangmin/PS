from sys import stdin
moves = []

def hanoi(fro, to, other, disk):
    """
    디스크 묶음을 from 에서 to로 옮기기 위해서는
    맨 아래의 하나의 디스크를 제외한 disk-1 개의 디스크를 other(보조 막대)에 옮긴 뒤
    맨 아래 하나의 디스크를 to로 옮긴다.
    그리고 다시 disk-1 개의 디스크를 other에서 to로 옮긴다.
    :param fro: 디스크 묶음이 처음 자리한 막대 번호
    :param to: 디스크 묶음을 옮기고 싶은 막대 번호
    :param other: 나머지 하나의 막대 번호 - 보조 막대라 하자.
    :param disk: 옮길 디스크 수
    :return: 디스크 갯수에 따른 최소한의 움직임 횟수
    """
    global moves
    if disk == 1:
        moves.append(str(fro))
        moves.append(' ')
        moves.append(str(to))
        moves.append('\n')
        return 1
    else:
        return hanoi(fro, other, to, disk-1) + hanoi(fro, to, other, 1) + hanoi(other, to, fro, disk-1)


print(hanoi(1, 3, 2, int(stdin.readline().rstrip())))
print(''.join(moves))