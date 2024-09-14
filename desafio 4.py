print("="*14)
print("Medidor de IMC")
print("="*14)

peso = float(input("Digite o seu peso: "))
altura = float(input("digite sua altura: "))
IMC = peso / pow(altura,2)
estado = "sem valor"
if IMC < 18.50:
    estado = "abaixo do normal"
elif 18.50 <= IMC <= 24.99:
    estado = "normal"
elif 25.00 <= IMC <= 29.99:
    estado =  "sobrepeso"
elif 30.00 <= IMC <= 34.99:
    estado = "Obesidade Grau 1"
elif 35.00 <= IMC <= 39.99:
    estado = "Obesidade Grau 2"
elif IMC >= 40.00:
    estado = "Obesidade Grau 3"

print("seu peso é {}, sua altura é {}, seu IMC é {:.2f}, e o estado do seu IMC é de {}".format(peso, altura, IMC, estado))