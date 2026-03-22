#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

static void win(void) {
    FILE *f = fopen("flag.txt", "r");
    if (!f) {
        puts("flag.txt not found");
        exit(1);
    }
    char buf[128];
    if (fgets(buf, sizeof(buf), f)) {
        puts(buf);
    }
    fclose(f);
    exit(0);
}

static void survey(void) {
    char buf[0x90];

    puts("== Survey ==");
    puts("Tell us your experience:");
    read(0, buf, sizeof(buf));

    char *p = buf + 0x10;
    free(p);

    char *q = malloc(0x30);
    puts("Final impression?");
    read(0, q, 0x100);
}

static void menu(void) {
    puts("1. Survey");
    puts("2. Exit");
    printf("> ");
}

int main(void) {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    while (1) {
        menu();
        char opt[8] = {0};
        if (!fgets(opt, sizeof(opt), stdin)) {
            break;
        }
        if (opt[0] == '1') {
            survey();
        } else if (opt[0] == '2') {
            puts("bye");
            break;
        } else {
            puts("invalid option");
        }
    }

    return 0;
}
