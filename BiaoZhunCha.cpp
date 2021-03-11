#include<bits/stdc++.h>
using namespace std;

//计算测量列的标准差

int main()
{
    int n;
    cout<<"正在计算测量列的标准差"<<endl;
    cout<<"请输入总数n: ";
    cin>>n;
    vector<double>nums;

    cout<<"请输入数据："<<endl;
    double total = 0.0;
    for(int i=0;i<n;++i)
    {
        double tmp;
        cin>>tmp;
        total+=tmp;
        nums.push_back(tmp);
    }

    double average = total/n;
    double ans = 0.0;
    for(double x: nums)
    {
        ans+=pow(x-average,2);
    }
    ans/=(n-1);
    ans = sqrt(ans);
    cout<<"\n测量列的标准差为："<<ans<<endl;


}