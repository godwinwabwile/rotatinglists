

def rotatelist(nlist, K):
    '''function takes list and a rotation value and returns a rotated list'''
    if K>0 and K<len(nlist):
        listlen = len(nlist)-K
        newlist = nlist[listlen:]
        slicedlist= nlist[:listlen]
        rotated = newlist  + slicedlist

        return rotated 

    


