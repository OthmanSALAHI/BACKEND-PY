#!/usr/bin/python3

def josephusProblem(n, k):
    win = []
    for i in range(1,n+1):
        win.append(i)

    while len(win) > 2:
        new_win = win[2::k]
        win = new_win
    return win[0]
if __name__ == "__main__":
    winner = josephusProblem(13, 1)
    print(winner)
