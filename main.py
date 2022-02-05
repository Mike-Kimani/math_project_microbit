sum2 = 0


def on_forever():
    global sum2
    basic.show_number(3)
    music.start_melody(music.built_in_melody(Melodies.DADADADUM),
        MelodyOptions.ONCE)
    basic.show_number(2)
    basic.pause(5000)
    sum2 = 3 + 2
    basic.show_number(sum2)
basic.forever(on_forever)
