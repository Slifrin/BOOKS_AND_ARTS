#include <stdlib.h>
#include <stdio.h>

char *som_f()
{
    int myNum;

    printf("Type a number: \n");

    scanf("%d", &myNum);
    char *my_chars = malloc(myNum * sizeof(char));

    my_chars = "Jurek";
    // char c = myNum +'0';
    // my_chars[6] = c;
    // my_chars[7] = '\0';
    printf("Hi %p \n", my_chars);

    return my_chars;
}


void check1()
{
    char *data = som_f();
    printf("Hi %p \n", data);
    printf("Hello there %s\n", data);
    char *data2 = som_f();
    printf("Hi %p \n", data);
    printf("Hello there %s\n", data);

    free(data);
}

char *other_func()
{
    char *p;
    int myNum;
    printf("Type a number: \n");
    scanf("%d", &myNum);

    p = (char *)malloc(myNum * sizeof(char));
    if (p != NULL)
    {
        printf("Memory alocated ");
        printf("%d\n", sizeof(p));
        p[0] = 'j';
        p[1] = myNum + '0';
    }
    return p;
}

void check2()
{
    char* data = other_func();
    printf("Hi %p \n", data);
    printf("Hello there %s\n", data);

    free(data);
}

int main()
{
    check2();
    return 0;
}