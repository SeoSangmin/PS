#include <stdio.h>
#include <stdlib.h>

int main()
{
	int cal_price = 0;
	int total = 0;
	int n, a, b;

	scanf("%d", &total);
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		scanf("%d %d", &a, &b);
		cal_price += a * b;
	}

	cal_price == total ? printf("Yes\n") : printf("No\n");
	return 0;
}
