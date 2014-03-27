def tramping(payment):
    if payment >= 50:
        payment_is_sufficient = True
    else:
        payment_is_sufficient = False
    if payment_is_sufficient or not payment_is_sufficient:
        return "{}".format("We're going tramping")
        