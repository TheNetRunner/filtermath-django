# filtermath-django
A set of math filters for django's template library

## What is filtermath-django
This is a simple math filter tool I made for django templates at 3am whilest working on a project.

## How to use it
You place the filtermath.py file in your application structure like this:
```
+
+-app/
+--templatetags/ # you will need to make this folder
+--- __init__.py # This is a blank python file that tells python that templatetags is a package
+--- filtermath.py
```
Once you have popped it into your app you will need to restart the django server, if it is running.

Then at the top of your template you can load it like this:
```python
{% load filtermath %}
```

# How Django filters work
*disclaimer*
Below is just a quick summary of how they work as I understand it. 
More and better info can be found [here](https://docs.djangoproject.com/en/2.1/howto/custom-template-tags/)

## What a custom django template filter looks like

```python
register = template.Library()

@register.filter(name='filtername')
def function(value, arg)
return # whatever you like
```

## The break down

```python
# first import the django template library:
register = template.Library()
```
```python
#  Next we register the filter by how we wish for people to refer to it. 
# The @ tells python this is a static method
@register.filter(name='filtername')
```
```python
# now we create a function as normal
def function(value, arg) 
# the value is that which comes before the | in the filter and the arg is what comes after
# i.e value|filter:arg
return 
# here is where you return the magic of your function i.e value * arg or round(value, arg)
```

## Examples of my filters

I have lists a few examples below of my filters below:

{% with number_one=12 number_two=2 %}
    {{ number_one|multiply:number_two %}
{% endwith %}

{% for number in mynumbers %}
    {{ number|add:5 }}
{% endfor %}

{% for number in mynumbers %}
    {{ number|div:2|round:2 }}
{% endfor %}
