tv = televisor ('SONY' , 'SONY-123')

controle = controleRemoto(tv)

controle.sintonizar_canal('globo')
controle.trocar_canal('globo')

print(tv.canal_Atual)
