#include <algorithm>
#include <iostream>
#include <string>


using namespace std;

int main(){
    string s;
    cin>>s;
    int CountOfF=count(begin(s),end(s),'f');
    if(CountOfF == 0) cout<<"-2";
    else if(CountOfF == 1) cout<<"-1";
    else{
        int k=0;
        int index=0;
        for(auto c : s){
            if(c == 'f')++k;
            if(k == 2){
                cout<<index;
                break;
            }
            index++;
        }
    }
}