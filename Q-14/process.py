import time
for i in range(1,200):
    print(f'Procesando {i/200*100}%')
    time.sleep(0.05)
print('Processamento concluído!')
