from bip_utils import Bip39WordsListGetter, Bip39Languages

def scan_text_for_bip39(text_corpus: str) -> list:
    wordlist = set(Bip39WordsListGetter.GetWords(Bip39Languages.ENGLISH))
    words_in_text = text_corpus.lower().split()
    found_words = [w for w in words_in_text if w in wordlist]
    return found_words

if __name__ == "__main__":
    sample_text = "abandon the mission to check apple basket"
    print(scan_text_for_bip39(sample_text))
  
