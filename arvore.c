#include <stdio.h>
#include <string.h>

void print(int matriz[][2], int a)
{
	if (a == -1) return;
	printf("%d ->", a);
	print(matriz, matriz[a][0]);//esquerda 
	print(matriz, matriz[a][1]);//direita
	
}

int main()
{
	int matriz[7][2], p, k = 3; //k = quant de linhas
	memset(matriz, -1, sizeof(matriz));//iniciar uma matriz/array com um numero. ex: -1;/// sizeof: retorna o valor da matriz

	for (int i = 0; i < k; ++i)
	{	
		scanf("%d", &p);
		scanf("%d %d", &matriz[p][0], &matriz[p][1]);
	}

	print(matriz, 0);
	return 0;
}
