// 입력받은 수가 6의 배수이면 "6의 배수" 출력
// 그렇지 않느면 "no" 
// 6의 배수; %2 ==0, %3 == 0 

/*
 절차
 	1. 변수 선언(kwargs|input, mod2, mod3
	2. input 입력받기 (scanf)
	3. mod2 <- input을 2로 나눈 나머지, mod3 <- 3으로 나눈 나머지 
	4. if(mod2 == 0 & mod3 == 0) "6의 배수" 출력 
*/

#include <stdio.h>


int main() {
	int input, mod2, mod3;
	scanf("%d", &input);
	
	mod2 = input % 2;
	mod3 = input % 3;
	
	if(mod2 || mod3)	printf("no");
	else				printf("6의 배수"); 
	
	return 0;
}

