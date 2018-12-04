def tracking(filename):
    local_track_dump = []
    local_track_dir = {}
    with open(filename) as tracks:
        local_track_dump = tracks.readlines()

    print("file contains %i lines" % len(local_track_dump))

    for i in range(1, len(local_track_dump)):
        ID = local_track_dump[i].strip("\n").split(",")[2]
        PosX = float(local_track_dump[i].strip("\n").split(",")[4])
        PosY = float(local_track_dump[i].strip("\n").split(",")[5])
        PosZ = local_track_dump[i].strip("\n").split(",")[6]
        PosT = int(local_track_dump[i].strip("\n").split(",")[7])

        if not ID in local_track_dir:
            local_track_dir[ID] = [[PosX, PosY, PosZ, PosT]]
        else:
            local_track_dir[ID].append([PosX, PosY, PosZ, PosT])

    return (local_track_dir)
