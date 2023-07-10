from hillCipher import HillCipher
from scipy.stats import binom
import itertools
import pprint

obj = HillCipher()


def calculate_score(plaintext):
    if plaintext is None:
        return 0
    
    portuguese_letter_frequency = {
        'a': 0.1463, 'b': 0.0104, 'c': 0.0388, 'd': 0.0499, 'e': 0.1257, 'f': 0.0102,
        'g': 0.0130, 'h': 0.0128, 'i': 0.0618, 'j': 0.0040, 'k': 0.0002, 'l': 0.0278,
        'm': 0.0474, 'n': 0.0505, 'o': 0.1073, 'p': 0.0252, 'q': 0.0120, 'r': 0.0653,
        's': 0.0781, 't': 0.0434, 'u': 0.0463, 'v': 0.0167, 'w': 0.0001, 'x': 0.0021,
        'y': 0.0001, 'z': 0.0047
    }

    score = 1

    letter_frequecy = get_letter_frequency(plaintext)

    # Calculate the frequency score based on binomial probability
    for letter in letter_frequecy:
        k = letter_frequecy.get(letter)
        n = len(plaintext)
        p = portuguese_letter_frequency.get(letter)
        score = score*binom.pmf(k, n, p)
    return score


def generate_keys():
    keys = []   
    for i in itertools.product(range(26), repeat=2):
        for j in itertools.product(range(26), repeat=2):
            keys.append([i,j])
    return keys

def get_letter_frequency(string):
    freq = {}
    for letter in string:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    return freq


def rank_keys(ciphertext, num_results):
    scores = []
    keys = generate_keys()
    for i, key in enumerate(keys):
        plaintext = obj.decrypt(ciphertext, key)
        if plaintext is not None:
            score = calculate_score(plaintext)
            scores.append((key, plaintext, score))
        if i % 100000 == 0:
            print(f"Iteration: {i}, Key: {key}")
    results = sorted(scores, key=lambda x: x[2], reverse=True)[:num_results]
    return results

ciphertext_know ="aznrkuwlpjeykmnjbwkuoukmamjeippdplmfoeasvdmfyigvamineqnjavihyhasxwqupbymnjzemzdhosquplaqvpjakucivagb"
ciphertext = "wdzcpeoqeghladmuoqmuupucrqiwyengiqhlgtatkqldmvjgmvdelcxzkqvgbqnqliialniuualqauoawcanpepaauucbepvadfe"
num_results = 100

results = rank_keys(ciphertext, num_results)
pprint.pprint(results)