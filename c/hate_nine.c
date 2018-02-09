#include <stdio.h>
long long hate_nine(long long  number);
int main(void){
	int test_cases=0,i;
	long long number;
	number=0;
	scanf("%d",&test_cases);
	for(i=0;i<test_cases;i++){
		scanf("%lld",&number);
		printf("%lld\n",(hate_nine(number-1)*8)%1000000007);
	}

}

long long hate_nine(long long number){
	long long arr[100]={0};
	long long counter=0, counter_two,counter_three,result=1;
	counter_three=9;
	while(1){
		if(number==0){
			break;
		}
		if(number%2 == 1){
			arr[counter] = 1;
		}
		counter++;
		number /= 2;
	}
	for(counter_two=0;counter_two<counter;counter_two++){
		if(arr[counter_two]==1){
			result*=counter_three;
			result=result%1000000007;	

		}
		counter_three*=counter_three;
		counter_three=counter_three%1000000007;
	}
	return result;
}


/*
long long hate_nine(long long number){
	if(number==0){
		return 1;
	}
	else if(number%2==0){

		return (hate_nine(number/2)*hate_nine(number/2))%1000000007;
	}
	else if(number%2==1){
		return (((hate_nine(number/2)*hate_nine(number/2))%1000000007)*9)%1000000007;
	}
}
*/




/*USELESS function  part 3


long long hate_nine(long long number){
	if(number==0){
		return 1;
	}
	else if(number%2==0){
		return (hate_nine(number/2)*hate_nine(number/2))%1000000007;
	}
	else if(number%2==1){
		return (((hate_nine(number/2)*hate_nine(number/2))%1000000007)*9)%1000000007;
	}
}


*/




/*
//USELESS function (part 2)

long long hate_nine(long long number){
	long long counter,sum;
	sum=8;
	for(counter=number-1;counter>0;counter--){
		sum*=9;
		sum%=1000000007;
	}
	return sum;
}

*/

/*
//USELESS function

long long hate_nine(long long number){
	if((number-1)==0){
		return 8;
	}
	else{
		return hate_nine(number-1)*9%1000000007;
	}
		
}

*/