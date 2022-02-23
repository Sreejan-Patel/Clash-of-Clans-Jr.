from src.village import Village

village = Village()

while(True):
    key = village.get_key()
    if key == 'q':
        break
    else:
        village.render()
    