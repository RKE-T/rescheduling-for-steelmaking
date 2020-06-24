import random
import matplotlib.pyplot as plt


def draw(ops):
    if ops.eq == 3:
        y_ = 4 - ops.eq_num
    elif ops.eq == 2:
        y_ = 8 - ops.eq_num
    elif ops.eq == 1:
        y_ = 12 - ops.eq_num
    x_sta = ops.sta
    x_end = ops.end
    x = [x_sta, x_end, x_end, x_sta, x_sta]
    y = [y_, y_, y_ + 0.6, y_ + 0.6, y_]
    if ops.jc == 1:
        color = [i * ops.lc / 5 / 255 for i in [208, 16, 76-1]]
    if ops.jc == 2:
        color = [i * ops.lc / 5 / 255 for i in [43, 95, 117-1]]
    if ops.jc == 3:
        color = [i * ops.lc / 5 / 255 for i in [27, 129, 62-1]]
    return [x, y, color]


class Op:
    def __init__(self, jc, lc, eq, eq_num, sta, end):
        self.jc = jc
        self.lc = lc
        self.eq = eq
        self.eq_num = eq_num
        self.sta = sta
        self.end = end

cont = 0
empty = 0
while cont < 20:
    fault_op = [3, 3, 1]
    fault_time = 144
    suspend = 20
    tt = {'1121': 10, '1122': 10, '1123': 13, '1221': 15, '1222': 15, '1223': 13,
          '1321': 15, '1322': 15, '1323': 13, '2131': 22, '2132': 25, '2133': 25,
          '2231': 22, '2232': 25, '2233': 25, '2331': 25, '2332': 22, '2333': 22}
    ot_min = {'1': 3, '2': 5, '3': 5}
    ot_max = {'1': 3, '2': 10, '3': 10}
    ot = {'1': 35, '2': 20, '3': 45}
    ft_backward = {'11': 800, '12': 800, '13': 800, '21': 800, '22': 800, '23': 800}
    ft_forward = {'11': 170, '12': 136, '13': 159 + 20, '21': 200, '22': 171, '23': 192 + 20}

    OPS = [
        [
            [Op(1, 1, 1, 1, 0, 35), Op(1, 1, 2, 1, 45, 65), Op(1, 1, 3, 1, 87, 132)],
            [Op(1, 2, 1, 1, 45, 80), Op(1, 2, 2, 1, 90, 110), Op(1, 2, 3, 1, 132, 177)],
            [Op(1, 3, 1, 1, 90, 125), Op(1, 3, 2, 1, 135, 155), Op(1, 3, 3, 1, 177, 222)],
            [Op(1, 4, 1, 1, 135, 170), Op(1, 4, 2, 1, 180, 200), Op(1, 4, 3, 1, 222, 267)],
            [Op(1, 5, 1, 1, 180, 215), Op(1, 5, 2, 1, 225, 245), Op(1, 5, 3, 1, 267, 312)],
            [Op(1, 6, 1, 1, 225, 260), Op(1, 6, 2, 1, 270, 290), Op(1, 6, 3, 1, 312, 357)]
        ],
        [
            [Op(2, 1, 1, 2, 11, 46), Op(2, 1, 2, 2, 61, 81), Op(2, 1, 3, 2, 106, 151)],
            [Op(2, 2, 1, 2, 56, 91), Op(2, 2, 2, 2, 106, 126), Op(2, 2, 3, 2, 151, 196)],
            [Op(2, 3, 1, 2, 101, 136), Op(2, 3, 2, 2, 151, 171), Op(2, 3, 3, 2, 196, 241)],
            [Op(2, 4, 1, 2, 146, 181), Op(2, 4, 2, 2, 196, 216), Op(2, 4, 3, 2, 241, 286)],
            [Op(2, 5, 1, 2, 191, 226), Op(2, 5, 2, 2, 241, 261), Op(2, 5, 3, 2, 286, 331)],
            [Op(2, 6, 1, 2, 236, 271), Op(2, 6, 2, 2, 286, 306), Op(2, 6, 3, 2, 331, 376)]
        ],
        [
            [Op(3, 1, 1, 3, 34, 69), Op(3, 1, 2, 3, 82, 102), Op(3, 1, 3, 3, 124, 169)],
            [Op(3, 2, 1, 3, 79, 114), Op(3, 2, 2, 3, 127, 147), Op(3, 2, 3, 3, 169, 214)],
            [Op(3, 3, 1, 3, 124, 159), Op(3, 3, 2, 3, 172, 192), Op(3, 3, 3, 3, 214, 259)],
            [Op(3, 4, 1, 3, 169, 204), Op(3, 4, 2, 3, 217, 237), Op(3, 4, 3, 3, 259, 304)],
            [Op(3, 5, 1, 3, 214, 249), Op(3, 5, 2, 3, 262, 282), Op(3, 5, 3, 3, 304, 349)],
            [Op(3, 6, 1, 3, 259, 294), Op(3, 6, 2, 3, 307, 327), Op(3, 6, 3, 3, 349, 394)]
        ]
    ]
    fault_op = [i - 1 for i in fault_op]
    OPS[fault_op[0]][fault_op[1]][fault_op[2]].sta = fault_time
    OPS[fault_op[0]][fault_op[1]][fault_op[2]].end = \
    fault_time + ot[str(fault_op[2] + 1)] - ot_min[str(fault_op[2] + 1)]

    for i in range(fault_op[2]+1, 3):
        OPS[fault_op[0]][fault_op[1]][i].sta = \
            OPS[fault_op[0]][fault_op[1]][i-1].end + \
            tt[str(OPS[fault_op[0]][fault_op[1]][i-1].eq) +
               str(OPS[fault_op[0]][fault_op[1]][i-1].eq_num) +
               str(OPS[fault_op[0]][fault_op[1]][i].eq) +
               str(OPS[fault_op[0]][fault_op[1]][i].eq_num)]
        OPS[fault_op[0]][fault_op[1]][i].end = \
            OPS[fault_op[0]][fault_op[1]][i].sta + \
            ot[str(OPS[fault_op[0]][fault_op[1]][i].eq)] - \
            ot_min[str(OPS[fault_op[0]][fault_op[1]][i].eq)]+1
    i=1
    while fault_op[1] + i <= 5:
        OPS[fault_op[0]][fault_op[1] + i][2].sta = OPS[fault_op[0]][fault_op[1] + i - 1][2].end
        OPS[fault_op[0]][fault_op[1] + i][2].end = OPS[fault_op[0]][fault_op[1] + i][2].sta + ot['3']
        i = i + 1

    space = OPS[fault_op[0]][fault_op[1]][2].sta - OPS[fault_op[0]][fault_op[1]-1][2].end
    OPS[2][0][2].end = OPS[2][0][2].end +10
    OPS[2][1][2].end = OPS[2][1][2].end +13
    OPS[2][1][2].sta = OPS[2][1][2].sta +10
    OPS_ing = []
    for i in OPS:
        for j in i:
            if j[0].sta > fault_time:
                OPS_ing.append(j[2])

    OPS_ing.sort(key=lambda x: x.sta, reverse=True)
    cont = cont + 1
    for cur_lc in OPS_ing:
        ct_ = 1000
        sta_ = 0
        alt_c = []
        alt_ct = []
        alt_sta = []
        for i in [1, 2, 3]:
            idea_sta = cur_lc.sta - ot['2'] - tt['2' + str(i) + '3' + str(cur_lc.eq_num)]
            sta = min([idea_sta, ft_backward['2' + str(i)] - ot['2']])
            ct = idea_sta - sta
            # if ct == ct_:
            if sta >= ft_forward['2' + str(i)]:
                temp = Op(cur_lc.jc, cur_lc.lc, cur_lc.eq - 1, i, sta, sta + ot['2'])
                alt_c.append(temp)

        for i in alt_c:
            idea_sta = cur_lc.sta - ot['2'] - tt['2' + str(i.eq_num) + '3' + str(cur_lc.eq_num)]
            ct = idea_sta - sta
            if ct == ct_:
                alt_ct.append(i)
            elif ct < ct_:
                alt_ct = [i]
                ct_ = ct

        for i in alt_ct:
            if i.sta == sta_:
                alt_sta.append(i)
            elif i.sta > sta_:
                sta_ = i.sta
                alt_sta = [i]
        if len(alt_sta) == 0:
            empty = 1
            break
        step = random.choice(alt_sta)
        OPS[cur_lc.jc - 1][cur_lc.lc - 1][cur_lc.eq - 2] = step
        ft_backward['2' + str(step.eq_num)] = step.sta

        alt_c = []
        alt_ct = []
        alt_sta = []
        ct_ = 1000
        sta_ = 0
        cur_lc = step
        for i in [1, 2, 3]:
            idea_sta = cur_lc.sta - ot['1'] - tt['1' + str(i) + '2' + str(cur_lc.eq_num)]
            sta = min([idea_sta, ft_backward['1' + str(i)] - ot['1']])
            ct = idea_sta - sta
            # if ct == ct_:
            if sta >= ft_forward['1' + str(i)]:
                temp = Op(cur_lc.jc, cur_lc.lc, cur_lc.eq - 1, i, sta, sta + ot['1'])
                alt_c.append(temp)

        for i in alt_c:
            idea_sta = cur_lc.sta - ot['1'] - tt['1' + str(i.eq_num) + '2' + str(cur_lc.eq_num)]
            ct = idea_sta - sta
            if ct == ct_:
                alt_ct.append(i)
            elif ct < ct_:
                alt_ct = [i]
                ct_ = ct

        for i in alt_ct:
            if i.sta == sta_:
                alt_sta.append(i)
            elif i.sta > sta_:
                sta_ = i.sta
                alt_sta = [i]
        if len(alt_sta) == 0:
            empty = 1
            break
        step = random.choice(alt_sta)
        OPS[cur_lc.jc - 1][cur_lc.lc - 1][cur_lc.eq - 2] = step
        ft_backward['1' + str(step.eq_num)] = step.sta
        empty = 0
    if empty == 0:
        break

fig = plt.figure(figsize=[15, 6])
coordinate = fig.add_subplot(1, 1, 1)
coordinate.axes.yaxis.set_visible(False)
coordinate.spines['right'].set_visible(False)
coordinate.spines['left'].set_visible(False)
coordinate.spines['top'].set_visible(False)
coordinate.spines['right'].set_visible(False)



for i in OPS:
    for j in i:
        for o in j:
            line = coordinate.plot([-10, 420], [0, 13], color=draw(o)[2], linewidth=3)[0]
            line.set_data(draw(o)[0], draw(o)[1])
            text = coordinate.text((draw(o)[0][0] + draw(o)[0][1]) / 2 - 6, draw(o)[1][0] + 0.1,
                                   str(o.jc) + str(o.lc) + str(o.eq), rotation=0, fontsize='12')

for i in OPS:
    for j in i:
        for o in [0, 1]:
            line = coordinate.plot([-10, 420], [0, 13], color=draw(j[o])[2], linewidth=1)[0]
            line.set_data([draw(j[o])[0][1], draw(j[o + 1])[0][3]], [draw(j[o])[1][1], draw(j[o + 1])[1][3]])

eq = ['LD', 'RH', 'CC']
for i in range(0,9):
    line = coordinate.plot([-10, 420], [0, 13], color=[0.5, 0.5, 0.5], linewidth=0.5)[0]
    line.set_data([-10, 500], [i+int(i/3)+1, i+int(i/3)+1])
    text = coordinate.text(-40, 11 - i - int(i/3)-0.15, eq[int(i / 3)] + str(i % 3 + 1), rotation=0,  fontsize='16')
print('''\\begin{longtable}[h]{|c|c|c|c|c|c|c|c|c|c|c|}
\caption{启发式算法调度仿真结果炉次操作开工/完工时间表}
\label{tab:time_table}\\\
\hline
\multirow{2}{*}{浇次} & \multirow{2}{*}{炉次} & \multicolumn{3}{c|}{转炉} & \multicolumn{3}{c|}{精炼} & \multicolumn{3}{c|}{连铸} \\\ \cline{3-11}
                    &                     & 设备     & 开始     & 结束    & 设备     & 开始     & 结束    & 设备     & 开始     & 结束    \\\ \hline
\endfirsthead
%
\multicolumn{11}{c}%
{{表 \\thetable\ 续表}} \\\
\hline
\multirow{2}{*}{浇次} & \multirow{2}{*}{炉次} & \multicolumn{3}{c|}{转炉} & \multicolumn{3}{c|}{精炼} & \multicolumn{3}{c|}{连铸} \\ \cline{3-11}
                    &                     & 设备     & 开始     & 结束    & 设备     & 开始     & 结束    & 设备     & 开始     & 结束    \\ \hline
\endhead
%''')
print('\multirow{6}{*}{1}  & 1                   & LD'+str(OPS[0][0][0].eq_num)+'    & '+str(OPS[0][0][0].sta)+'    & '+str(OPS[0][0][0].end)+'   & RH'+str(OPS[0][0][1].eq_num)+'    & '+str(OPS[0][0][1].sta)+'    & '+str(OPS[0][0][1].end)+'   & CC'+str(OPS[0][0][2].eq_num)+'    & '+str(OPS[0][0][2].sta)+'    & '+str(OPS[0][0][2].end)+'   \\\ \cline{2-11}')
print('                    & 2                   & LD'+str(OPS[0][1][0].eq_num)+'    & '+str(OPS[0][1][0].sta)+'    & '+str(OPS[0][1][0].end)+'   & RH'+str(OPS[0][1][1].eq_num)+'    & '+str(OPS[0][1][1].sta)+'    & '+str(OPS[0][1][1].end)+'   & CC'+str(OPS[0][1][2].eq_num)+'    & '+str(OPS[0][1][2].sta)+'    & '+str(OPS[0][1][2].end)+'   \\\ \cline{2-11}')
print('                    & 3                   & LD'+str(OPS[0][2][0].eq_num)+'    & '+str(OPS[0][2][0].sta)+'    & '+str(OPS[0][2][0].end)+'   & RH'+str(OPS[0][2][1].eq_num)+'    & '+str(OPS[0][2][1].sta)+'    & '+str(OPS[0][2][1].end)+'   & CC'+str(OPS[0][2][2].eq_num)+'    & '+str(OPS[0][2][2].sta)+'    & '+str(OPS[0][2][2].end)+'   \\\ \cline{2-11}')
print('                    & 4                   & LD'+str(OPS[0][3][0].eq_num)+'    & '+str(OPS[0][3][0].sta)+'    & '+str(OPS[0][3][0].end)+'   & RH'+str(OPS[0][3][1].eq_num)+'    & '+str(OPS[0][3][1].sta)+'    & '+str(OPS[0][3][1].end)+'   & CC'+str(OPS[0][3][2].eq_num)+'    & '+str(OPS[0][3][2].sta)+'    & '+str(OPS[0][3][2].end)+'   \\\ \cline{2-11}')
print('                    & 5                   & LD'+str(OPS[0][4][0].eq_num)+'    & '+str(OPS[0][4][0].sta)+'    & '+str(OPS[0][4][0].end)+'   & RH'+str(OPS[0][4][1].eq_num)+'    & '+str(OPS[0][4][1].sta)+'    & '+str(OPS[0][4][1].end)+'   & CC'+str(OPS[0][4][2].eq_num)+'    & '+str(OPS[0][4][2].sta)+'    & '+str(OPS[0][4][2].end)+'   \\\ \cline{2-11}')
print('                    & 6                   & LD'+str(OPS[0][5][0].eq_num)+'    & '+str(OPS[0][5][0].sta)+'    & '+str(OPS[0][5][0].end)+'   & RH'+str(OPS[0][5][1].eq_num)+'    & '+str(OPS[0][5][1].sta)+'    & '+str(OPS[0][5][1].end)+'   & CC'+str(OPS[0][5][2].eq_num)+'    & '+str(OPS[0][5][2].sta)+'    & '+str(OPS[0][5][2].end)+'   \\\ \hline')
print('\multirow{6}{*}{2}  & 1                   & LD'+str(OPS[1][0][0].eq_num)+'    & '+str(OPS[1][0][0].sta)+'    & '+str(OPS[1][0][0].end)+'   & RH'+str(OPS[1][0][1].eq_num)+'    & '+str(OPS[1][0][1].sta)+'    & '+str(OPS[1][0][1].end)+'   & CC'+str(OPS[1][0][2].eq_num)+'    & '+str(OPS[1][0][2].sta)+'    & '+str(OPS[1][0][2].end)+'   \\\ \cline{2-11}')
print('                    & 2                   & LD'+str(OPS[1][1][0].eq_num)+'    & '+str(OPS[1][1][0].sta)+'    & '+str(OPS[1][1][0].end)+'   & RH'+str(OPS[1][1][1].eq_num)+'    & '+str(OPS[1][1][1].sta)+'    & '+str(OPS[1][1][1].end)+'   & CC'+str(OPS[1][1][2].eq_num)+'    & '+str(OPS[1][1][2].sta)+'    & '+str(OPS[1][1][2].end)+'   \\\ \cline{2-11}')
print('                    & 3                   & LD'+str(OPS[1][2][0].eq_num)+'    & '+str(OPS[1][2][0].sta)+'    & '+str(OPS[1][2][0].end)+'   & RH'+str(OPS[1][2][1].eq_num)+'    & '+str(OPS[1][2][1].sta)+'    & '+str(OPS[1][2][1].end)+'   & CC'+str(OPS[1][2][2].eq_num)+'    & '+str(OPS[1][2][2].sta)+'    & '+str(OPS[1][2][2].end)+'   \\\ \cline{2-11}')
print('                    & 4                   & LD'+str(OPS[1][3][0].eq_num)+'    & '+str(OPS[1][3][0].sta)+'    & '+str(OPS[1][3][0].end)+'   & RH'+str(OPS[1][3][1].eq_num)+'    & '+str(OPS[1][3][1].sta)+'    & '+str(OPS[1][3][1].end)+'   & CC'+str(OPS[1][3][2].eq_num)+'    & '+str(OPS[1][3][2].sta)+'    & '+str(OPS[1][3][2].end)+'   \\\ \cline{2-11}')
print('                    & 5                   & LD'+str(OPS[1][4][0].eq_num)+'    & '+str(OPS[1][4][0].sta)+'    & '+str(OPS[1][4][0].end)+'   & RH'+str(OPS[1][4][1].eq_num)+'    & '+str(OPS[1][4][1].sta)+'    & '+str(OPS[1][4][1].end)+'   & CC'+str(OPS[1][4][2].eq_num)+'    & '+str(OPS[1][4][2].sta)+'    & '+str(OPS[1][4][2].end)+'   \\\ \cline{2-11}')
print('                    & 6                   & LD'+str(OPS[1][5][0].eq_num)+'    & '+str(OPS[1][5][0].sta)+'    & '+str(OPS[1][5][0].end)+'   & RH'+str(OPS[1][5][1].eq_num)+'    & '+str(OPS[1][5][1].sta)+'    & '+str(OPS[1][5][1].end)+'   & CC'+str(OPS[1][5][2].eq_num)+'    & '+str(OPS[1][5][2].sta)+'    & '+str(OPS[1][5][2].end)+'   \\\ \hline')
print('\multirow{6}{*}{3}  & 1                   & LD'+str(OPS[2][0][0].eq_num)+'    & '+str(OPS[2][0][0].sta)+'    & '+str(OPS[2][0][0].end)+'   & RH'+str(OPS[2][0][1].eq_num)+'    & '+str(OPS[2][0][1].sta)+'    & '+str(OPS[2][0][1].end)+'   & CC'+str(OPS[2][0][2].eq_num)+'    & '+str(OPS[2][0][2].sta)+'    & '+str(OPS[2][0][2].end)+'   \\\ \cline{2-11}')
print('                    & 2                   & LD'+str(OPS[2][1][0].eq_num)+'    & '+str(OPS[2][1][0].sta)+'    & '+str(OPS[2][1][0].end)+'   & RH'+str(OPS[2][1][1].eq_num)+'    & '+str(OPS[2][1][1].sta)+'    & '+str(OPS[2][1][1].end)+'   & CC'+str(OPS[2][1][2].eq_num)+'    & '+str(OPS[2][1][2].sta)+'    & '+str(OPS[2][1][2].end)+'   \\\ \cline{2-11}')
print('                    & 3                   & LD'+str(OPS[2][2][0].eq_num)+'    & '+str(OPS[2][2][0].sta)+'    & '+str(OPS[2][2][0].end)+'   & RH'+str(OPS[2][2][1].eq_num)+'    & '+str(OPS[2][2][1].sta)+'    & '+str(OPS[2][2][1].end)+'   & CC'+str(OPS[2][2][2].eq_num)+'    & '+str(OPS[2][2][2].sta)+'    & '+str(OPS[2][2][2].end)+'   \\\ \cline{2-11}')
print('                    & 4                   & LD'+str(OPS[2][3][0].eq_num)+'    & '+str(OPS[2][3][0].sta)+'    & '+str(OPS[2][3][0].end)+'   & RH'+str(OPS[2][3][1].eq_num)+'    & '+str(OPS[2][3][1].sta)+'    & '+str(OPS[2][3][1].end)+'   & CC'+str(OPS[2][3][2].eq_num)+'    & '+str(OPS[2][3][2].sta)+'    & '+str(OPS[2][3][2].end)+'   \\\ \cline{2-11}')
print('                    & 5                   & LD'+str(OPS[2][4][0].eq_num)+'    & '+str(OPS[2][4][0].sta)+'    & '+str(OPS[2][4][0].end)+'   & RH'+str(OPS[2][4][1].eq_num)+'    & '+str(OPS[2][4][1].sta)+'    & '+str(OPS[2][4][1].end)+'   & CC'+str(OPS[2][4][2].eq_num)+'    & '+str(OPS[2][4][2].sta)+'    & '+str(OPS[2][4][2].end)+'   \\\ \cline{2-11}')
print('                    & 6                   & LD'+str(OPS[2][5][0].eq_num)+'    & '+str(OPS[2][5][0].sta)+'    & '+str(OPS[2][5][0].end)+'   & RH'+str(OPS[2][5][1].eq_num)+'    & '+str(OPS[2][5][1].sta)+'    & '+str(OPS[2][5][1].end)+'   & CC'+str(OPS[2][5][2].eq_num)+'    & '+str(OPS[2][5][2].sta)+'    & '+str(OPS[2][5][2].end)+'   \\\ \hline')
print('\end{longtable}')

while 1:
    plt.pause(1)
