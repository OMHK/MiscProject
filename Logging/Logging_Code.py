import logging as log
log.basicConfig(level = log.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s' )
log.debug('Start of The Program')

def factorial(n):
    log.debug('Start of factorial (%s%%)' % ('n'))
    total = 1
    for i in range(1, n + 1):
        total *= i
        log.debug('i is ' + str(i) + ', total is ' + str(total))
    log.debug('end of factorial (%s%%)' %(n))
    return total
print(factorial(5))
log.debug('End of program')
