#include <bits/stdc++.h>
using namespace std;
int main()
{
int q;
cin >> q;
int l[q+1];
map<int, int> m;
int o;
for(int y=0; y<q; y++)
{
cin >> o;
m[o] = -1;
l[y] = o;
}


int ans[10000000+69];
for(int i=0;i<10000000+69;i++) ans[i] = 1;
m[1] = 1;
for(int i=2; i<=10000000; i++){
    for(int j=i; j<=10000000; j+=i) {
        ans[j] += i; }
    if (m.find(ans[i]) == m.end()) continue;
    if (m[ans[i]] == -1) m[ans[i]] = i;
  }
for(int i=0; i<q; i++) cout << m[l[i]] << "\n";
 

return 0;
}