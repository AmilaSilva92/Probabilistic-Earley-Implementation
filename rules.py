rules = {
    "ROOT": [["S"]],
    "S": [
        ["NP", "VP"]
    ],
    "NP": [
        ["NP", "PP"],
        ["det", "nn"]
    ],
    "VP": [
        ["vi"],
        ["vt", "NP"],
        ["VP", "PP"]
    ],
    "PP": [
        ["in", "NP"]
    ],
    "det": {"the"},
    "nn": {"man", "women", "telescope", "dog"},
    "in": {"with", "in"},
    "vi": {"sleeps"},
    "vt": {"saw"}
}

'''
rule1 = {
    "ROOT": [["S"]],
    "S": [
        ["NP", "VP"],
        ["aux", "NP", "VP"],
        ["VP"]
    ],
    "NP": [
        ["pronoun"],
        ["noun"],
        ["det", "NOMINAL"]
    ],
    "NOMINAL": [
        ["noun"],
        ["NOMINAL", "noun"],
        ["NOMINAL", "PP"]
    ],
    "VP": [
        ["verb"],
        ["verb", "NP"],
        ["verb", "NP", "PP"],
        ["verb", "PP"],
        ["VP", "PP"]
    ],
    "PP": [
        ["prepos", "NP"]
    ],
    "det": {"that", "this", "a"},
    "noun": {"flight", "meal", "money", "gift", "astronomers", "stars", "ears", "world", "india", "me"},
    "verb": {"book", "include", "prefer", "saw", "hello"},
    "pronoun": {"i", "she", "me"},
    "aux": {"does"},
    "prepos": {"from", "to", "on", "near", "through", "with"}
}

rule2 = {
    "ROOT": [["S"]],
    "S" :  [
        ["NP", "VP"],
        ],
    "VP" : [
        ["vt", "NP"],
        ["vi", "adv"]
        ],
    "NP" : [
        ["det", "nn"],
        ["np"]
        ],
    "nn" : {"cat", "dog"},
    "np" : {"Fluffy", "Fido"},
    "det" : {"Every", "a"},
    "vt" : {"is", "loves"},
    "vi" : {"sleeps"},
    "adv" : {"soundly"}
}
'''
