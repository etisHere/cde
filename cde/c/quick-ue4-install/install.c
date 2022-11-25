#include<stdlib.h>
int main()
{
	char *com = "git clone https://github.com/EpicGames/UnrealEngine && cd UnrealEngine && ./Setup.sh && ./GenerateProjectFiles.sh && make";
	system(com);
	
	return 0;
}
