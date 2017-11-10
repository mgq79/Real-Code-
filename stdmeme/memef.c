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
                    s = spongeCase(va_arg(args, char*));
                    printf("%s", s);
                    free(s);
                    break;
                case 'a':
                    s = aestheticCase(va_arg(args, char*));
                    printf("%s", s);
                    free(s);
                    break;
                case 'o':
                    s = owOofCase(va_arg(args, char*));
                    printf("%s", s);
                    free(s);
                    break;
                case 'g':
                    s = aggroCase(va_arg(args, char*));
                    printf("%s", s);
                    free(s);
                    break;
                case 'l':
                    s = l33tCase(va_arg(args, char*));
                    printf("%s", s);
                    free(s);
                    break;
                default:
                    printf("<Unrecognized Pattern: %c>", pat[i]);
            }
        }
    }

    va_end(args);
}
