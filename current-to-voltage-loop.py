# 运放深度负反馈下，V+ = V-.
# I(loop) = I(R11) + I(R10)
# I(R11) = I(R10) * R10 / R11
# I(R10) = I(R9) + I(R7)
# I(R9) = V(DAC1_OUT1) / R9
# I(R7) = 5V / R7
# V(DAC1_OUT1)= 0.2~2.3V,留点余量,V(DAC1_OUT1)=0.4~2.1V.
# I(Loop) = 4mA~20mA
# I(loop) 与VDAC1_OUT1有线性关系.所以V(DAC1_OUT1)=1.25V时, I(loop) = 12mA
# 连立以上.
# I(loop) = (R10 / R11 + 1) ((V(DAC1_OUT1) / R9) + 5 / R7)
# 电阻小些,不容易受干扰. 取 R10 / R11 + 1 = 10, 当R11 = 10时, R10 = 90.
# 此时需要担心运放输出电流是否过大,大约数量级别为 20mA / 10 = 2mA,查询得到OPA2244UA输出电流可达12mA.
# 代入 V(DAC1_OUT1)=1.25V时, I(loop) = 12mA,得到
# 12e-3 = 1e1 ((1.25/ R9) + 5/R7)
# 12e-4 =(1.25 / R9) + 5 / R7
# 当R9 = 3.4K 时,R7 = 6.007K



from decimal import Decimal, getcontext

# Set decimal precision
getcontext().prec = 12

# Constants
Rd = Decimal('10.0')  # Ω
Gain = Decimal('4.99')        # Gain setting
Vb = Decimal('5')           # 5V supply
Va_min = Decimal('0.1')       # Minimum voltage
Va_max = Decimal('3.2')       # Maximum voltage

# Current range calculations
Iloop_min = (Decimal('4e-3') / Gain)  # 4mA
Iloop_max = (Decimal('20e-3') / Gain) # 20mA

# Calculate Rx (current-to-voltage conversion resistor)
Ra = (Va_max - Va_min) / (Iloop_max - Iloop_min)

# Calculate Rb (bias resistor)
Rb = Vb / (Iloop_min - (Va_min / Ra))

Rc = (Gain - 1) * Rd

# Print results
print(f"Ra: {Ra} Ω")
print(f"Rb: {Rb} Ω")
print(f"Rc: {Rc} Ω")
print(f"Rs: {Rd} Ω")

# Ra: 966.812500000 Ω
# Rb: 7161.57407407 Ω
# Rc: 39.900 Ω
# Rd: 10.0 Ω

