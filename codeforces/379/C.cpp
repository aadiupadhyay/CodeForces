#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

#define _int64 long long

int a[500000];
int d[500000];

int main()
{
  int i,n,last;
  vector<pair<int,int> > aa;
  scanf("%d",&n);
  aa.clear();
  for (i=0;i<n;i++)
  {
    scanf("%d",&a[i]);
    aa.push_back(make_pair(a[i],i));
  }
  sort(aa.begin(),aa.end());
  last=0;
  for (i=0;i<aa.size();i++)
  {
    if (aa[i].first>last+1)
    {
      d[aa[i].second]=aa[i].first;
      last=aa[i].first;
    }
    else
    {
      d[aa[i].second]=last+1;
      last=last+1;
    }
  }
  for (i=0;i<n;i++)
  {
    if (i!=0) printf(" ");
    printf("%d",d[i]);
  }
  printf("\n");
  return 0;
}
