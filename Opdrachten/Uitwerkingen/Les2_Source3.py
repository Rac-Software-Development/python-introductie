containers_unloaded = 331
unload_time = 441
containers_loaded = 287
load_time = 295

average_unload_time = unload_time / containers_unloaded
average_load_time = load_time / containers_loaded

print(f'De gemiddelde lostijd bedraagt {average_unload_time} minuten per container')
print(f'De gemiddelde laadtijd bedraagt {average_load_time} minuten per container')


