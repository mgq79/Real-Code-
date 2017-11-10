#include "stdmeme.h"

char *aggroCase(char *str)
{
    int len = strlen(str);
    int madLen = len/2;
    char *result = calloc(sizeof(char), len);
    int i;
    for(i = 0; i < len; i++)
    {
        if(i < madLen) result[i] = downCase(str[i]);
        else           result[i] = upCase(str[i]);
    }
    return result;
}


