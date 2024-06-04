#include<stdio.h>
int c(int n){if(n<=1) return n-1;if(n&1) return 1+c(3*n+1);return 1+c(n/2);}
int main(){for(int i=1;i<1001;i++)printf("%d\n", c(i));}
