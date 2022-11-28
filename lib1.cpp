#include <string>
#include<cstring>
#include "lib1.h"

typedef void (*FUNP)();

typedef void (*FUNP1)(char *ch);

void hello() {
    printf("%s\n", "Hello, World!");
}

void echo(char *text) {
    printf("%s\n", text);
}

void printUser(char *user, unsigned int age) {
    printf("His name is %s and is %d years old.\n", user, age);
}

char *getName(char *userName) {
    return userName;
}

int sum(int a, int b) {
    return a + b;
}

void *getVoidData(void *data) {
    return data;
}

void *getVoidData1(void *data, int *addr) {
    char *tmp = static_cast<char *>(data);
    *addr = strlen(tmp);
    return data;
}

void callback(FUNP funp) {
    (*funp)();
}

void callback1(FUNP1 funp1, char *text) {
    (*funp1)(text);
}