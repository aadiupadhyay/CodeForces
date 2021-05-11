#include<bits/stdc++.h>
 
using namespace std;
const int MAXN = 500100;
 
unordered_set<int> grafo[MAXN],s;
vector<int> vec;
 
void dfs(int x){
	vec.push_back(x);
	
	vector<int> v;
	
	for(auto i : s){
		if(grafo[x].find(i) != grafo[x].end()) continue;
		v.push_back(i);
	}
	
	for(int i = 0;i < v.size();i++) s.erase(v[i]);
	for(int i = 0;i < v.size();i++) dfs(v[i]);
}
 
int main(){
	int n,m;
	scanf("%d %d",&n,&m);
	
	for(int i = 1;i <= n;i++) s.insert(i);
	
	for(int i = 1;i <= m;i++){
		int x,y;
		scanf("%d %d",&x,&y);
		grafo[x].insert(y);
		grafo[y].insert(x);
	}	
	
	int cnt = 0;
	
	vector<int> resp;
	
	for(int i = 1;i <= n;i++){
		if(s.find(i) == s.end()) continue;
		vec.clear();
		s.erase(i);
		dfs(i);
		cnt ++;
		resp.push_back((int) vec.size());
		for(int j = 0;j < vec.size();j++) resp.push_back(vec[j]);
		resp.push_back(-1);
	}
	
	printf("%d\n",cnt);
	
	for(int i = 0;i < resp.size();i++){
		if(resp[i] == -1) printf("\n");
		else printf("%d ",resp[i]);
	}
}