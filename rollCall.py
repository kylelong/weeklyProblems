def rollCall(roll):
    return sorted([name[::-1] for name in roll])

assert rollCall(["yzneT","ydissaC","enimA"]) == ["Amine","Cassidy","Tenzy"]
assert rollCall(["rennoD","nexiV","recnarP","temoC","neztilB","recnaD","dipuC","rehsaD","hploduR"]) == ['Blitzen', 'Comet', 'Cupid', 'Dancer', 'Dasher', 'Donner', 'Prancer', 'Rudolph', 'Vixen']
assert rollCall(["A","B","C"]) == ["A","B","C"]