def in_trouble(j_angry, s_angry):
    if j_angry and s_angry:
        # Both are angry
        return True
    elif not j_angry and not s_angry:
        # Neither is angry
        return True
    else:
        # One is angry, the other is not
        return False
print(in_trouble(True, True))    # ➜ True (Both angry)
print(in_trouble(False, False))  # ➜ True (Neither angry)
print(in_trouble(True, False))   # ➜ False (Only John angry)
print(in_trouble(False, True))   # ➜ False (Only Smith angry)
