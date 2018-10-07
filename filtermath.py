from django import template

register = template.Library()


@register.filter(name='intconvertion')
def convert_to_int(number):
    return int(number)


@register.filter(name='floatconvertion')
def convert_to_int(number):
    return float(number)


@register.filter(name='add')
def add(number_one, number_two):
    return number_one + number_two


@register.filter(name='subtract')
def subtract(number_one, number_two):
    return number_one - number_two


@register.filter(name='multiply')
def multiply(number_one, number_two):
    return number_one * number_two


@register.filter(name='divide')
def divide(numerator, denominator):
    return numerator / denominator


# Returns the remainder
@register.filter(name='modulus')
def modulus(numerator, denominator):
    return numerator % denominator


# The base is the large number or the number that is being multiplied lots of times
# The exponent is the small number or the number of times the base is being multiplied
@register.filter(name='exponent')
def power_of(base, exponent):
    return base ** exponent


@register.filter(name='floordivision')
def floor_division(numerator, denominator):
    return numerator // denominator


# This rounds a floating point number to the number of digits you set in the digits
@register.filter(name='round')
def round_num(number, digits):
    return round(number, digits)

