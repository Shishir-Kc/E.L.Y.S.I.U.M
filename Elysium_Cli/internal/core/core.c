// This is the main file that runs the logic for the CLI from here . 
#include <stdio.h>
#include <string.h>
#include "commands/help/help.h"
#include "commands/system_info/system_info.h"
#include "internal/parse/parse.h"




char *logic(char *input){

    // for initial development hardcoded logic will be used but in near future changes 
    //   functiongemma will be used to make the calls !. 

  if (strcmp(input,"help")==0){
    return help();
  }
  else if (strcmp(input ,"system_info")==0){
    return system_info();
  }

  else{
      return "unknown command";
    }
  
}
int run(void) {
    char input[100];
    while (1) {
        printf("> ");
        fflush(stdout);
        fgets(input, 100, stdin);
        input[strcspn(input, "\n")] = 0;

        char *cmd = parse(input);
        if (cmd == NULL) continue;

        printf("%s\n", logic(cmd));
    }
}
