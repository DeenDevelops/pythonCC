def make_album(artistName, albumTitle, songNumber = None):
    albumDict = {'name': artistName, 'album': albumTitle}
    if songNumber:
        albumDict['songs'] = songNumber 
    return albumDict

album = make_album('Fleetwood Mac', 'Rumours', 11)
album2 = make_album('Thriller', 'Michael Jackson', 30)
album3 = make_album('Abbey Road', 'The Beatles')
print(album)
print(album2)
print(album3)