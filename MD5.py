import hashlib
inputstring = "Saveetha School Of Engineering"
output = hashlib.md5(inputstring.encode())
print("Hash of the input string:")
print(output.hexdigest())
