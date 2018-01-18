# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    
    call areawarp

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

label areawarp:
    
    scene bg black
    
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