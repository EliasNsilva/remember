import matplotlib.pyplot as plt #importando biblioteca por um nome mais curto
import pandas as pd 
import matplotlib.style as mplstyle #para estilos rapidos

#1º Gráfico com todos dados.

mplstyle.use(['ggplot'])#estilos rapidos para ver todos usar o comado mplstyle.available

dados = pd.read_csv('a2_MANCHAS.csv')#ler arquivo csv e salvar em variável
plt.plot(dados.Ano, dados.manchas)#plotando os dados, pelos nomes das colunas de dados
plt.grid(True)#ativando grades no gráfico
plt.xlabel("Anos")#titulo pro eixo X
plt.ylabel("Manchas")#titulo para o eixo Y
plt.title("Número de manchas Solares")#titulo do gráfico
plt.show()#apresentar o grafico quando rodar o code

#2º Dez primeiras linhas de dados.

dados_10 = dados[0:10]#usando as 10 primeiras linhas de dados
plt.plot(dados_10.Ano, dados_10.manchas, 'g')#usar 'letra da cor' para escolher a cor da linha
plt.grid(True)
plt.xlabel("Anos")
plt.ylabel("Manchas")
plt.title("Número de manchas Solares")
plt.xticks(dados_10.Ano, rotation = 'vertical')#rotacionar os dados exibidos no eixo escolhido 
plt.show()

#3º Dez últimas linhas de dados. 

dados_10_ult = dados[167:]#escolhendo uma linha para começar a ler os dados até o final
plt.plot(dados_10_ult.Ano, dados_10_ult.manchas, 'b--')# -- linha pontinhada
plt.grid(True)
plt.xlabel("Anos")
plt.ylabel("Manchas")
plt.title("Número de manchas Solares")
plt.xticks(dados_10_ult.Ano, rotation = 'vertical')
plt.show()

#4º boxplot.

plt.boxplot(dados.manchas)#grafico boxplot de um coluna de dados
plt.grid(True)
plt.ylabel("Manchas")
plt.title("Número de manchas Solares")
plt.show()
#plt.savefig('nome da imagem')#para salvar o grafico gerado
