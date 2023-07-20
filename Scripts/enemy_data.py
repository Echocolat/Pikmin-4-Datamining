import json

with open('Enemy Data/BaseData.json') as json_file:
    basedata = json.loads(json_file.read())

with open('Enemy Data/GenseiName.json') as json_file:
    genseiname = json.loads(json_file.read())

with open('Enemy Data/GenseiFamilyName.json') as json_file:
    genseifamilyname = json.loads(json_file.read())

with open('Enemy Data/GenseiScientificName_PictureBook.json') as json_file:
    genseiscientificname = json.loads(json_file.read())

def get_enemy_data():

    data_list = []

    for enemy in genseiname['GenseiName']:
        enemy_dict = {"Internal name": enemy}
        enemy_dict["Name"] = genseiname['GenseiName'][enemy].split(']')[-1]
        enemy_dict['Scientific name'] = genseiscientificname['GenseiScientificName_Picturebook'][enemy.replace('_00', '').replace('_01', '')].split(']')[-1]
        enemy_dict['Family'] = genseifamilyname['GenseiFamilyName'][enemy.replace('_00', '').replace('_01', '')].split(']')[-1]
        try:
            enemy_dict['Weight'] = basedata[0]['Rows'][enemy]['CarryWeightMin']
        except:
            None
        try:
            enemy_dict['MaxLife'] = basedata[0]['Rows'][enemy]['MaxLife']
        except:
            None
        try:
            enemy_dict['Sparklium'] = basedata[0]['Rows'][enemy]['Poko']
        except:
            None
        try:
            enemy_dict['Pikmin Seeds'] = basedata[0]['Rows'][enemy]['Kira']
        except:
            None
        try:
            enemy_dict['Player Damage'] = basedata[0]['Rows'][enemy]['PlayerDamage']
        except:
            None
        try:
            enemy_dict['Other Damage'] = basedata[0]['Rows'][enemy]['OtherDamage']
        except:
            None
        try:
            enemy_dict['Starbit amount'] = basedata[0]['Rows'][enemy]['DropStationPieceNum']
        except:
            None
        data_list.append(enemy_dict)

    return data_list

with open('Ready for spreadsheet/Enemy_data.json', 'w') as json_file:
    json_file.write(json.dumps(get_enemy_data(), indent = 2))
