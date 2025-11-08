weight = input("Enter Your weight!")

unit = input("(L)bs or (K)g")

k_to_p = int(weight) * 2.204
p_to_k = int(weight) / 2.204

if unit== str("L") or unit== str("l"):
    print ('You are ' + str(p_to_k) + 'Kg')

elif unit == str("K") or unit== str("k"):
    print ('you are ' + str(k_to_p) + "Lbs")

else:
    print("Enter valid value please!")

#Here i built a code to convert kilo into pounds and pounds into kilos!
#put a weight and then select unit then u will get your answer!
#mosh used smart approach here he simply used the UPPER case function
#so the input automatically gets convirted into upeer case so no need to write OR statement!
#he also restricted user from entring anything in weight input by simply putting weight=str,,where as i converted it again and again
#he also used F function to convert the whole line ! print(f'{})