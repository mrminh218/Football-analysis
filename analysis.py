# Viết code cho file "analysis.py" thực hiện các công việc sau
#a. load toàn bộ nội dung file "EPL_2018_2019.csv" vào biến data
#b. Viết hàm get_match(team, round) lấy kết quả trận đấu của một đội bóng ở vòng "round"
#c. viết hàm get_point(team) tính điểm của 1 đội bóng qua từng vòng, sau đó vẽ điểm số lên đồ thị

import csv 
import numpy as np
import matplotlib.pyplot as plt
raw = []
with open("EPL_2018_2019.csv", 'r') as f:
    all_file = csv.reader(f)
    for line in all_file:
        raw.append(line[4:6]+line[7:8]+line[12:14])
    title = raw.pop(0)
    
data = np.array(raw)
# print(data)
# title = np.array(title)
# print(data[2,0])

def get_match(team, round):
    start = 10*round-10
    end = 10*round
    res = -1
    pos = -1
    for i in range(start, end):
        if team == data[i,0]:
            res = i
            pos = 0
        elif team == data[i,1]:
            res = i
            pos = 1
    if res == -1:
        return [0,0]
    return data[res]

print(get_match("Manchester United",1))

def get_point(team):
    rounds_number = 38
    rounds = []
    scores = []
    for i in range(rounds_number):
        info = get_match(team, i)
        # print(info)
        
        # print(info[0])
        if info[0] == team:
            scores.append(int(info[3]))
            rounds.append(i)
        elif info[1] == team:
            scores.append(int(info[4]))
            rounds.append(i)
    return rounds, scores

print(get_point("Manchester United"))

def draw_plot(x, y, plot_title, x_tit, y_tit, marker='o', linestyle='-', color='red'):
    plt.plot(x,y)
    plt.xlabel(x_tit)
    plt.ylabel(y_tit)
    plt.title(plot_title)
    plt.xlim(1,38)
    plt.grid(True)
    plt.legend()
    plt.show()

x,y = get_point("Manchester United")
draw_plot(np.array(x)+1 ,y, "Manchester United scores", "Rounds", "Scores")