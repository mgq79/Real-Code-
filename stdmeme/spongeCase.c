#include "stdmeme.h"

char upCase(char c)
{
    if(c < 97) return c;
    if(c < 123) return (c-32);
    return c;
}

char downCase(char c)
{
    if(c < 65) return c;
    if(c < 91) return (c-32);
    return c;
}

char *spongeCase(char *str)
{
    int len = strlen(str);
    char *result = calloc(sizeof(char),len);
    int count = 0;
    int i;
    for(i = 0; i < len, i++){
        if(count % 2 == 0)
            result[i] = upCase(str[i]);
        else
            result[i] = downCase(str[i]);
        count = (count + 1) % 2;
    }
    return result;
}

