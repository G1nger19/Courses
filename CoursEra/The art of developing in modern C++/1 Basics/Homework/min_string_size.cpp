#include <iostream>
#include <vector>
#include <string.h>
using namespace std;

int main(){
    vector<string> words={"a","b","c"};
    string word1,word2,word3;
    cin>>word1>>word2>>word3;
    int count1,count2,count3;
    count1=word1.size();
    count2=word2.size();
    count3=word3.size();
    if(count1<count2,count3)cout<<word1;
    else if(count2<count1,count3)cout<<word2;
    else if(count3<count1,count2)cout<<word3;
    else if(count1==count2==count3)cout<<word1;
    else if(count1==count2&&count1<count3)cout<<word1;
    else if(count2==count3&&count2<count1)cout<<word2;
    else cout<<word1;
    return 0;
}