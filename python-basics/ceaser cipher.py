alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

choose=input("Whether you want to encode or decode:\n")
text=input("enter your text:\n").lower()
shift=int(input("Enter the number youwant to shift:\n"))

def ceaser(original_text,shifted_amount,encode_or_decode):

    if encode_or_decode == "encode":
        
        def encrypt(original_text,shifted_amount):
            shifted=""
            for i in original_text:
                s=alphabet.index(i)+shifted_amount
                s=s%len(alphabet)
                shifted+=alphabet[s]
            print("Your encoded text is:",shifted)
        encrypt(text,shift)
        
    elif encode_or_decode == "decode":
        
        def decrypt(original_text,shifted_amount):
            shifted=""
            for i in original_text:
                s=alphabet.index(i)- shifted_amount
                s=s%len(alphabet)
                shifted+=alphabet[s]
            print("Your decode text is:",shifted)
        decrypt(text,shift)
        
    else:
        print("Enter correctly")
    
ceaser(text,shift,choose)
    