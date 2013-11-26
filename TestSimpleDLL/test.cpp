#include "../SimpleDLL/simple.h"

void TestReturnInt(void)
{
	int i_return = TakeReturnInt(2);
}

void TestTakeArgEasy(void)
{
	bool b_output;
	int i_output;
	TakeArgEasy(true, 2, 3.0, &b_output, &i_output);
}

void TestTakeArg(void)
{
	const ::size_t SZ = 2;
	double d_array[SZ] = { 4.0, 5.0 };
	int i_array[SZ] = { 4, 5 };
	bool b_output;
	int i_output;
	double d_output = TakeArg(true, 2, 3.0, d_array, SZ, &b_output, &i_output, i_array, SZ);
}

void TestVarArgEasy(void)
{
	bool b_input(true);
	int i_input(2);
	bool b_output;
	int i_output;

	void *argv[4];
	argv[0] = &b_input;
	argv[1] = &i_input;
	argv[2] = &b_output;
	argv[3] = &i_output;

	TakeVarArgEasy(argv);
}

void TestVarArg(void)
{
	bool b_input(true);
	int i_input(3);
	double d_input(2.0);
	double d_array[] = { 3.0, 4.0 };
	bool b_output;
	int i_output;

	void *argv[6];
	argv[0] = &b_input;
	argv[1] = &i_input;
	argv[2] = &d_input;
	argv[3] = d_array;
	argv[4] = &b_output;
	argv[5] = &i_output;

	double d_output = TakeVarArg(argv);
}

int main(void)
{
	TestReturnInt();
	TestTakeArgEasy();
	TestTakeArg();
	TestVarArgEasy();
	TestVarArg();
}