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

double TakeArg(bool b_in, int i_in, double d_in, double *p_d, ::size_t sz_d, bool *p_b, int *p_i, int *p_i2, ::size_t sz_i)
{
	// Change output value according to given input values.
	*p_b = !b_in;
	*p_i = i_in + 1;

	for (::size_t count = 0; count < sz_i; ++count)
	{
		// Change the content of an input/output array.
		*(p_i2 + count) = *(p_i2 + count) + 10;
	}

	double d_output(0.0);
	for (::size_t count = 0; count < sz_d; ++count)
	{
		// Change output value according to a given array.
		d_output += *(p_d + count);

		// Change the content of an input/output array.
		*(p_d + count) = *(p_d + count) + 10.0;
	}
	return d_output;
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

double TakeVarArg(void *argv[])
{
	bool b_in = *((bool *)argv[0]);
	int i_in = *((int *)argv[1]);
	double d_in = *((double *)argv[2]);
	double *p_d = (double *)(argv[3]);
	double d_array_0 = *p_d;
	double d_array_1 = *(p_d + 1);
	int *p_i_array = (int *)(argv[4]);

	bool *p_b = (bool *)(argv[5]);
	int *p_i = (int *)(argv[6]);

	*p_b = !b_in;
	*p_i = i_in + 1;
	*p_d = *p_d + 10.0;
	*(p_d + 1) = *(p_d + 1) + 10.0;
	*p_i_array = *p_i_array + 10;
	*(p_i_array + 1) = *(p_i_array + 1) + 10;
	return d_array_0 + d_array_1;
}
