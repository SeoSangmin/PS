#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n;
	int *nums;
	int v;
	int ret;

	scanf("%d\n", &n);
	nums = (int *) malloc(sizeof (int) * n);
	if (!nums)
		return 0;
	for (int i = 0; i < n; ++i)
		scanf("%d ", nums + i);
	scanf("%d", &v);
	ret = 0;
	for (int i = 0; i < n; ++i)
		if (*(nums + i) == v)
			ret++;
	printf("%d", ret);
	return 0;
}
