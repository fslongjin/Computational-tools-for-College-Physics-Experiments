#include <bits/stdc++.h>
using namespace std;

//计算线性相关系数
int main()
{
    int n;
    cout << "请输入总的样本点数量：";

    cin >> n;

    vector<double> x, y;

    cout << "请输入所有的x：" << endl;
    for (int i = 0; i < n; ++i)
    {
        double tmp;
        cin >> tmp;
        x.push_back(tmp);
    }
    cout << "请输入所有的y：" << endl;
    for (int i = 0; i < n; ++i)
    {
        double tmp;
        cin >> tmp;
        y.push_back(tmp);
    }

    double average_x = 0.0;
    for (double tmp : x)
    {
        average_x += tmp;
    }

    average_x /= double(x.size());

    double average_y = 0.0;
    for (double tmp : y)
    {
        average_y += tmp;
    }

    average_y /= double(y.size());

    double up = 0.0;
    double down_l = 0.0,down_r=0.0;

    for (int i = 0; i < n; ++i)
    {
        double a = (x[i] - average_x);
        double b = (y[i] - average_y);
        up += (a * b);
        down_l+=a*a;
        down_r+=b*b;
    }

    double down = sqrt(down_l)*sqrt(down_r);

    double r = up/down;

    printf("线性相关系数：%llf\n",r);
}