from difflib import SequenceMatcher

def asd(str1 , str2):
    seq_match = SequenceMatcher(None, str1, str2)

    match = seq_match.find_longest_match(0, len(str1), 0, len(str2))

    return str1[match.a: match.a + match.size] if match.size != 0 else 'false'

print(asd('fsdkjfskfa', 'dfdjkfkhdjf'))