#include <stdio.h>

int arr[100000];

int main(){
	int i, max, n;
	
	scanf("%d", &n);
	
	for(i=0;i<n;++i)
		scanf("%d", &arr[i]);
	
	max = arr[0];
	
	for(i=1;i<n;++i){
		if(arr[i-1] > 0 && arr[i] + arr[i-1] > 0)
			arr[i] += arr[i-1];
		if(max <= arr[i])
			max = arr[i];
	}
	
	printf("%d", max);
	
}