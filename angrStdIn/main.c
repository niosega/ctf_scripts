#include <stdio.h>
#include <string.h>

int main() {
    char buf[250];
    fgets(buf, 249, stdin);

    if (strcmp(buf, "nico{flag}\n") == 0) {
        printf("WIN\n");
    } else {
        printf("LOSE\n");
    }
}