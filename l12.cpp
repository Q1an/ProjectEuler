#include <iostream>
#include <string>
using namespace std;

string intToRoman(int num) {
string rt = "";

string roman[13]={"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};
int number[13]={1,4,5,9,10,40,50,90,100,400,500,900,1000};
while (num > 0) {
	for(int i = 12;i>=0;i--){1
		while(num-number[i]>=0){
			rt+=roman[i];
			num-=number[i];
		}
	}
}
return rt;
}

int main()
{
	cout<<intToRoman(499);
}
