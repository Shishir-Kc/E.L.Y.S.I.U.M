#include <stdio.h>

char *system_info(void){
  #ifdef __WIN32
    return "windows";
  #elif defined(__APPLE__) && defined(__MACH__)
   return "Mac";
  #elif defined(__gnu_linux__)
    return "Linux";
  #else
  return "Unkown" ;
  #endif
  return 0;

}
