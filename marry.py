import random

boys=['ali','raza','yasin','benyamin','mehrdad','sajjad','aidin','shahin']
girls=['sara','zari','neda','homa','eli','goli','mary','mina']


marry=[]

for i in range(len(boys)):
    if len(girls)==0:
        break
    girl=random.choice(girls)
    boy=random.choice(boys)
    girls.remove(girl)
    boys.remove(boy)
    m=[boy,girl]
    marry.append(m)


print('husband and wife: ',marry)