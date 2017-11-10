#include "stdmeme.h"

char *aestheticCase(char *str)
{
    int len = strlen(str);
    char *result = calloc(sizeof(char),2*len);
    int i;
    for(i = 0; i < len; i++)
    {
        result[2*i]   = str[i];
        result[(2*i+1)] = ' ';
    }
    return result;
}
