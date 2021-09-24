max_length_key_estimate = 20
english_alphabet = 'abcdefghijklmnopqrstuvwxyz'

english_alphabet_frequencies = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
					  0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
					  0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
					  0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

def get_index_coincidence(ciphertext):
    x = float(len(ciphertext))
    frequency = 0.0
    for letter in english_alphabet:
        frequency += ciphertext.count(letter) * (ciphertext.count(letter)-1)
    indexC = frequency/(x*(x-1))
    return indexC

def acquire_key_length(ciphertext):
    indexC_table=[]
    for est_length in range(max_length_key_estimate):
        indexCSum = 0.0
        avg_indexC = 0.0
        for i in range(est_length):
            sequence = ""
            for j in range(0, len(ciphertext[i:]), est_length):
                sequence += ciphertext[i+j]
            indexCSum += get_index_coincidence(sequence)
        if not est_length == 0:
            avg_indexC = indexCSum/est_length
        indexC_table.append(avg_indexC)
    best_est = indexC_table.index(sorted(indexC_table, reverse = True) [0])
    second_best_est = indexC_table.index(sorted(indexC_table, reverse = True) [1])
    return best_est

def frequency_analysis(sequence):
    all_chi_squares = [0] * 26
    for i in range(26):
        chi_square_sum = 0.0
        sequence_offset = [chr(((ord(sequence[j])-97-i)%26)+97) for j in range(len(sequence))]
        y = [0] * 26
        for l in sequence_offset:
            y[ord(l) - ord('a')] += 1
        for j in range(26):
            y[j] * (1.0/float(len(sequence)))
        for j in range(26):
            chi_square_sum += ((y[j] - float(english_alphabet_frequencies[j])) ** 2)/float(english_alphabet_frequencies[j])
        all_chi_squares[i] = chi_square_sum
    shift_letter = all_chi_squares.index(min(all_chi_squares))
    return chr(shift_letter+97)

def acquire_key(ciphertext, key_length):
    key = ''
    for i in range(key_length):
        sequence = ''
        for j in range(0, len(ciphertext[i:]), key_length):
            sequence += ciphertext[i + j]
        key += frequency_analysis(sequence)
    return key

def decryption(ciphertext, key):
    ciphertext_ascii = [ord(letter) for letter in ciphertext]
    key_ascii = [ord(letter) for letter in key]
    plaintext_ascii = []
    for i in range(len(ciphertext_ascii)):
        plaintext_ascii.append(((ciphertext_ascii[i] - key_ascii[i % len(key)]) % 26) + 97)
    plaintext = ''.join(chr(i) for i in plaintext_ascii)
    return plaintext

def main():
    raw_ciphertext = 'rimqessfntwpwtelqdeerkwdpezrfxjumpqxqqurxhifdjaffirlffnsyahrxtoutszwaxwvdspwqbpidwhitvpdnvizstnexzrhpujfcwmfvihdcspkqbrvpczztxugnfdlhdzreheyrkworezrnrpcmatrsdesifqpwwfvnxdmssnsysgltzbgwyqbpidwoegidgnvxvgbyhivvgwrffcixogiskcwlvuchwpjdfnxewamcwcsxefwbrhvqvcmfmfyryotoefopscwweprfwnpxkmelxmwaxtxfjecmbqejkvfyxuqnxxfbnzhqfaggpduzkdoclnzbupvespxhkvfomeqvtazbfdsranxwvabemogpsbgiupveqvictsbyhqzrgiiwdlpqbtmcvsstrsoctazqbemabfsutfzaxaueeeymjygxiqipkadlvpgpsbgiupvbofwlffedezrrptthszruqpsbdssniofltifzprcbfvsgkcusiycqigeohpamgnpbfgudczcacbfithmfvrrrimqemabglttcogidgvscftjyjafzeizcoqvaanvtrrbmpqggeivhpltboeickbpywqbfiiystprpsevtkojyiphuipswmtxkhbhttfzaxfvrmcwcsxefwbrperusidsssgvowzmpiaapehfotqffscjpftrsooptkcspepwgwxeqfhsdzqapiwbyhfvresmsoesrhuirfaqfxqfgltdsusspghwtuhpnedflsjkqsjtfcysvpvbginspsbvwonvqofmcxzznsydyimrbetxeoctazqbemabzsgvkjoiedeipuapoidbpvnghprvmducufzmzaeofxgfbhwceqvickwgtgmdcvdrqilrprrwxxbtnvkdgsvioqsmooykdiwusqeoesjerdzqbigeizcolptoehcvgtlweiztizcodqmyvrvjidsexubvxkvndlmfqxdsfflonmnrpujfcwmflmizgusiafrxxtomwcbcfwxszfesnfrezjidseemfxtdpvemfwfmcwsbdmnzrxductzfkoaceiodemooyqtrbtelqgrwrysnpwmfrxwvffqsdspsbgiulxucaeacmtpggfrxwvffpbuggmcwcsxefwbriyspcifwpeacmtpggfrwrysnpwfvnxeicwlfxmpececuminfboteoopbmacptzgusiabrxxdsqlhnigxwvgfdgtszihrffxsdsqmuwwdfpfhbmbgzfxizhglpehipxtsbvtkwdlpxmovtrybmpqphxrfaqfxmhvscrzmjwqqhvtdsdsezwfqhtfzaxazbknismlxqrgirybpwssmuehiojdipoaybssszjxsteazgtfiewaxwviotxqrxmcxrpxeprvxxfbtesfvrvtximlxucasuzbwpwfwteiffzasisewpthspugweihrgvdtqqgistfjxmzoyxdyoooshsexwvwsprofltizcovikwsehbsemcxojicwcsniysaxdkvfcaugrxwvitpviwypurqflgdwzmcrzdsedurxwvsmpgffbrxttszrfwrvufiooefwbrxjwogsxjrhxeodlwqwaxwvgvavqargdlfuzjfvryczhfowfogihnvjnliwyppjqfcxmwamuisrfmdwakhlgqpgfsqggzajyexggseicwthqhuixisonvkdgmdeyfjwfcyelvbgzvoszickwtfrocawizhvemabnpiysfqjugnvvlworxtogxwzgjdehwbppkwpysrhuigzuiesrbbxqvworjafpiskcjygdwzmcrhfzrqgrpurghtzqbvriysgtjfvnqternprf'
    ciphertext = ''.join(x.lower() for x in raw_ciphertext if x.isalpha())
    key_length = acquire_key_length(ciphertext)
    key = acquire_key(ciphertext, key_length)
    plaintext = decryption(ciphertext, key)
    print("Key: {}".format(key))
    print("Plaintext: {}".format(plaintext))

if __name__ == '__main__':
    main()