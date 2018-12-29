X = "seMi Long StRing WiTH COMPLetely RaNDOM CasINg"
result_string = ""
index = 0;
for c in X:
    if(index%2 == 0):
        result_string += c.lower()
    else:
        result_string += c.upper()
    index+=1

print(result_string)
