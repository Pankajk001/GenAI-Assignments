
class Encoder:
    def __init__(self, vocabSize = 10000):
        self.vocabSize = vocabSize

    #function to encode tokens
    def encode(self, text):
        tokens = text.split()
        encodedTokens = []

        for token in tokens:
            asciVal = ""
            for char in token:
                asciVal += str(ord(char))

            encodedToken = int(asciVal)
            encodedTokens.append(encodedToken)

        return encodedTokens
    

    #function to decode tokens
    def decode(self, encodedTokens):
        decodedTokens = []

        for number in encodedTokens:
            digits = str(number)
            i = 0
            token = ""

            while i < len(digits):
                if(i+3 < len(digits) and 32 <= int(digits[i : i+3]) <= 126):
                    token += chr(int(digits[i:i+3]))
                    i += 3

                elif(i+2 <= len(digits) and 32 <= int(digits[i: i+2]) <= 126):
                    token += chr(int(digits[i: i+2]))
                    i += 2

                else:
                    token += "<UNK>"
                    break

            decodedTokens.append(token)
        
        return " ".join(decodedTokens)
    

def main():
    encoder = Encoder()
    text = "Hey! Pankaj this side."

    encoded_val = encoder.encode(text)
    print(f"Encoded String is : {encoded_val}")

    decoded_val = encoder.decode(encoded_val)
    print(f"Decoded string is : {decoded_val}")


if(__name__ == "__main__"):
    main()