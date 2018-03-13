
label init_fighters:
    #    init_fighters acts like a function that initializes fighter objects and their assigned attributes.
    #    Call this label when resetting battle stats back to their defaults.
    $ blackSheep1 = fighter(
        FTR = "Black Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 10,
        SPD = 420,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card ="images/pipo-enemy031.png",            
        pic_sprite =  "blackSheep", #"images/pipo-enemy031.png",   
        sprite_pos = [0.5, 0.5]
        )
    
    $ blackSheep2 = fighter(
        FTR = "Black Sheep 2",
        ALIVE = True,
        ATK = 100,
        DEF = 10,
        SPD = 420,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card ="images/pipo-enemy031.png",            
        pic_sprite =  "creamSheep", #"images/pipo-enemy031.png",   
        sprite_pos = [0.4, 0.5]
        )
    
    $ creamSheep1  = fighter(
        FTR = "Mako",
        ALIVE = True,
        ATK = 100,
        DEF = 10,
        SPD = 420,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card ="images/makoidle.png",            
        pic_sprite =  "makosprite", #"images/pipo-enemy031.png",   
        sprite_pos = [0.6, 0.5]
        )
    
    $ creamSheep2 = fighter(
        FTR = "Sidney",
        ALIVE = True,
        ATK = 100,
        DEF = 10,
        SPD = 420,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card ="images/pipo-enemy031.png",            
        pic_sprite =  "creamSheep", #"images/pipo-enemy031.png",   
        sprite_pos = [0.1, 0.5]
        )
    
    $ pinkSheep1 = fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

    
    $ pinkSheep2 = fighter(
        FTR = "Pink Sheep 2",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite ="pinkSheep",# "images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

    $ pinkSheep3 = fighter(
        FTR = "Pink Sheep 3",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep",#"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )
    
    $ brownBear1 = fighter(
        FTR = "Alfie",
        ALIVE = True,
        ATK = 200,
        DEF = 560,
        SPD = 340,
        MG = 10,
        HP = 420,
        MP = 300,
        ELEM = "Fire",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy037.png",          
        pic_sprite = "brownBear", #"images/pipo-enemy037.png",    
        sprite_pos = [0.1, 0.5]
        )

		
		$ MasterPlan
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ VideoGame
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ HurriedDeadline
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ BigPresentation
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ MegaExam
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ TemptingNotification
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ GossipGlobs
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ DrDoubts
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ GuiltTrip
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ ADistraction
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ Overexcitement
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ Boredom
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ BigNews
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ PuzzlingPattern
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ CreatorsShadow
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ WeatherWoes
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ ReturnedCharacter
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ BasicBrainstorm
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ SadStatue
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ GreedyGetting
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ Darkness
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ ABigMistake
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ BrokenMirror
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ ThePerfectCharacter
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ RuinedRoles
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ PettyJealousAttack
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ MysteryThought
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ TheHappyPolice
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ FearofFear
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ LostJoys
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ InfiniteLoop
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ MrDisappointment
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ OneStepTooFar
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ HiddenTruths
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ ThoughtMismatch
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ Responsibility
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ PayingAttention
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ WeightyExpectations
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ TheUnknown
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ Quiet
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )

$ OminousRock
= fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [HigherAttack],
        pic_card = "images/pipo-enemy031a.png",          
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",    
        sprite_pos = [0.9, 0.5]
        )	