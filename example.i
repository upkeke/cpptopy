%module example
%{
#define SWIG_FILE_WITH_INIT
#include "example.h"
%}

void hello(string str);

void introduce();
int add(int x, int y);

template<class T>
void h1(T t)
{
	cout<<t<<endl;
}