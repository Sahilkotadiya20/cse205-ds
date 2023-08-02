int sumOfMultiples(int n){
int sum=0,a;
for(a=1;a<=n;a++){
    if(a%3==0 || a%5==0 || a%7==0){
        sum=sum+a;
    }
}
return sum;
}