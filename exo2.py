temp=[]
for _ in range (31):
    val=float(input("Entrez la température: "))
    temp.append(val)
total_min=temp[0]
total_max=temp[0]
for i in range (len(temp)-1):
    if total_min>temp[i+1]:
        total_min=temp[i+1]
    if total_max<temp[i+1]:
        total_max=temp[i+1]
etendue=total_max-total_min
print("L'étendue des températures est de :",etendue)
print("La valeur la plus petit est de :",total_min)
print("La valeur la plus grande est de :",total_max)