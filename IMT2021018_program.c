#include<stdio.h>
int main(){
    printf("Perform:\n");
    printf("1. Addition of 10 numbers\n");
    printf("2. Multiplication of two numbers\n");
    printf("3. Greater of two numbers\n");
    int n;
    scanf("%d",&n);
    if (n==1){
        int sum=0;
        for(int i=0;i<10;i++){
            int temp;
            scanf("%d",&temp);
            sum=sum+temp;
        }
        printf("%d",sum);
        return 0;
    }
    else if (n==2){
        int a,b;
        scanf("%d",&a);
        scanf("%d",&b);
        printf("%d",a*b);
        return 0;
    }
    else if (n==3){
        int a,b;
        scanf("%d",&a);
        scanf("%d",&b);

        if (a>b){
            printf("%d",a);
            return 0;
        }
        printf("%d",b);
        return 0;
    }
}