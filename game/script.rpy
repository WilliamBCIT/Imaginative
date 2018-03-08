# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alfie")
define s = Character("Sidney")
define m = Character("Mako")

define j = Character("Julie")
define p = Character("Preston")
define mo = Character("Monique")

define lt = Character("Lost Toy")
define cr = Character("The Critic")
define nqa = Character("Not-Quite Alive")

define x = Character("Xavier")
define f = Character("Frida")
define z = Character("Zack")
define r = Character("Raymond")
define e = Character("Ernie")
define q = Character("Quincy")
define mi = Character("Mick")
define h = Character("Hugh")
define n = Character("Norman")
define sh = Character("Shauna")
define l = Character("Lulu")
define ne = Character("Nelly")
define em = Character("Emilia")
define sa = Character("Sarah")
define fi = Character("Filbert")
define c = Character("Cynthia")
define z = Character("Zoe")
define mor = Character("Morgan")
define ro = Character("Rosanne")
define b = Character("Brad")
define bri = Character("Bridgette")

define profw = Character("Professor Williams")
define profh = Character("Professor Hastings")
define proff = Character("Professor Fish")
define profl = Character("Professor Li")
define profc = Character("Professor Conrad")

define k = Character("Karen")
define mm = Character("Monique's Mother")


image bg forest = "images/pipo-battlebg002.jpg"
image blackSheep ="images/pipo-enemy031b.png"
image creamSheep = "images/pipo-enemy031.png"
image pinkSheep = "images/pipo-enemy031a.png"
image brownBear = "images/pipo-enemy037.png"

image makosprite = "images/makoidle.png"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black
    
    call dpdemo
    
    call test
    
    mo "It's only {color=#0000ffff}5 more days{/color} before my group project for business class is due! What a complete nightmare!"

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    
    call testmenu

    "Hello, world."

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
    
label testmenu:
    
    scene black
    
    menu:
        
        "Area Selection":
            call areawarp
            
        "Cutscene Test":
            return
            
        "Battle Test":
            return
        
        "Test In-Game Menus":
            return
            
        "Event Flags":
            return
            
        "Player Statistics":
            return

label areawarp:
    
    scene black
    
    menu:
        
        "University":
            call unistart
            
        "City Plaza":
            call plazastart
            
        "Downtown":
            call dtstart
            
        "Office Tower":
            call otstart
            
        "Cheerful Neighbourhood":
            call cheerstart
            
        "Post Office":
            call poststart
        
        "Community Centre":
            call centrestart
            
        "Seaside Park":
            call parkstart
            
        "Dark Woods":
            call darkstart
        
        "Highway":
            call highwaystart
            
        "Northern Mines":
            call nmstart
            
        "Old Fort":
            call fortstart
            
        "Winter Town":
            call winterstart
        
        "Select an area to visit it."
            
            
label unistart:
    
label plazastart:

label dtstart:

label otstart:
    
label cheerstart:
    
label poststart:
    
label centrestart:
    
label parkstart:
    
label darkstart:
    
label highwaystart:
    
label nmstart:
    
label fortstart:
    
label winterstart: