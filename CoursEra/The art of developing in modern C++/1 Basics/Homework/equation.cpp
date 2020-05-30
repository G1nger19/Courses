#include <iostream>
#include <math.h>
using namespace std;


int main(){
    double a,b,c;
    cin>>a>>b>>c;
    double x1,x2;
    double dic=b*b-4*a*c;
    if(a!=0){
    x1=(-b+sqrt(dic))/(2*a);
    x2=(-b-sqrt(dic))/(2*a);
    }
    else if(b!=0)x1=-(c/b);
    else return 0;
    
    if(dic>=0){
        if(x1==x2){
            cout<<x1;
        }
        else if(a!=0)cout<<x1<<" "<<x2;
        else cout<<x1;
    }
    else return 0;
/* 
if (A == 0) {
    
    // Bx = -C => x = -C / B
    if (B != 0) {
      cout << -C / B << endl;
    }
    // если B равно нулю, корней нет
    
  } else if (D == 0) {  // случай с нулевым дискриминантом
    
    // корень ровно один
    cout << -B / (2 * A) << endl;
    
  } else if (D > 0) {  // в случае с положительным дискриминантом корня два
  
    double r1 = (-B + sqrt(D)) / (2 * A);
    double r2 = (-B - sqrt(D)) / (2 * A);

    cout << r1 << " " << r2 << endl;
    
  }
*/
}