def is_leap(year):
    # Verifica as condições para ser um ano bissexto
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input())
print(is_leap(year))