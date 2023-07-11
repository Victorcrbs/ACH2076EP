def get_letter_frequency_mono(string):
    freqs = {}
    for letter in string:
        if letter in freqs:
            freqs[letter] += 1
        else:
            freqs[letter] = 1
    for freq in freqs:
        x = freqs.get(freq)/len(string)
        freqs = { **freqs, freq: x}
    return sorted(freqs.items(), key=lambda x: x[1], reverse= True)

ciphertext_know ="ribnbqorfjoebrbibrrfaozoebxfqonaovjbjvmhaqbofnbjorbkbzebqororlbeosazorbuvbnqbbszfubqbqbnfivsmaeboraz"
ciphertext = "zldltljmltjmakvletiagltasvlermoarkeueplklrltadnklatlglnsxemdaoaetilktaulvnemdaoadpmtrlvoedaedaviekil"

print(get_letter_frequency(ciphertext_know))
#[('b', 0.21), ('o', 0.13), ('r', 0.1), ('q', 0.07), ('f', 0.06), ('a', 0.06), ('n', 0.05), ('e', 0.05), ('z', 0.05), ('j', 0.04), ('v', 0.04), ('i', 0.03), ('s', 0.03), ('m', 0.02), ('u', 0.02), ('x', 0.01), ('h', 0.01), ('k', 0.01), ('l', 0.01)]
print(get_letter_frequency(ciphertext))
#[('l', 0.17), ('a', 0.13), ('e', 0.1), ('t', 0.09), ('d', 0.07), ('m', 0.06), ('k', 0.06), ('v', 0.05), ('i', 0.04), ('r', 0.04), ('o', 0.04), ('n', 0.03), ('j', 0.02), ('g', 0.02), ('s', 0.02), ('u', 0.02), ('p', 0.02), ('z', 0.01), ('x', 0.01)]

