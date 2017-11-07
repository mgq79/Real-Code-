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
