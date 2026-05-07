
//
// this is just a simple parser right now but in new cahnges it may get complex 
//


#include <stddef.h>


char * parse(char *input){
  if (input[0]=='/'){
    return input+1;
  }
  else{
    return NULL;
  }
}
