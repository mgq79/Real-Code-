#include "stdmeme.h"


void memef(char *pat, ...)
{
    int len = strlen(pat);
    int i;
    va_list args;
    char *s;

    va_start(args, pat);

    for(i = 0; i < len; i++)
    {
        if(pat[i] != '%')
            printf("%c", pat[i]);
        else
        {
            i++;
            switch(pat[i])
            {
                case 's':
                    printf("%s", spongeCase(va_arg(args, char*)));
                    break;
                case 'a':
                    printf("%s", aestheticCase(va_arg(args, char*)));
                    break;
                case 'o':
                    printf("%s", owOofCase(va_arg(args, char*)));
                    break;
                case 'g':
                    printf("%s", aggroCase(va_arg(args, char*)));
                    break;
                case 'l':
                    printf("%s", l33tCase(va_arg(args, char*)));
                    break;
                default:
                    printf("<Unrecognized Pattern: %c>", pat[i]);
            }
        }
    }

    va_end(args);
}
