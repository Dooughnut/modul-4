#include <stdio.h> 

int main(){
int angka1, angka2, i ,j; 

scanf(" %d %d",&angka1, &angka2);

for (i=angka1, j=angka2; i<=angka2&&j>=angka1; i++, j--)
{
    printf("%d %d",i, j);
    if (i<angka2||j>angka1){
        printf(" - "); }
}
for(i=angka1, j=angka2; i>=angka2&&j<=angka1; i--, j++) {
    printf(" %d %d", i, j);
    if (i>angka2||j<angka1){
        printf(" - ");
        }
}
return 0;
}
