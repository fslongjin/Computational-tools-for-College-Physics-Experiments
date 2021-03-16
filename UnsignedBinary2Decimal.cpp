//这是一个把二进制无符号整数转换为对应的十进制的程序

#include<bits/stdc++.h>
using namespace std;

int unsigned_binary_2_decimal(string bin)//如果是无符号二进制数则返回对应值，否则返回-1
{
    //检验是否为二进制数
    for(auto x:bin)
    {
        if(x-'0'>1)
            return -1;
    }

    int ans=0;
    int len = bin.length();
    for(int i=len-1;i>=0;--i)
    {
        ans+=(bin[i]-'0')*pow(2,len-i-1);
    }
    return ans;
}

int main()
{
    string input;
    cin>>input;
    cout<<unsigned_binary_2_decimal(input)<<endl;
}