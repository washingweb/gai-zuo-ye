'''
pull user git
'''

import os

USER_TABLE = [
    [51, 'brightq', '齐明'],
    [52, 'Congying1112', '王聪颖'],
    [53, 'BillyQin', '覃昶栋'],
    [54, 'yangfan1992', '陈扬帆'],
    [56, 'public2018', '杨柳雨'],
    [58, 'dangfp', '党飞鹏'],
    [59, 'Jchen666', '陈俊杰'],
    [60, 'jinzhao672', '金昭'],
]

def shell(cmd):
    os.system(cmd)
    # print(cmd)

def init(id, git_name, user_name):
    shell('mkdir {}'.format(id))
    shell('cd {} && git clone https://github.com/{}/guigulive-operation.git'.format(id, git_name))

def update(id, git_name, user_name):
    shell('cd {}/guigulive-operation && git pull'.format(id))

for user_info in USER_TABLE:
    init(*user_info)
    update(*user_info)
