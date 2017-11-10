#include "stdmeme.h"

char *owOofCase(char *str)
{
    int len = strlen(str);
    int resultLen = 0;
    int i;
    for(i = 0; i < len; i++)
    {
        if     (str[i] < 65)  resultLen += 1;
        else if(str[i] < 91)  resultLen += 3;
        else if(str[i] < 97)  resultLen += 1;
        else if(str[i] < 123) resultLen += 3;
        else resultLen += 1;
    }

    char *result = calloc(sizeof(char), resultLen);
    char f = '*';
    int resultIndex = 0;
    for(i = 0; i < len; i++)
    {

        if     (str[i] < 65)
        {
            result[resultIndex] = str[i];
            resultIndex++;
        }
        else if(str[i] < 91)
        {
            result[resultIndex] = f;
            result[resultIndex+1] = str[i];
            result[resultIndex+2] = f;
            resultIndex += 3;

            if(f == '*') f = '_';
            else         f = '*';
        }
        else if(str[i] < 97)
        {
            result[resultIndex] = str[i];
            resultIndex++;
        }
        else if(str[i] < 123)
        {
            result[resultIndex] = f;
            result[resultIndex+1] = str[i];
            result[resultIndex+2] = f;
            resultIndex += 3;

            if(f == '*') f = '_';
            else         f = '*';
        }
    }
    return result;
}
