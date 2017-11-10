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
    if(c < 91) return (c+32);
    return c;
}

char intCase(char c)
{
    switch(c)
    {
        case 'a':
            return '4';
        case 'A':
            return '4';
        case 'e':
            return '3';
        case 'E':
            return '3';
        case 'o':
            return '0';
        case 'O':
            return '0';
        case 's':
            return '5';
        case 'S':
            return '5';
        case 't':
            return '7';
        case 'T':
            return '7';
        case 'i':
            return '1';
        case 'I':
            return '1';
        default:
            return c;
    }
}


