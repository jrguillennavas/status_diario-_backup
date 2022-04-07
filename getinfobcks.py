import os
from datetime import datetime


def getRutes(path_bck, dir = ''):
    data= []
    if dir.endswith('zip') or dir.startswith('zi') or dir.endswith('bat'):
        return [path_bck]

    if os.path.isdir(path_bck):
        path_dir = f'{path_bck}/{dir}'
        for dir1 in os.listdir(path_dir):
            data += getRutes(path_dir, dir1)
    return data

def info_backup(path_bck):
    routes = set(getRutes(path_bck))
    data = []
    for route in routes:
        exists = False
        split_route = route.replace('//', ' ').replace('/', ' ').lstrip().split(' ')
        for file in os.listdir(route):
            route_file = f'{route}/{file}'
            if datetime.fromtimestamp(os.path.getatime(route_file)).strftime(f'%Y%m%d') == datetime.now().date().strftime(f'%Y%m%d'):
                exists = True
                data += [{'backup': True, 'su':f'{split_route[-1] if split_route[-2] == "Backup" else split_route[-2]}'.upper(), 'folder': f'{split_route[-1]}', 'name': f'{file}', 'size': f'{round(os.path.getsize(route_file) / 1024**3)}GB', 'date': f'{datetime.fromtimestamp(os.path.getatime(route_file))}'} if len(split_route) > 3 else {'backup': True, 'su':f'{split_route[-2]}', 'folder': f'{split_route[-1]}', 'name': f'{file}', 'size': f'{round(os.path.getsize(route_file) / 1024**3)}GB', 'date': f'{datetime.fromtimestamp(os.path.getatime(route_file))}'}]
            
        if not exists and len(split_route) > 3:
            data += [{'backup': False, 'su':f'{split_route[-2]}'.upper(), 'folder': f'{split_route[-1]}', 'name': 'Fallo', 'size': '0GB', 'date': f'{ datetime.now()}'}]
        elif not exists and len(split_route) <= 3:
            data += [{'backup': False, 'su':f'{split_route[-1]}'.upper(), 'folder': '', 'name': f'{file}', 'size': f'{round(os.path.getsize(route_file) / 1024**3)}GB', 'date': f'{ datetime.now()}'}]
    return data  
