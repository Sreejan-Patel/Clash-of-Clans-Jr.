from src.village import Village

village = Village()

while(True):
    key = village.get_key()
    if key == 'q':
        break
    elif village.game_result == 0:
        village.render()
    else:
        break
    