'''
pull user git
'''

import os

USER_TABLE = [
    [21, 'baamax', '白君'],
    [22, 'Satoshi-Kusumoto', '吴逸飞'],
    [23, 'enwang', '王恩临'],
    [24, '1Promise', '秦翀'],
    [25, 'smart-hash', '廖祜秋'],
    [26, 'Antipas', '李轶男'],
    [27, 'FENGXIANGLI', '李丰翔'],
    [28, 'xcyivan', '夏车韵'],
    [29, 'liucc1986', '刘金伟'],
    [30, 'hellodian', 'hellodian'],
]

def shell(cmd):
    os.system(cmd)
    # print(cmd)

def init(id, git_name, user_name):
    shell('mkdir {}'.format(id))
    shell('cd {} && git clone https://github.com/{}/Team-C.git'.format(id, git_name))

def update(id, git_name, user_name):
    shell('cd {}/guigulive-operation && git pull'.format(id))

for user_info in USER_TABLE:
    init(*user_info)
    # update(*user_info)
