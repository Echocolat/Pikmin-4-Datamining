import json

with open('Ready for spreadsheet\Enemy_data.json') as json_file:
    enemy_data = json.loads(json_file.read())

def get_enemy_locs(area):

    with open(f'Maps/Main/Area{area}/AP_Area{area}_P_Teki_Day.json') as json_file:
        enemy_file = json.loads(json_file.read())

    enemy_locs = []

    for enemy in enemy_file[0]['Properties']['ActorGeneratorList']:

        if not 'Egg' in enemy['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Teki/', ''):
            actor_name = enemy['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Teki/', '').split('.')[0]
            enemy_number = [enemy_['ActorName'] for enemy_ in enemy_data if 'ActorName' in enemy_].index(actor_name)
            enemy_dict = {'Internal name': enemy_data[enemy_number]['Internal name'], 'Name': enemy_data[enemy_number]['Name']}
            enemy_dict['Translate'] = enemy['InitTransform']['Translation']
            enemy_locs.append(enemy_dict)

    with open(f'Map info/Main/Area{area}/AP_Area{area}_Day_Enemies.json', 'w') as json_file:
        json_file.write(json.dumps(enemy_locs, indent = 2))

get_enemy_locs('001')