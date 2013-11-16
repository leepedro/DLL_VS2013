import ctypes
import numpy as np

if __name__ == '__main__':
    # Load a DLL file.
    lib1 = ctypes.WinDLL('SimpleDLL.dll')

    funcTakeReturnInt = getattr(lib1, "TakeReturnInt")
    i_out = funcTakeReturnInt(2)
    print(i_out)
    
    b_in = True
    i_in = 2
    d_in = 3.0
    b_out = False   # dummy init
    i_out = 0       # dummy init
    c_d_in = ctypes.c_double(d_in)
    c_b_out = ctypes.c_bool(b_out)
    c_i_out = ctypes.c_int(i_out)
    p_c_b_out = ctypes.pointer(c_b_out)
    p_c_i_out = ctypes.pointer(c_i_out)
    funcTakeArgEasy = getattr(lib1, "TakeArgEasy")
    funcTakeArgEasy(b_in, i_in, c_d_in, p_c_b_out, p_c_i_out)
    print("Output = {0}, {1}".format(p_c_b_out.contents.value, p_c_i_out.contents.value))
    
    d_array_in = np.array([3.0, 4.0])
    p_c_d_array = d_array_in.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    funcTakeArg = getattr(lib1, "TakeArg")
    d_out = funcTakeArg(b_in, i_in, c_d_in, p_c_d_array, p_c_b_out, p_c_i_out)
    print(d_out)
    
    funcTakeVarArgEasy = getattr(lib1, "TakeVarArgEasy")
    argv = ctypes.c_void_p * 4
    c_argv = argv(ctypes.pointer(b_in), ctypes.pointer(i_in), p_c_b_out, p_c_i_out)
    funcTakeVarArgEasy(arg)
#    
#    funcTakeVarArg = getattr(lib1, "TakeVarArg")
    
    print("Completed")
