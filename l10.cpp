#include <iostream>
using namespace std;
class Solution {
public:
    bool isMatch(string s, string p) {
    	int slen= s.length()+1;
    	int plen= p.length()+1;
        bool** T = new bool*[slen];
        for(int i = 0;i<slen;i++){
        	T[i]=new bool[plen];
        }
        for(int i = 0;i<slen;i++){
        	for(int j=0;j<plen;j++){
        		T[i][j]=false;
        	}
        }
        T[0][0]=true;
        for(int j=2;j<plen;j++){
        	if(p[j-1]=='*'){
        		T[0][j]=T[0][j-2];
        	}
        }
        for(int i=1;i<slen;i++){
        	for(int j=1;j<plen;j++){
        		if(p[j-1]!='*'){
        			T[i][j] = T[i-1][j-1] && (p[j-1]==s[i-1]||p[j-1]=='.');
        		}else{
        			T[i][j] = T[i][j-2] || ((p[j-2]=='.'||p[j-2]==s[i-1])&&T[i-1][j]);
        		}
        	}
        }
        return T[s.length()][p.length()];
    }
};
int main(){
	cout<<Solution().isMatch("aaa","ab*a*c*a");
}

