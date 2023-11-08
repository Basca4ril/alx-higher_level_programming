#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        bscore = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if value == bscore:
                return key
    else:
        return None
