days = int(input('Digite o numero de dias\n>>>'))
years = (days - days%365)/365
r = days%365
months = (r - r%30)/30
day = r%30
print('Thanos chega em: {ano} ano(s),{mes} mês(es) e {dia} dia(s)'.format(ano=int(years),mes=int(months),dia=int(day)))
