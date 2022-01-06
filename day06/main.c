#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void pfish(const char *fishies, const int size) {
  printf("%d: ", size);
  for (int i = 0; i < size; i++) 
    printf("%d ", fishies[i]);
  printf("\n");
}

char* update(char* fishies, int* _size) {
  char* ret;
  int adds = 0;
  int size = *_size;

  for (int i = 0; i < size; i++) {
    char timer = fishies[i];
    if (timer == 0) {
      fishies[i] = 6;
      adds++;
    }
    else
      fishies[i] = timer-1;
  }

  //printf("%x\n", fishies);
  //printf("%d\n", adds);
  if (adds > 0) {
    ret = (char*)realloc(fishies, sizeof(char)*(size+adds));
    if (ret == NULL) {
      free(ret);
      printf("error realloc\n");
      exit(-1);
    }
    fishies = ret;
    for (int i = size; i < size+adds; i++)
      fishies[i] = 8;
    *_size = size + adds;
    return ret;
  }
  return fishies;
}

int main(int argc, char** argv) {
  FILE *fp;  
  char line[500];
  fp = fopen(argv[1], "r");
  fgets(line, 500, fp);
  fclose(fp);
  //printf("%s", line);

  char *fishies;
  fishies = (char*)malloc(sizeof(char)*1);
  int size = 0;
  char *ptr;

  while (1) {
    ptr = (size == 0) ? strtok(line, ",") : strtok(NULL, ",");
    if (ptr == NULL) 
      break;
    if (size > 0)
      fishies = (char*)realloc(fishies, sizeof(char)*(size+1));
    fishies[size++] = atoi(ptr);
  }

  pfish(fishies, size);
  
  char* news;
  int days = 256;
  for (int i = 0; i < days; i++) {
    news = update(fishies, &size);
    fishies = news; 
    //pfish(fishies, size);
  }
  printf("size: %d\n", size);

  free(fishies);
  return 0;
}
