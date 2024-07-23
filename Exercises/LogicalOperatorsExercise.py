# Check if magician AND expert -> "You are a master magician"

# check if magician but not expert ->  "at least you are getting there"

# if you're not a magician "You need magic powers"

is_magician = True
is_expert = False


def determineAbility():
    global is_magician
    global is_expert
    if is_magician and is_expert:
        print("YOU, are a master magician")
    elif is_magician and not is_expert:
        print("At least you are getting there")
    else:
        print("You need magic powers")

if __name__ == "__main__":
    determineAbility()