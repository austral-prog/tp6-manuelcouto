def remove_elements(list_to_remove_elements):
    resu=list_to_remove_elements
    if resu==[]:
        resu=[]
    else:
        if len(resu)<5:
            del resu[0]
        elif len(resu)==5:
            del resu[0]
            del resu[3]
        elif len(resu)>=6:
            del resu[0]
            del resu[3]
            del resu[3]
    return resu


def add_elements(list_to_add_elements):
    resu=list_to_add_elements
    resu.insert(0,"Pink")
    resu.insert(len(resu),"Yellow")
    return resu


def is_empty(list_to_check):
    if list_to_check==[]:
        resu=True
    else:
        resu=False
    return resu


def check_lists(list_to_compare1, list_to_compare2):
    l1=list_to_compare1
    l2=list_to_compare2
    resu=True
    if len(l1)<3 or len(l2)<3:
        resu=False
    elif l1[2]==l2[2]:
        resu=True
    else:
        resu=False
    return resu


def list_of_lists(list_of_lists_to_modify):
    resu=list_of_lists_to_modify
    x1=[]
    x2=[]
    x3=[]
    if len(resu[0])<2:
        x1=resu[0][0:]
    else:
        x1=resu[0][0:2]
    if len(resu[1])<2:
        x2=[]
    elif len(resu[1])<4:
        x2=resu[1][1:]
    elif len(resu[1])>=4:
        x2=resu[1][1:4]
    if len(resu[2])<2:
        x3=resu[2][0:]
    else:
        x3=resu[2][-2:]

    resu=[x1,x2,x3]

    return resu
