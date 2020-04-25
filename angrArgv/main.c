#include <stdio.h>
#include <string.h>

int main(int argc, char** argv) {
    if (strcmp(argv[1], "nico{flag}") == 0) {
        printf("WIN\n");
    } else {
        printf("LOSE\n");
    }
}