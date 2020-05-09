#include <iostream>
#include <vector>
using namespace std;

int main(){
    int number;
    cin>>number;
    vector<int> bit={};
    vector<int> bit_real={};
    while(number != 0){
        if(number%2 == 0) bit.push_back(0);
        else bit.push_back(1);
        number/=2;
    }
    for(int i=bit.size()-1;i>-1;i--){
        cout<<bit[i];
    }
}