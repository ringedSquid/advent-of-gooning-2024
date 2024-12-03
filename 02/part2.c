#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int check(int* a, int n) {
	int trend = (a[1] - a[0]) > 0 ? 1 : 0;
	for (int i=1; i<n; i++) {
		int diff = a[i] - a[i-1];
		if ((abs(diff) > 3) || (abs(diff) < 1) || ((diff > 0) != trend)) {
			return 0;
		}
	}
	return 1;
}

int checkall(int* a, int n) {
	int* b = (int*)malloc(sizeof(int)*(n-1));
	for (int i=0; i<n; i++) {
		int z = 0;
		for (int y=0; y<n; y++) {
			if (y == i) {
				z++;	
			}
			else {
				b[y-z] = a[y];
			}
		}
		if (check(b, n-1)) {
			return 1;
		}

	}
	return 0;
}


int main(void) {
	int a[100];
	int n=0;

	char buff[100];
	while (fgets(buff, 100, stdin)) {
		int i;
		char* line = buff;
		char* token;
		for (i=0; token = strsep(&line, " "); i++) {
			a[i] = atoi(token);
		}
		n += checkall(a, i);
	}
	printf("%d\n", n);
}
