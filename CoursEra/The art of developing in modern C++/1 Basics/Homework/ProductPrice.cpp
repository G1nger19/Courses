#include <iostream>

using namespace std;

int main(){
    double n,a,b,x,y;
    cin>>n>>a>>b>>x>>y;
    if(n>a && n<=b){
        cout<<(n-(n/100*x));
    }
    else if(n>b){
        cout<<(n-(n/100*y));
    }
    else{
        cout<<n;
    }
}