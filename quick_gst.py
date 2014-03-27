def gst(amount):
    gst = (amount * 3) / 23
    return ("Amount: {0:3.2f}\n Gst: {1:6.2f}\n Excl: {2:5.2f}".format(amount, gst, amount - gst))

