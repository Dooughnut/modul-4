#include <stdio.h>

int main() {
    int kelipatan, jumlah_anak = 50;
    char simbol;

    scanf("%d %c", &kelipatan, &simbol);
   
    for (int i = 1; i <= jumlah_anak; i++) {
        if (i % kelipatan == 0) {
            printf("%c ", simbol);
        } else {
            printf("%d ", i);
        }
    }

    printf("\n");
    return 0;
}