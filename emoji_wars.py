'''how to use this:

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
'''


'''import section'''
from random import choice

'''class section'''
class rps:
    attacks = []
    char = []
    msy = []
    al = []

'''funtions section'''
def _amm(self):
    
    '''creates a hidden action'''
    
    if not self in rps.msy:
        rps.msy.append(self)
        rps.al.append(self)
def mys():
    
    '''uses the funcion _amm(),
    this creates hidden actions'''
    
    _amm('>:D')
    _cycle(['>:D', rps.al])
    _amm('>:[]')
    _cycle(['>:[]', [':D', 'D:', ':[]']])
    _amm('D:<')
    _cycle([rps.al, 'D:<'])
def check(i):

    '''check if it's a tie or
    an unkown action'''
    
    if i in rps.al:
        return 'tie'
    else:
        return 'cancel'
def ran():

    '''return a random choice of all avalable
    actions, including hidden ones'''
    
    return choice(rps.char)
def _add(self):

    '''creates a normal action'''
    
    if not self in rps.char:
        rps.char.append(self)
        rps.al.append(self)
def _attack(ok, ko):

    '''creates a list of two actions
    beats the other. then add that
    list to a list called rps.attacks'''
    if ok in rps.al or ko in rps.al:
        rps.attacks.append([ok, ko])
def _cycle(ie):

    ''' add a cycle attack (eg. _cycle('sciccors', 'paper', 'rock') =
    scissors beats paper beats rock beats scissors.)'''
    
    if len(ie) == 2:
        if type(ie[0]) == type([]) and type(ie[1]) == type(''):
            for i in ie[0]:
                _attack(i, ie[1])
        elif type(ie[0]) == type('') and type(ie[1]) == type([]):
            for i in ie[1]:
                _attack(i, ie[0])
        elif type(ie[0]) == type('') and type(ie[1]) == type(''):
            _attack(ie[0], ie[1])
        elif type(ie[0]) == type([]) and type(ie[1]) == type([]):
            h = 0
            for i in ie[0]:
                _attack(i, ie[1][h])
                h=+1
    else:
        h = 0
        prev = ''
        for i in range(-1, len(ie), -1):
            if h > 0:
                _attack(ie[i], prev)
            prev = ie[i]
            h=+1
        _attack(ie[len(ie)-1], ie[0])
def cycle(ie):

    '''an advanced version of the _cycle()
    function'''
    
    for i in ie:
        if type(i) == type(''):
            _add(i)
    _cycle(ie)
def run():

    '''runs the whole code'''
    
    for i in rps.char:
        print(i)
    print('?')
    k = input()
    if k == '?':
        k = ran()
    print('you choose:', k)
    oop = ran()
    print(oop)
    io =  ''
    for i in rps.attacks:
        if k in i:
            if k == i[0] and oop == i[1]:
                if io == '':
                    io = 'player win'
            elif oop == i[0] and k == i[1]:
                if io == '':
                    io = 'com win'
            elif k == oop:
                if io == '':
                    io = 'tie'
    if io == '':
        io = check(k)
    print(io)
    if input('again?(y/n)')=='y':
    	run()
def setup():

    '''setups the game'''
    
    cycle([':)', ':(', ':|'])
    cycle([':D', 'D:', ':[]'])
    cycle([':D', ':)'])
    cycle(['D:', ':('])
    cycle([':[]', ':|'])
    cycle([':D', [':)', ':(', ':|']])
    cycle(['D:', [':)', ':(', ':|']])
    cycle([':[]', [':)', ':(', ':|']])
    cycle(['6_6', '>w<', '^_____^'])
    cycle([['6_6', '>w<', '^_____^'], [':[]', ':D', 'D:']])
    cycle(['I_I', 'T_T', 'U_U'])
    cycle(['o_O', 'O:K', ': >'])
    cycle([['o_O', 'O:K', ': >'], ['I_I', 'T_T', 'U_U']])
    cycle([['o_O', 'O:K', ': >'], [':)', ':(', ':|']])
    cycle([['o_O', 'O:K', ': >'], ['6_6', '>w<', '^_____^']])
    cycle(['^o^', 'J_J'])
    cycle([rps.al, 'J_J'])
    cycle([rps.al, '^o^'])
    cycle(['⫕⨟⨞', '∑⫕Ⅾ', 'ↁ⊂⊐⋅⊃'])
    cycle(['⫕⨟⨞', ':)'])
    cycle(['∑⫕Ⅾ', ':('])
    cycle(['ↁ⊂⊐⋅⊃', ':|'])
    cycle([':D', '⫕⨟⨞'])
    cycle(['D:', '∑⫕Ⅾ'])
    cycle([':[]', 'ↁ⊂⊐⋅⊃'])
setup()
mys()
run()
