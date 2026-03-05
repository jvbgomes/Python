def piso(x):
  inteiro = 0

  if x >= 0:
    while inteiro + 1 <= x:
      inteiro += 1
    return inteiro
  else:
    while inteiro - 1 >= x:
      inteiro -= 1
    if x == inteiro:
      return inteiro
    else:
      return inteiro - 1    

def teto(x):
  inteiro = 0

  if x >= 0:
    while inteiro + 1 <= x:
      inteiro += 1
    if x == inteiro:
      return inteiro
    else:
      return inteiro + 1
  else:
    while inteiro -1 >= x:
      inteiro -= 1
    return inteiro         

def div(a, b):
  if b == 0:
    raise ValueError("Divisão por zero não é permitida.")

  quociente = 0
  sinal = 1 if (a * b) >= 0 else -1
  abs_a = a if a >= 0 else -a
  abs_b = b if b >= 0 else -b

  while abs_a >= abs_b:
    abs_a -= abs_b
    quociente += 1

  quociente *= sinal

  if a < 0 and (a - b * quociente) != 0:
    quociente -= 1

  return quociente

def mod(a, b):
  q = div(a, b)
  resto = a - b * q
  return resto

def intervalos_primos(a, b):
  inicio = min(a, b)
  fim = max(a, b)
  if fim < 2:
      return []

  if inicio < 2:
      inicio = 2

  primos = []
  marcados = [False] * (fim + 1)

  for i in range(2, fim + 1):
      if not marcados[i]:
          if i >= inicio:
              primos.append(i)
          for j in range(i * 2, fim + 1, i):
              marcados[j] = True

  return primos

def mdc_bezout(a, b):
  A, B = a, b

  s0, s1 = 1, 0
  t0, t1 = 0, 1
  r0, r1 = a, b

  print(f"Passo: r0={r0}, r1={r1}, s0={s0}, s1={s1}, t0={t0}, t1={t1}")

  while r1 != 0:
    q = 0
    temp = r0
    if abs(r0) >= abs(r1):
      while abs(temp) >= abs(r1):
        if r0 > 0:
          temp -= abs(r1)
        else:
          temp += abs(r1)
        q += 1

    if (r0 < 0) != (r1 < 0):
      q = -q

    r2 = r0 - q * r1
    s2 = s0 - q * s1
    t2 = t0 - q * t1

    print(f"Passo: r0={r1}, r1={r2}, s0={s1}, s1={s2}, t0={t1}, t2={t2}")

    r0, r1 = r1, r2
    s0, s1 = s1, s2
    t0, t1 = t1, t2

  print(f"MDC({A},{B}) = {r0}, s = {s0}, t = {t0}")
  return r0, s0, t0

def dia_da_semana(dia, mes, ano):
  if ano == 1582 and mes == 10 and 5<= dia <= 15:
    return "Data inexistente"

  if mes < 3:
    mes += 12
    ano -= 1

  k = mod(ano, 100)
  j = div(ano, 100)

  termo_mes = div(13 * (mes + 1), 5)
  termo_k4 = div(k, 4)
  termo_j4 = div(j, 4)

  soma = dia + termo_mes + k + termo_k4 + termo_j4 + 5 * j
  s = mod(soma, 7)

  dias = ["Sábado", "Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]

  return dias[s]


if __name__ == "__main__":
  
  x = 3.7
  a = 17
  b = 5

p = piso(x)
t = teto(x)
print(f"piso({x}) --> {p}")
print(f"teto({x}) --> {t}")

print(f"div({a}, {b}) --> {div(a, b)}")
print(f"mod({a}, {b}) --> {mod(a, b)}")

primos = intervalos_primos(10, 30)
print(f"intervalos_primos(10, 30) --> {primos}")

mdc, s, tcoef = mdc_bezout(189, 67)
print(f"mdc_bezout(189, 67) --> mdc={mdc}, s={s}, t={tcoef}")

print(f"dia_da_semana(18, 10 , 2025) --> {dia_da_semana(18, 10, 2025)}")