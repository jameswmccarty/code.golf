#include<stdio.h>
int c(int c){int w=0;while(c){if(c&1)w+=1;c/=2;}return w&1;}
int main(){for(int i=0;i<51;i++){
if(!c(i))printf("%d\n",i);}}
