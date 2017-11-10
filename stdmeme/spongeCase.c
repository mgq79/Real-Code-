#include "stdmeme.h"

char *spongeCase(char *str)
{
    int len = strlen(str);
    char *result = calloc(sizeof(char),len);
    int count = 0;
    int i;
    for(i = 0; i < len; i++){
        if(count % 2 == 0)
            result[i] = upCase(str[i]);
        else
            result[i] = downCase(str[i]);
        count = (count + 1) % 2;
    }
    return result;
}

