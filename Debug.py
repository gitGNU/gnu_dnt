def bug(s = "") :
    tmp1 = "Bug hit"
    if s != "" :
	tmp2 = tmp1 + ": " + s
    else :
	tmp2 = tmp1 + "!"

    error(tmp2)
    os._exit(1)
