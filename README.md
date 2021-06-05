# emoji-wars
play with a computer!
my first readME

how to use this:
    actions:
        they are elements for you to
        beat your opponent.
        make sure you know their weakness.
    hidden actions:
        they are like actions
        but OP.
        and you can't just choose them.
        you can only access them
        using the "?" option.
        unfortunately, the "?" char
        picks all actions and hidden actions,
        even weak ones.
        but sometimes, there are really, really weak hidden actions.
        so, be careful.
    cycles:
        this function
        is special.
        instead of making one action/hidden action
        attack the other, cycle() can make
        multi-attacks.
        example:
            cycle(['scissors', 'paper', 'rock'])
            = scissors beats paper beats rock beats scissors.
        but if the cycle list contains
        list(s):
            cycle([['scissors', 'paper', 'rock'], 'water'])
            = 'scissors', 'paper' and 'rock' all can beat water.
            or
            cycle(['water', ['scissors', 'paper', 'rock']])
            = water can beat 'scissors', 'paper' and 'rock'
            or
            
            cycle([['water', 'ocean', 'waves'], ['scissors', 'paper', 'rock']])
            = water beats scissors
            = ocean beats paper
            = waves beats rock
    attack list:
        when the function cycle is used, it has called the funcion
        attack().
        but it does't just
        attack the other.
        it has SET the attack.
        example:
            attack(water, paper)
        this adds a list of water beats paper
        in the list rps.attacks.
        the list looks a bit like this:
            ['water', 'paper']
        then it adds this list
        to the list rps.attacks (once).
        
    running the game:
        when the attacks is set,
        what do you do with it?
        ah, this is when the checking comes in.
        when the player and the com
        has choose they're actions,
        the com checks the two
        actions, checking if there's a set of action
        like that.
        example:
            player = 'water'
            com = 'paper'
            com : now it is time to check it.
            rps.attacks = [['water', 'paper'], ['waves', 'rock']]
            com : ah, i found it.
            ['water', 'paper']
            = water beats paper
            com : looks like player win
        but when the player is
        the same as the com,
        example:
            player = 'water'
            com = 'water'
            com : now it is time to check it.
            player == com = True
            com : looks like it's a tie.
        see, it becomes a tie.
        but when the player types nonsense,
        example:
            player = 'ygbybgujh'
            com = 'paper'
            com : now it is time to check it.
            com : what is the player typing?
            com : looks like it's a cancel.
