#include <iostream>
#include <cstdio>
using namespace std;

#define RUN 0
#define TEST 1
#define PRG_MODE TEST  //or RUN

#if (PRG_MODE == TEST)
void test(bool test_result){
	if (test_result == true){
		cout << "Pass" << endl;
	}else{
		cout << "FAIL" << endl;
		exit(1);
	}
}
#endif

int sum(int a, int b = 1){
    return a+b;
}

int main() {
	#if (PRG_MODE == RUN)
    cout << "The sum is: ";
    cout << sum(6, 2) << endl;

	#elif (PRG_MODE == TEST)
    cout << "TEST mode." << endl;
	cout << "1. The function enter 4 and 6, the result is 10." << endl;
	test(sum(4,6) == 10);

	cout << "2. The function enter 4 and -5, the result is -1." << endl;
	test(sum(4,-5) == -1);
	#else
	cout << "This PRG_MODE option is not valid!" << endl;
	#endif
    return 0;
}
