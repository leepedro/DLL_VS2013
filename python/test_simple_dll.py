import ctypes

if __name__ == '__main__':
    # Load a DLL file.
    lib1 = ctypes.WinDLL('SimpleDLL.dll')

    funcTakeReturnInt = getattr(lib1, "TakeReturnInt")
    print(funcTakeReturnInt(2))
    
    b_in = True
    i_in = 2
    d_in = 3.0
    b_out = False   # dummy
    i_out = 0       # init
    c_d_in = ctypes.c_double(d_in)
    c_b_out = ctypes.c_bool(b_out)
    c_i_out = ctypes.c_int(i_out)
    p_c_b_out = ctypes.pointer(c_b_out)
    p_c_i_out = ctypes.pointer(c_i_out)
    funcTakeArgEasy = getattr(lib1, "TakeArgEasy")
    funcTakeArgEasy(b_in, i_in, c_d_in, p_c_b_out, p_c_i_out)
    print("Output = {0}, {1}".format(p_c_b_out.contents.value, p_c_i_out.contents.value))
    
    funcTakeArg = getattr(lib1, "TakeArg")

    funcTakeVarArgEasy = getattr(lib1, "TakeVarArgEasy")
    c_b_in = ctypes.c_bool(b_in)
    c_i_in = ctypes.c_int(i_in)
    arg = [b_in, i_in, b_out, i_out]
    
    funcTakeVarArg = getattr(lib1, "TakeVarArg")
    
    print("Completed")
