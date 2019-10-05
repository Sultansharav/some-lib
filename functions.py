def hamgiinUrt(n): #n list
    k=0
    for i in n:
        if len(i)>k:
            k=len(i)
            urt_ner = i
    return urt_ner

def hamgiinBogino(n):
    k=30
    for i in n:
        if len(i) < k:
            k = len(i)
            bogino_ner = i
    return bogino_ner