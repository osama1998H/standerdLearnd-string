from difflib import SequenceMatcher

def asd(str1 , str2):
    seq_match = SequenceMatcher(None, str1, str2)

    match = seq_match.find_longest_match(0, len(str1), 0, len(str2))

    if match.size != 0:
        return (str1[match.a: match.a + match.size])
    else:
        return 'false'

print(asd('fsdkjfskfa', 'dfdjkfkhdjf'))