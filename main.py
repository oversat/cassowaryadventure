def quest1():
    music.play(music.create_song(assets.song("""
            questS1""")),
        music.PlaybackMode.IN_BACKGROUND)
    adventure.add_image_to_text_log(assets.image("""cass0"""))
    adventure.add_to_textlog("You're looking for a Cassowary, a large colorful bird from New Guinea.")
    adventure.add_to_textlog("Press (A) to enter the forests of Northern New Guinea.")
    adventure.add_to_textlog("Press (B) to give up and go home.")
    
    while not (controller.A.is_pressed() or controller.B.is_pressed()):
        pause(100)
    
    if controller.A.is_pressed():
        adventure.add_to_textlog("Fact about New Guinea's cassowary habitats.")
        quest2()
    else:
        adventure.add_to_textlog("You haven't found a cassowary yet!")
        game.over(False)

def quest2():
    music.play(music.create_song(assets.song("""
    questS1""")),
        music.PlaybackMode.IN_BACKGROUND)
    adventure.add_image_to_text_log(assets.image("""
    cass1"""))
    adventure.add_to_textlog("You reach a forest in New Guinea.")
    adventure.add_to_textlog("Press (A) to look left.")
    adventure.add_to_textlog("Press (B) to look right.")
    
    while not (controller.A.is_pressed() or controller.B.is_pressed()):
        pause(100)
    
    if controller.A.is_pressed():
        adventure.add_to_textlog("You found one!")
        quest3()
    else:
        adventure.add_to_textlog("Nothing to see here...")
        quest2()

def quest3():
    music.play(music.create_song(assets.song("""
    questS1""")),
        music.PlaybackMode.IN_BACKGROUND)
    adventure.add_image_to_text_log(assets.image("""
    cass1"""))
    adventure.add_to_textlog("You found the cassowary, what do you do?")
    adventure.add_to_textlog("Press (A) to approach it.")
    adventure.add_to_textlog("Press (B) to note the location for scientists.")
    
    while not (controller.A.is_pressed() or controller.B.is_pressed()):
        pause(100)
    
    if controller.A.is_pressed():
        adventure.add_to_textlog("It makes a scary noise and runs into the forest.")
        quest4()
    else:
        adventure.add_to_textlog("The cassowary's head pops up, and then it retreats into the deep forest.")
        game.over(False)

def quest4():
    music.play(music.create_song(assets.song("""
    questS1""")),
        music.PlaybackMode.IN_BACKGROUND)
    adventure.add_image_to_text_log(assets.image("""
    cass1"""))
    adventure.add_to_textlog("What's one thing you learned about Northern Cassowary?")
    adventure.add_to_textlog("Press (A) if they are from New Guinea.")
    adventure.add_to_textlog("Press (B) if they can fly.")
    
    while not (controller.A.is_pressed() or controller.B.is_pressed()):
        pause(100)
    
    if controller.A.is_pressed():
        adventure.add_to_textlog("They are from New Guinea.")
        game.over(False)
    else:
        adventure.add_to_textlog("They can fly.")
        game.over(True)

quest1()
