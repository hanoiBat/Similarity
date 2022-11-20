import similarity
import scan

def main(text1, text):
    return similarity.sentenceSimilarity(text1, text)

if __name__ == "__main__":
    text1 = "this is not a test"
    text2 = "This is a test"
    print(main(text1, text2))
