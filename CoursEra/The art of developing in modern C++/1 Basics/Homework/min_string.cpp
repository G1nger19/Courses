#include <iostream>
#include <vector>
#include <string.h>
using namespace std;

int main(){
    vector<string> words={"a","b","c"};
    string word1,word2,word3;
    cin>>word1>>word2>>word3;
    if(word1<word2&&word1<word3)cout<<word1;
    else if(word2<word1&&word2<word3)cout<<word2;
    else if(word3<word1&&word3<word2)cout<<word3;
    else if(word1==word2&&word1<word3)cout<<word1;
    else if(word2==word3&&word2<word1)cout<<word2;
    else cout<<word1;
    return 0;
    /*
    if (a <= b && a <= c) {
    cout << a;
  } else if (b <= a && b <= c) {
    cout << b;
  } else {
    cout << c;
  }*/
}