# If statement

is_msian = True
is_cute = False

if is_msian and is_cute:
    print("You are a cute Malaysian.")
elif is_msian and not(is_cute):
    print("You are not a cute Malaysian.")
elif not(is_msian) and is_cute:
    print("You are a cute non-Malaysian.")
else:
    print("You are neither cute nor a Malaysian.")