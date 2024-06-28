#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    char str[100];
    fgets(str, sizeof(str), stdin);
    str[strlen(str) - 1] = '\0'; // remove newline character

    for (int i = 0; str[i]; i++) {
        if (i == 0 || !isalpha(str[i-1])) {
            str[i] = toupper(str[i]);
        } else {
            str[i] = tolower(str[i]);
        }
    }

    printf("%s\n", str);
    return 0;
}
