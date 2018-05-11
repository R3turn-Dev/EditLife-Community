// Created At: 2018-05-11 KST 19:39
// Author: return0927 이은학 

// 입력받은 수가 짝수인지 홀수인지 알아내는 프로그램.
// 짝수: 2의 배수: 	2로 나눈 나머지가 0인 수
// 홀수: 			2로 나눈 나머지가 1인 수	2로 나눈 나머지가 0이 아닌 수 
/*
	절차
		1. 변수 선언 (kwargs| tg: integer, mod: integer)
		2. tg값 입력받기(scanf)
		3. tg를 2로 나눈 나머지(%) 계산하여 mod에 대입
		4. mod가 0이면 `짝수`라고 출력
		5. mod가 1이면, `홀수`라고 출력 
		
	파일 이름: even-odd.c 
*/
#include <stdio.h>


int main() {
	int tg, mod;
	
	printf("정수 입력: ");
	scanf("%d", &tg);
	
	mod = tg % 2;
	
	// Method 1
	if(mod)	printf("홀수\n");
	else	printf("짝수\n");
	
	// Method 2
	if(mod == 0)	printf("짝수\n");
	if(mod == 1)	printf("홀수\n");
	
	// Method 3
	if(mod == 0)	printf("짝수\n");
	else			printf("홀수\n");
	
	
	return 0;
}
