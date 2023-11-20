v_d_h = float(input("Digite quanto você recebe por hora: "))
h_t = float(
    input("Digite quantas horas você trabalhou esse mês: "))
s_b = v_d_h * horas_trabalhadas
if s_b<= 900:
    desconto_ir = 0.0
elif s_b <= 1500:
    desconto_ir = 5
elif s_b <= 2500:
    desconto_ir = 10
else:
    desconto_ir = 20

IR = s_b * (desconto_ir / 100)
INSS = s_b* (10 / 100)
FGTS = s_b * (11 / 100)
t_d_des = IR + INSS
salario_liquido = salario_bruto - total_de_descontos

print(
    f"\nSalário Bruto     : R${s_b:.2f}",
    f"\n(-) IR (5%)       : R${IR:.2f}",
    f"\n(-) INSS ( 10%)   : R${INSS:.2f}",
    f"\nFGTS (11%)        : R${FGTS:.2f}",
    f"\nTotal de descontos: R${t_d_des:.2f}",
    f"\nSalário Liquido   : R${s_l:.2f}",
)
