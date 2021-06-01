# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name='Doc', msg="Hello"):
    print(f'{msg}, {name}!')

greet()
greet('Bob', "What's up")

def force(mass,body='earth'): 

    force= mass * round(celestials[body],1)
    print(force)
    
celestials = {'sun': 274,
        'jupiter': 24.92,
        'neptune': 11.15, 
        'saturn': 10.44,
        'earth': 9.798,
        'uranus': 8.87,
        'venus': 8.87,
        'mars': 3.71,
        'mercury': 3.7,
        'moon': 1.62,
        'pluto': 0.58
        }

force(2,"pluto")


def pull(m1,m2,d):
    Gravity = 6.674 * (10**-11)
    pull = Gravity * ((m1*m2)/(d**2))
    return print(round(pull,10))
pull(800,1500,3)






        


