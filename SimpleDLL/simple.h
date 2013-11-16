#if !defined(SIMPLE_H)
#define SIMPLE_H

#if defined(TESTSIMPLEDLL_EXPORTS)
#define SIMPLE_DLL_API __declspec(dllexport)
#else
#define SIMPLE_DLL_API __declspec(dllimport)
#endif

extern "C" SIMPLE_DLL_API int TakeReturnInt(int src);
extern "C" SIMPLE_DLL_API void TakeArgEasy(bool b_in, int i_in, double d_in, bool *p_b, int *p_i);
extern "C" SIMPLE_DLL_API double TakeArg(bool b_in, int i_in, double d_in, double *p_d, bool *p_b, int *p_i);
extern "C" SIMPLE_DLL_API void TakeVarArgEasy(void *argv[]);
extern "C" SIMPLE_DLL_API double TakeVarArg(void *argv[]);
#endif
