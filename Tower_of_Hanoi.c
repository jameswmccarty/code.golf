#include<stdio.h>
void s(int n,int c,int d){if(n){s(n-1,c,c^d);printf("%d -> %d\n",c,d);s(n-1,c^d,d);}}
void main(){s(9,1,3);}
