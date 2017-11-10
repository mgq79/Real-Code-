#include "stdmeme.h"

char *l33tCase(char *str)
{
    int len = strlen(str);
    int i;
    char *result = calloc(sizeof(char), len);
    for(i = 0; i < len; i++)
    {
        result[i] = intCase(str[i]);
    }
    return result;
}
