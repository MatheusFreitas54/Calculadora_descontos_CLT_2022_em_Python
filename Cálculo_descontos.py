# Calculo-de-descontos-sobre-o-sal-rio-bruto---2022
#Calculadora automático dos descontos sobre o seu salário bruto
br = ''
print(br)
print("Calculo de descontos sobre o salário bruto - 2022")
print(br)
val_hora = float(input("Digite o valor da sua hora: "))
hora_sem = float(input("Qual a sua carga horária semanal: "))
dep_quant = int(input('Quantos dependentes você possui: '))
quest_vt = input('Você ultiliza vale transporte? Responda com s/n: ')
hora_men = float(hora_sem*5)
sal_bru = float(hora_men*val_hora)
FGTS = round(float(sal_bru/100*8),2)
if sal_bru <= 1212.00 :
    INSS = round(float(sal_bru/100*7.5),2)
    p_inss = '7.5%'
elif sal_bru >= 1212.01 or sal_bru <= 2427.35 :
    INSS = round(float(sal_bru/100*9),2)
    p_inss = '9%'
elif sal_bru >= 2427.36 or sal_bru <= 3614.03 :
    INSS = round(float(sal_bru/100*12),2)
    p_inss = '12%'
elif sal_bru >= 3614.04 or sal_bru <= 7087.22 :
    INSS = round(float(sal_bru/100*14),2)
    p_inss = '14%'
else:
    print("Erro de cálculo - INSS")
if quest_vt == 'n' or quest_vt == 'N' :
    VT = 'Isento'
    porc_vt = '0%'
    sal_liq = round(float(sal_bru - FGTS - INSS ),2) 
elif quest_vt == 's' or quest_vt == 'S' :
    VT = round(float(sal_bru/100*6),2)
    porc_vt = '6%'
    sal_liq = round(float(sal_bru - FGTS - VT - INSS ),2)  
else:
    print('erro de calculo - VT')
if sal_liq <= 1903.98 and dep_quant >= 0:
    dep_irrf = round(float(dep_quant * 189.59),2)
    IRRF = 'Isento'
    p_irrf = '0%' 
    sal_liqfinal = float(sal_liq)
elif sal_liq >= 1903.99 and sal_liq <= 2826.65 and dep_quant > 0:
    dep_irrf = round(float(dep_quant * 189.59),2)
    IRRF = round(float((sal_liq - dep_irrf)/100*7.5),2)
    p_irrf = '7.5%'
    sal_liqfinal = round(float(sal_liq - IRRF),2)
elif sal_liq >= 2826.66 and sal_liq <= 3751.05 and dep_quant > 0:
    dep_irrf = round(float(dep_quant * 189.59),2)
    IRRF = round(float((sal_liq - dep_irrf)/100*15),2)
    p_irrf = '15%'
    sal_liqfinal = round(float(sal_liq - IRRF),2)
elif sal_liq >= 3751.06 and sal_liq <= 4664.68 and dep_quant > 0:
    dep_irrf = round(float(dep_quant * 189.59),2)
    IRRF = round(float((sal_liq - dep_irrf)/100*22.5),2)
    p_irrf = '22.5%'
    sal_liqfinal = round(float(sal_liq - IRRF),2)
elif sal_liq >= 4664.69 and dep_quant > 0:
    dep_irrf = round(float(dep_quant * 189.59),2)
    IRRF = round(float((sal_liq - dep_irrf)/100*27.5),2)
    p_irrf = '27.5%'
    sal_liqfinal = round(float(sal_liq - IRRF),2)
else:
    print('Erro de calculo dependente - IRRF')
print(br)
print("O seu salário bruto é - R$:",sal_bru)
print(br)
print("Os descontos do seu salário são:")
print("FGTS = 8% - R$:",FGTS)
print("VT =",porc_vt," - R$:",VT)
print("INSS =",p_inss,"- R$:",INSS)
print("IRRF =",p_irrf,"- R$:",IRRF,'(Já com os descontos dos dependentes)')
print(br)
print("O seu salário líquido é - R$:",sal_liqfinal)
