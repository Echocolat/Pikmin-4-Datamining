import json
import os

with open('Ready for spreadsheet\Enemy_data.json') as json_file:
    enemy_data = json.loads(json_file.read())

with open('Ready for spreadsheet\Treasure_data.json') as json_file:
    treasure_data = json.loads(json_file.read())

def get_enemy_locs(area, is_cave = False):

    enemy_locs = []

    try:
        if not is_cave:
            with open(f'Maps/Main/Area/Area{area}/ActorPlacementInfo/AP_Area{area}_P_Teki_Day.json') as json_file:
                enemy_file = json.loads(json_file.read())
            for enemy in enemy_file[0]['Properties']['ActorGeneratorList']:

                if not ('Other' in enemy['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Teki/', '') or 'Placeables' in enemy['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Teki/', '') or 'NightTobiKaburi' in enemy['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Teki/', '')):
                    actor_name = enemy['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Teki/', '').split('.')[0]
                    enemy_number = [enemy_['ActorName'] for enemy_ in enemy_data if 'ActorName' in enemy_].index(actor_name)
                    enemy_dict = {'Internal name': enemy_data[enemy_number]['Internal name'], 'Name': enemy_data[enemy_number]['Name']}
                    enemy_dict['Translate'] = enemy['InitTransform']['Translation']
                    enemy_locs.append(enemy_dict)
        else:
            number_floor = len(os.listdir(f'Maps/Madori/Cave/Cave{area}'))
            
            for floor in range(number_floor):
                floor_str = str(floor).zfill(2)
                try:
                    with open(f'Maps/Madori/Cave/Cave{area}/Cave{area}_F{floor_str}/ActorPlacementInfo/AP_Cave{area}_F{floor_str}_P_Teki.json') as json_file:
                        enemy_file = json.loads(json_file.read())
                        for enemy in enemy_file[0]['Properties']['ActorGeneratorList']:

                            if not ('Other' in enemy['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Teki/', '') or 'Placeables' in enemy['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Teki/', '') or 'NightTobiKaburi' in enemy['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Teki/', '')):
                                actor_name = enemy['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Teki/', '').split('.')[0]
                                enemy_number = [enemy_['ActorName'] for enemy_ in enemy_data if 'ActorName' in enemy_].index(actor_name)
                                enemy_dict = {'Internal name': enemy_data[enemy_number]['Internal name'], 'Name': enemy_data[enemy_number]['Name']}
                                enemy_dict['Floor'] = floor
                                enemy_dict['Translate'] = enemy['InitTransform']['Translation']
                                enemy_locs.append(enemy_dict)
                except:
                    None

    except:
        None
        
    if not is_cave:
        os.makedirs(f'Map Info/Main/Area/Area{area}', exist_ok = True)
        with open(f'Map Info/Main/Area/Area{area}/Area{area}_Enemies.json', 'w') as json_file:
            json_file.write(json.dumps(enemy_locs, indent = 2))

    else:
        os.makedirs(f'Map Info/Madori/Cave/Cave{area}', exist_ok = True)
        with open(f'Map Info/Madori/Cave/Cave{area}/Cave{area}_Enemies.json', 'w') as json_file:
            json_file.write(json.dumps(enemy_locs, indent = 2))

def get_treasure_locs(area, is_cave = False):

    treasure_locs = []

    try:
        if not is_cave:
            with open(f'Maps/Main/Area/Area{area}/ActorPlacementInfo/AP_Area{area}_P_Objects_Day.json') as json_file:
                treasure_file = json.loads(json_file.read())
            for object in treasure_file[0]['Properties']['ActorGeneratorList']:

                if 'Game/Carrot4/Placeables/Objects/Otakara' in object['SoftRefActorClass']['AssetPathName']:
                    actor_name = object['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Objects/Otakara/', '').split('.')[0]
                    treasure_number = [treasure_['ActorName'] for treasure_ in treasure_data if 'ActorName' in treasure_].index(actor_name)
                    treasure_dict = {'Internal name': treasure_data[treasure_number]['Internal name'], 'Name': treasure_data[treasure_number]['Name']}
                    treasure_dict['Translate'] = object['InitTransform']['Translation']
                    treasure_locs.append(treasure_dict)
        else:
            number_floor = len(os.listdir(f'Maps/Madori/Cave/Cave{area}'))
            
            for floor in range(number_floor):
                floor_str = str(floor).zfill(2)
                try:
                    with open(f'Maps/Madori/Cave/Cave{area}/Cave{area}_F{floor_str}/ActorPlacementInfo/AP_Cave{area}_F{floor_str}_P_Objects.json') as json_file:
                        treasure_file = json.loads(json_file.read())
                        for object in treasure_file[0]['Properties']['ActorGeneratorList']:

                            if 'Game/Carrot4/Placeables/Objects/Otakara' in object['SoftRefActorClass']['AssetPathName']:
                                actor_name = object['SoftRefActorClass']['AssetPathName'].replace('/Game/Carrot4/Placeables/Objects/Otakara/', '').split('.')[0]
                                treasure_number = [treasure_['ActorName'] for treasure_ in treasure_data if 'ActorName' in treasure_].index(actor_name)
                                treasure_dict = {'Internal name': treasure_data[treasure_number]['Internal name'], 'Name': treasure_data[treasure_number]['Name']}
                                treasure_dict['Floor'] = floor
                                treasure_dict['Translate'] = object['InitTransform']['Translation']
                                treasure_locs.append(treasure_dict)
                except:
                    None

    except:
        None
        
    if not is_cave:
        os.makedirs(f'Map Info/Main/Area/Area{area}', exist_ok = True)
        with open(f'Map Info/Main/Area/Area{area}/Area{area}_Treasures.json', 'w') as json_file:
            json_file.write(json.dumps(treasure_locs, indent = 2))

    else:
        os.makedirs(f'Map Info/Madori/Cave/Cave{area}', exist_ok = True)
        with open(f'Map Info/Madori/Cave/Cave{area}/Cave{area}_Treasures.json', 'w') as json_file:
            json_file.write(json.dumps(treasure_locs, indent = 2))

def main():

    for area in ['001', '002', '003', '004', '006', '010', '011', '500']:
        get_enemy_locs(area)
        get_treasure_locs(area)
        print(f'Proceeded area {area}')

    for cave in ['00' + str(i) for i in range(1, 10)] + ['0' + str(i) for i in range(10, 36)]:
        get_enemy_locs(cave, is_cave = True)
        get_treasure_locs(cave, is_cave = True)
        print(f'Proceeded cave {cave}')

if __name__ == '__main__':
    main()