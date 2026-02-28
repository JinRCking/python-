import random

def monty_hall(simulations):
    change_win_count = 0
    keep_win_count = 0

    for _ in range(simulations):
        doors = [0, 0, 1]  # 0 表示山羊，1 表示汽车
        random.shuffle(doors)  # 打乱门的顺序

        # 参赛者随机选择一扇门
        selected_door_index = random.randint(0, 2)

        # 主持人打开一扇有山羊的门
        for i, door in enumerate(doors):
            if i != selected_door_index and door == 0:
                # 只有在当前选的门不是汽车且不是参赛者选的门时，主持人才会打开
                doors[i] = -1  # -1 表示已经打开
                break

        # 如果参赛者改变选择
        for i, door in enumerate(doors):
            if i != selected_door_index and door != -1:
                # 改变选择到剩下的门上
                selected_door_index = i
                break

        # 判断是否获胜
        if doors[selected_door_index] == 1:  # 如果选中的门是汽车
            change_win_count += 1
        else:
            keep_win_count += 1

    # 计算获胜的概率
    change_win_probability = change_win_count / simulations
    keep_win_probability = keep_win_count / simulations

    return change_win_probability, keep_win_probability

# 模拟100000次
simulations = 100000
change_win_probability, keep_win_probability = monty_hall(simulations)

print("参赛者改变选择获胜的概率：", change_win_probability)
print("参赛者坚持选择获胜的概率：", keep_win_probability)
