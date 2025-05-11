# This script is used to format the Json
# path definition

# Character list json need to be modified
Cha_list_js_path = r"Characte_list.json"

# Used to correct character list json
Correct_Night_Order_path = r"Correct_Night_Order.json"

# Read js file like json Fuction， 提取类似 JSON 的对象
def read_js_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
    import json
    data = json.loads(data)
    return data

if __name__ == '__main__':
    Cha_list = read_js_file(Cha_list_js_path)
    print(type(Cha_list))
    #     {
    #     "id": "wudidejiemidashi111",
    #     "image": "https://oss.gstonegames.com/data_file/clocktower/web/icons/puzzlemaster.png",
    #     "edition": "custom",
    #     "name": "解谜大师",
    #     "ability": "一名玩家醉酒，即使你已死亡。每局游戏限一次，你可以猜测谁是那个醉酒的玩家，如果猜对了，你会得知谁是恶魔，但如果猜错了，你会得知错误的“谁是恶魔”信息。",
    #     "team": "outsider",
    #     "sch_team": "外来者",
    #     "firstNight": 0,
    #     "otherNight": 0,
    #     "firstNightReminder": "",
    #     "otherNightReminder": "",
    #     "reminders": [
    #         "醉酒",
    #         "已猜测"
    #     ],
    #     "setup": false
    # },

    Correct_Night_Order = read_js_file(Correct_Night_Order_path)
    print(type(Correct_Night_Order))
    # "thief": {
    #     "id": "thief",
    #     "image": "https://oss.gstonegames.com/data_file/clocktower/web/icons/thief.png",
    #     "edition": "custom",
    #     "name": "窃贼",
    #     "ability": "每个夜晚，你要选择除你以外的一名玩家：明天白天他的投票会被算作负数。",
    #     "team": "traveler",
    #     "firstNight": 1,
    #     "otherNight": 1,
    #     "firstNightReminder": "唤醒窃贼。让窃贼指向任意一名玩家。用窃贼的“负票”提示标记那名被选中的玩家。让窃贼入睡。",
    #     "otherNightReminder": "唤醒窃贼。让窃贼指向任意一名玩家。用窃贼的“负票”提示标记那名被选中的玩家。让窃贼入睡。",
    #     "reminders": [
    #         "负票"
    #     ],
    #     "setup": false
    # },

    Name2EngName = {}
    for key_ in Correct_Night_Order:
        Name2EngName[Correct_Night_Order[key_]['name']] = key_
        # {
        #     k: “厨师”
        #     v: "chef"
        # }
    for item in Cha_list:
        Cha_name = item['name']
    #         {
    #     "id": "daneishiwei111",
    #     "image": "https://oss.gstonegames.com/data_file/clocktower/web/icons/jinyiwei.png",
    #     "edition": "custom",
    #     "name": "锦衣卫",
    #     "ability": "每个夜晚*，你要选择一名玩家：如果他在下个黄昏前死亡，你代替他死亡。",
    #     "team": "townsfolk",
    #     "sch_team": "镇民",
    #     "firstNight": 0,
    #     "otherNight": 13,
    #     "firstNightReminder": "",
    #     "otherNightReminder": "唤醒锦衣卫，让他选择一名玩家。他现在开始保护那名玩家。",
    #     "reminders": [
    #         "保护"
    #     ],
    #     "setup": false
    # },
        Cha_Eng_name = Name2EngName.get(Cha_name, None)
        if Cha_Eng_name:
            Correct_Data = Correct_Night_Order[Cha_Eng_name]
            Correct_firstNight = Correct_Data['firstNight']
            Correct_otherNight = Correct_Data['otherNight']
            item['firstNight'] = Correct_firstNight
            item['otherNight'] = Correct_otherNight
            # modify the json
    
    # Dump a new json file
    import json
    with open(Cha_list_js_path, 'w', encoding='utf-8') as f:
        json.dump(Cha_list, f, ensure_ascii=False, indent=4)
