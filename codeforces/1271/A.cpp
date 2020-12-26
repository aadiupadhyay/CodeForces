/*
                              _,add8ba,
                            ,d888888888b,
                           d8888888888888b                        _,ad8ba,_
                          d888888888888888)                     ,d888888888b,
                          I8888888888888888 _________          ,8888888888888b
                __________`Y88888888888888P"""""""""""baaa,__ ,888888888888888,
            ,adP"""""""""""9888888888P""^                 ^""Y8888888888888888I
         ,a8"^           ,d888P"888P^                           ^"Y8888888888P'
       ,a8^            ,d8888'                                     ^Y8888888P'
      a88'           ,d8888P'                                        I88P"^
    ,d88'           d88888P'                                          "b,
   ,d88'           d888888'                                            `b,
  ,d88'           d888888I                                              `b,
  d88I           ,8888888'            ___                                `b,
 ,888'           d8888888          ,d88888b,              ____            `b,
 d888           ,8888888I         d88888888b,           ,d8888b,           `b
,8888           I8888888I        d8888888888I          ,88888888b           8,
I8888           88888888b       d88888888888'          8888888888b          8I
d8886           888888888       Y888888888P'           Y8888888888,        ,8b
88888b          I88888888b      `Y8888888^             `Y888888888I        d88,
Y88888b         `888888888b,      `""""^                `Y8888888P'       d888I
`888888b         88888888888b,                           `Y8888P^        d88888
 Y888888b       ,8888888888888ba,_          _______        `""^        ,d888888
 I8888888b,    ,888888888888888888ba,_     d88888888b               ,ad8888888I
 `888888888b,  I8888888888888888888888b,    ^"Y888P"^      ____.,ad88888888888I
  88888888888b,`888888888888888888888888b,     ""      ad888888888888888888888'
  8888888888888698888888888888888888888888b_,ad88ba,_,d88888888888888888888888
  88888888888888888888888888888888888888888b,`"""^ d8888888888888888888888888I
  8888888888888888888888888888888888888888888baaad888888888888888888888888888'
  Y8888888888888888888888888888888888888888888888888888888888888888888888888P
  I888888888888888888888888888888888888888888888P^  ^Y8888888888888888888888'
  `Y88888888888888888P88888888888888888888888888'     ^88888888888888888888I
   `Y8888888888888888 `8888888888888888888888888       8888888888888888888P'
    `Y888888888888888  `888888888888888888888888,     ,888888888888888888P'
     `Y88888888888888b  `88888888888888888888888I     I888888888888888888'
       "Y8888888888888b  `8888888888888888888888I     I88888888888888888'
         "Y88888888888P   `888888888888888888888b     d8888888888888888'
            ^""""""""^     `Y88888888888888888888,    888888888888888P'
                            "8888888888888888888b,   Y888888888888P^
                             `Y888888888888888888b   `Y8888888P"^
                                "Y8888888888888888P     `""""^
                                  `"YY88888888888P'
                                       ^""""""""'
*/
//Divyanshu Srivastava

#include <bits/stdc++.h>

using namespace std;

#define t(w)  \
    ll w;     \
    cin >> w; \
    while (w--)

#define ipv(v, n)              \
    for (ll i = 0; i < n; i++) \
    {                          \
        ll a;                  \
        cin >> a;              \
        v.push_back(a);        \
    }

#define op(v)                                     \
    for (auto it = v.begin(); it < v.end(); it++) \
        cout << *it << " ";

#define opm(m)                                     \
    for (auto it = m.begin(); it != m.end(); it++) \
        cout << it->first << " " << it->second << endl;

#define counter(v)   \
    map<ll, ll> feq; \
    for (auto a : v) \
        feq[a]++;

#define pb push_back
#define all(v) v.begin(), v.end()
#define MX 1000000007

typedef long long int ll;
typedef unsigned long long int ull;
typedef vector<ll> vi;

void solve()
{
    ll a, b, c, d, e, f;
    cin >> a >> b >> c >> d >> e >> f;

    ll ans1 = min(a, d) * e + min(b, min(c, d - min(a, d))) * f;
    ll ans2 = min(b, min(c, d)) * f + min(a, d - min(b, min(c, d))) * e;
    cout << max(ans1, ans2) << endl;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    //t(w)
    {
        solve();
    }
    return 0;
}