
#include <bits/stdc++.h>

using namespace std;

#define t(w) ll w; cin>>w; while(w--) 
#define ipv(v,n) for(ll i=0;i<n;i++){ll a; cin>>a; v.push_back(a);}
#define op(v) for(auto it=v.begin();it<v.end();it++) cout<<*it<<" ";
#define opm(m) for(auto it=m.begin();it!=m.end();it++) cout<<it->first<<"->"<<it->second<<endl;
#define pb push_back
#define all(v) v.begin(), v.end() 

typedef long long int ll; 
typedef unsigned long long int ull; 
typedef vector<ll> vi;

// __builtin_popcount(n));
// lower_bound(v.begin(),v.end(),30);
// binary_s1earch(v.begin(),v.end(),30)   returns bool t/f


vector<ll> seve(1000001,1);

void create_seve(){
  seve[0]=0;
  seve[1]=0;
    for(ll i=2;i<=1000000;i++){
        for(ll j=2;j*j<=i;j++){
            if(i%j==0){
                seve[i]=0;
                break;
            }
        }
    }
}

bool is_prime(ll n){
  // create_seve();
    return seve[n];
} 

vector<pair<ll,ll>> prime_factorization(ll n){
  vector<pair<ll,ll>> pf;
  for(ll i=2;i*i<=n;i++){
    ll c=0;
    while(n%i==0){
      c++;
      n/=i;
    }
    if(c!=0)
      pf.push_back(make_pair(i,c));  
  }
  if(n>1)
    pf.push_back(make_pair(n,1));
  return pf;
}

ll gcd(ll a,ll b){
  return b==0?a:gcd(b,a%b);
}

ull power(ull a,ull n){
  ull ans=1;
  while(n>0){
    if(n&1){
      ans*=a;
    }
    a*=a;
    n=n>>1; 
  }
  return ans;
}

ull modulo_power(ull a,ull n,ull m){
  ull ans=1;
  while(n>0){
    if(n&1){
      ans=(ans*a)%m;
    }
    a=(a*a)%m;
    n=n>>1; 
  }
  return ans%m;
}

ll sumofdig(ll ds){
  ll ans=0;
  while(ds){
    ans+=ds%10;
    ds=ds/10;  
  }
  return ans;
}

bool compare(pair<ll ,ll> i, pair<ll, ll> j) {//asending
  return i.second < j.second;
}

//----------------------------------------------------------------Solution Code---------------------------------------------------------------------------------

bool is_safe(string s[], int i, int j,vector<vector<ll>>&v,int n,int m){
    return i>-1 and j>-1 and i<n and j<m and v[i][j]==-1 and s[i][j]=='.';
}

int find(vector<int>& p,int i){
  if(p[i]==-1){
     return i;
  }
  return find(p,p[i]);
}

void solve(){
    ll n;
    cin>>n;
    ll a=1,ans=0,cnt=0,a1=INT_MAX;
    while(1){
       // cout<<"YES\n";
        ll p=ceil((double)n/(a+cnt));
        ans=p+(a+cnt);
    ans--;
        cnt++;
        if(ans<=a1){
      a1=ans;
        }
    else{
          break;
    }
    }
    cout<<a1-1<<endl;
}


//always call create_seve() in main()
int main(){
  //create_seve();
  // ios_base::sync_with_stdio(false);   
  // cin.tie(NULL);
  // cout.tie(NULL);    
  ll t;
  cin>>t;
  while(t--){
    solve();
  }

  // ll n;
  // cin>>n;
  //vector<ll> v{100,50,40,20,10};
  //reverse(all(v));
  // auto a=lower_bound(v.begin(),v.end(),25,greater<int>());
  // auto b=upper_bound(v.begin(),v.end(),2,greater<int>());
  // cout<<a-v.begin()<<" "<<(b-v.begin());
  // // ipv(v,n);
  // op(v);
  // vector<pair<ll,ll>> a=prime_factorization(999983);
  // for(pair<ll,ll> b:a){
  //   cout<<b.first<<" "<<b.second<<"\n";
  // }
  //cout<<ceil();
  //vector<ll> v{1,2,3,4,5};
  //cout<<v;
  return 0;
}