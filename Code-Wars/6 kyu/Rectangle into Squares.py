def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    result = []
    while lng != wdth:
        if lng < wdth:
            lng, wdth = wdth, lng
        result.append(wdth)
        lng, wdth = wdth, lng - wdth
    return result + [wdth]
