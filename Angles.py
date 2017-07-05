import math


def checkio(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return [0, 0, 0]
    result = []
    try:
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    except:
        return [0, 0, 0]
        quit()

    sinalfa = 2 * S / (a * b)
    sinbeta = 2 * S / (b * c)
    singamma = 2 * S / (a * c)

    alfa = math.asin(sinalfa)
    beta = math.asin(sinbeta)
    gamma = math.asin(singamma)

    # alfa=round(math.degrees(alfa))  #math.ceil
    beta = round(math.degrees(beta))
    gamma = round(math.degrees(gamma))
    alfa = 180 - (gamma + beta)

    result = [alfa, beta, gamma]
    result.sort()

    print(alfa, beta, gamma)
    # print (result)
    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    assert checkio(11, 20, 30) == [11, 20, 149], " "
