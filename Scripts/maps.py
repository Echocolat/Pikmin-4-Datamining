import json
import os

with open('Ready for spreadsheet\Enemy_data.json') as json_file:
    enemy_data = json.loads(json_file.read())

with open('Ready for spreadsheet\Treasure_data.json') as json_file:
    treasure_data = json.loads(json_file.read())

def get_enemy_locs(area, folder):

    enemy_locs = []

    try:
        with open(f'Maps/{area}_P_Teki_Day.json') as json_file:
            enemy_file = json.loads(json_file.read())

        for enemy in enemy_file[0]['Properties']['ActorGeneratorList']:

            if not ('Other' in enemy['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Teki/', '') or 'Placeables' in enemy['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Teki/', '') or 'NightTobiKaburi' in enemy['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Teki/', '')):
                actor_name = enemy['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Teki/', '').split('.')[0]
                enemy_number = [enemy_['ActorName'] for enemy_ in enemy_data if 'ActorName' in enemy_].index(actor_name)
                enemy_dict = {'Internal name': enemy_data[enemy_number]['Internal name'], 'Name': enemy_data[enemy_number]['Name']}
                enemy_dict['Translate'] = enemy['InitTransform']['Translation']
                enemy_locs.append(enemy_dict)

    except:
        None
    
    folder_path = os.makedirs(f'Map Info/{folder}', exist_ok=True)

    with open(f'Map info/{area}_Day_Enemies.json', 'w') as json_file:
        json_file.write(json.dumps(enemy_locs, indent = 2))

def get_treasure_locs(area, folder):

    treasure_locs = []

    try:
        with open(f'Maps/{area}_P_Objects_Day.json') as json_file:
            treasure_file = json.loads(json_file.read())

        for object in treasure_file[0]['Properties']['ActorGeneratorList']:

            if 'Game/Carrot4/Placeables/Objects/Otakara' in object['SoftRefActorClass']['AssetPathName']:
                actor_name = object['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Objects/Otakara/', '').split('.')[0]
                treasure_number = [treasure_['ActorName'] for treasure_ in treasure_data if 'ActorName' in treasure_].index(actor_name)
                treasure_dict = {'Internal name': treasure_data[treasure_number]['Internal name'], 'Name': treasure_data[treasure_number]['Name']}
                treasure_dict['Translate'] = object['InitTransform']['Translation']
                treasure_locs.append(treasure_dict)

    except:
        None

    folder_path = os.makedirs(f'Map Info/{folder}', exist_ok = True)

    with open(f'Map info/{area}_Day_Treasures.json', 'w') as json_file:
        json_file.write(json.dumps(treasure_locs, indent = 2))

for area in ['001', '002', '003', '004', '006', '010', '011', '500']:
    get_enemy_locs(f'Main/Area/Area{area}/ActorPlacementInfo/AP_Area{area}', f'Main/Area/Area{area}/ActorPlacementInfo')
    get_treasure_locs(f'Main/Area/Area{area}/ActorPlacementInfo/AP_Area{area}', f'Main/Area/Area{area}/ActorPlacementInfo')