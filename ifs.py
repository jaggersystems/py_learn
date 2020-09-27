
is_male = False
is_tall = False

#if is_male or is_tall:

if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not (is_tall):
    print("You are male and not tall")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")

