#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
#Bob answers 'Sure.' if you ask him a question.

# He answers 'Whoa, chill out!' if you yell at him.

# He says 'Fine. Be that way!' if you address him without actually saying
# anything.

# He answers 'Whatever.' to anything else.

    what = what.strip()
    if not what:
        return "Fine. Be that way!"
    elif what.isupper():
        return "Whoa, chill out!"
    elif what[-1] == "?":
        return "Sure."
    else:
        return "Whatever."

    # what = what.strip()
    # if not what:
    #     return "Fine. Be that way!"
    # elif what.isupper():
    #     return "Whoa, chill out!"
    # elif what.endswith('?'):
    #     return "Sure."
    # return "Whatever."


