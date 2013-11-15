// TestSimpleDLL.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"

#include "simple.h"

int TakeReturnInt(int src)
{
	return src * 2;
}

void TakeArgEasy(bool b_in, int i_in, double d_in, bool *p_b, int *p_i)
{
	*p_b = !b_in;
	*p_i = i_in + 1;
}

void TakeArg(bool b_in, int i_in, double d_in, double *p_d, bool *p_b, int *p_i)
{
	double d_array_0 = *p_d;
	double d_array_1 = *(p_d + 1);
	*p_b = !b_in;
	*p_i = i_in + 1;
}

void TakeVarArgEasy(void *argv[])
{
	bool b_in = *((bool *)argv[0]);
	int i_in = *((int *)argv[1]);

	bool *p_b = (bool *)(argv[2]);
	int *p_i = (int *)(argv[3]);

	*p_b = !b_in;
	*p_i = i_in + 1;
}

void TakeVarArg(void *argv[])
{
	bool b_in = *((bool *)argv[0]);
	int i_in = *((int *)argv[1]);
	double d_in = *((double *)argv[2]);
	double *p_d = (double *)(argv[3]);
	double d_array_0 = *p_d;
	double d_array_1 = *(p_d + 1);

	bool *p_b = (bool *)(argv[4]);
	int *p_i = (int *)(argv[5]);

	*p_b = !b_in;
	*p_i = i_in + 1;
}
