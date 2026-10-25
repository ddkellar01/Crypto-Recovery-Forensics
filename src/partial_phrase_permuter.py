from bip_utils import Bip39MnemonicValidator, Bip39Languages, Bip39WordsListGetter

def recover_missing_word(words_with_missing: list, missing_index: int) -> list:
    wordlist = Bip39WordsListGetter.GetWords(Bip39Languages.ENGLISH)
    validator = Bip39MnemonicValidator(Bip39Languages.ENGLISH)
    valid_candidates = []

    words_copy = words_with_missing.copy()
    
    for candidate_word in wordlist:
        words_copy[missing_index] = candidate_word
        test_phrase = " ".join(words_copy)
        if validator.IsValid(test_phrase):
            valid_candidates.append(candidate_word)

    return valid_candidates

if __name__ == "__main__":
    # Test vector with word index 11 replaced by wildcard placeholder
    phrase_words = ["abandon"] * 11 + [""]
    missing_idx = 11
    
    matches = recover_missing_word(phrase_words, missing_idx)
    print(f"Valid BIP-39 candidate words for position {missing_idx}: {matches}")
  
