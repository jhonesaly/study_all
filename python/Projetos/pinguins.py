
endgame = False

while endgame == False:
    
    FatherAway = True
    AdultNear = False

    # True & True = True
    # True & False = False
    # False & False = False

    if FatherAway & AdultNear:
        endgame = True
    else:
        continue