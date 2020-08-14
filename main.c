#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc,char ** argv)
{
    if(argc < 2)
    {
        system("/usr/bin/python3 ./main.py");
    }
    else if(argc == 2)
    {
        if(strcmp(argv[1],"-h")||strcmp(argv[1],"--help"))
        {
            printf("parser [src_file]\nif [src_file] is given,use [src_file] replace original one.\n");
            exit(0);
        }
        else{
            char s[4096];
            sprintf(s,"cp %s ./core/src.core",argv[1]);
            system(s);
        }
    }
    else{
        printf("parser [src_file]\nif [src_file] is given,use [src_file] replace original one.\n");
        exit(1);
    }
    exit(0);
}