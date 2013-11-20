import ctypes
import numpy as np


def testReturnInt():
    print("\nTakeReturnInt")
    
    # Load a DLL file, get a function, and then call the function.
    lib1 = ctypes.WinDLL('SimpleDLL.dll')
    funcTakeReturnInt = getattr(lib1, "TakeReturnInt")
    i_out = funcTakeReturnInt(2)
    
    print(i_out)


def testTakeArgEasy():
    print("\nTakeArgEasy")

    # Prepare and check arguments.    
    b_in = True
    i_in = 2
    c_d_in = ctypes.c_double(3.0)
    c_b_out = ctypes.c_bool(False)
    c_i_out = ctypes.c_int(0)
    p_c_b_out = ctypes.pointer(c_b_out)
    p_c_i_out = ctypes.pointer(c_i_out)
    print("Input = {0}, {1}".format(b_in, i_in))
    print("Initialized output = {0}, {1}".format(c_b_out.value, c_i_out.value))

    # Load a DLL file, get a function, and then call the function.
    lib1 = ctypes.WinDLL('SimpleDLL.dll')
    funcTakeArgEasy = getattr(lib1, "TakeArgEasy")
    funcTakeArgEasy(b_in, i_in, c_d_in, p_c_b_out, p_c_i_out)
    
    # Check arguments again.
    print("Output = {0}, {1}".format(c_b_out.value, c_i_out.value))
    print("Output = {0}, {1}".format(p_c_b_out.contents.value, p_c_i_out.contents.value))


def testTakeArg():
    print("\nTakeArg")

    # Prepare and check arguments.
    b_in = True
    i_in = 2
    c_d_in = ctypes.c_double(3.0)
    d_array_in = np.array([3.0, 4.0])
    p_c_d_array = d_array_in.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    c_b_out = ctypes.c_bool(False)
    c_i_out = ctypes.c_int(0)
    p_c_b_out = ctypes.pointer(c_b_out)
    p_c_i_out = ctypes.pointer(c_i_out)
    print("Input = {0}, {1}, {2}, {3}".format(b_in, i_in, d_array_in[0], d_array_in[1]))
    
    # Load a DLL file, get a function, and then call the function.
    lib1 = ctypes.WinDLL('SimpleDLL.dll')
    funcTakeArg = getattr(lib1, "TakeArg")
    funcTakeArg.argtypes = [ctypes.c_bool, ctypes.c_int, ctypes.c_double,
                            ctypes.POINTER(ctypes.c_double),
                            ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_int)]
    funcTakeArg.restype = ctypes.c_double
    d_out = funcTakeArg(b_in, i_in, c_d_in, p_c_d_array, p_c_b_out, p_c_i_out)
    
    # Check arguments again.
    print("Output = {0}, {1}, {2}".format(c_b_out.value, c_i_out.value, d_out))


def testTakeVarArgEasy():
    print("\nTakeVarArgEasy")
    
    # Prepare and check arguments.
    c_b_in = ctypes.c_bool(True)
    c_i_in = ctypes.c_int(2)
    p_c_b_in = ctypes.pointer(c_b_in)
    p_c_i_in = ctypes.pointer(c_i_in)
    c_b_out = ctypes.c_bool(False)
    c_i_out = ctypes.c_int(0)
    p_c_b_out = ctypes.pointer(c_b_out)
    p_c_i_out = ctypes.pointer(c_i_out)    
    argvType = ctypes.c_void_p * 4
    argv = argvType()
    argv[0] = ctypes.cast(p_c_b_in, ctypes.c_void_p)
    argv[1] = ctypes.cast(p_c_i_in, ctypes.c_void_p)
    argv[2] = ctypes.cast(p_c_b_out, ctypes.c_void_p)
    argv[3] = ctypes.cast(p_c_i_out, ctypes.c_void_p)
#    for arg in argv:
#        print(arg)
    print("Input = {0}, {1}".format(c_b_in.value, c_i_in.value))
    
    # Load a DLL file, get a function, and then call the function.
    lib1 = ctypes.WinDLL('SimpleDLL.dll')
    funcTakeVarArgEasy = getattr(lib1, "TakeVarArgEasy")
    funcTakeVarArgEasy.argtypes = [argvType]
    funcTakeVarArgEasy(argv)
    
    # Check arguments again.
    print("Output = {0}, {1}".format(c_b_out.value, c_i_out.value))


def testTakeVarArg():
    print("\nTakeVarArg")
    
    # Prepare and check arguments.
    c_b_in = ctypes.c_bool(True)
    c_i_in = ctypes.c_int(2)
    p_c_b_in = ctypes.pointer(c_b_in)
    p_c_i_in = ctypes.pointer(c_i_in)
    c_d_in = ctypes.c_double(3.0)
    p_c_d_in = ctypes.pointer(c_d_in)
    d_array_in = np.array([4.0, 5.0])
    p_c_d_array = d_array_in.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    c_b_out = ctypes.c_bool(False)
    c_i_out = ctypes.c_int(0)
    p_c_b_out = ctypes.pointer(c_b_out)
    p_c_i_out = ctypes.pointer(c_i_out)
    argvType = ctypes.c_void_p * 6
    argv = argvType()
    argv[0] = ctypes.cast(p_c_b_in, ctypes.c_void_p)
    argv[1] = ctypes.cast(p_c_i_in, ctypes.c_void_p)
    argv[2] = ctypes.cast(p_c_d_in, ctypes.c_void_p)
    argv[3] = ctypes.cast(p_c_d_array, ctypes.c_void_p)
    argv[4] = ctypes.cast(p_c_b_out, ctypes.c_void_p)
    argv[5] = ctypes.cast(p_c_i_out, ctypes.c_void_p)    
#    for arg in argv:
#        print(arg)
    print("Input = {0}, {1}, {2}, {3}".format(c_b_in.value, c_i_in.value, d_array_in[0],
          d_array_in[1]))

    # Load a DLL file, get a function, and then call the function.
    lib1 = ctypes.WinDLL('SimpleDLL.dll')
    funcTakeVarArg = getattr(lib1, "TakeVarArg")
    funcTakeVarArg.argtypes = [argvType]
    funcTakeVarArg.restype = ctypes.c_double
    d_out = funcTakeVarArg(argv)
    print("Output = {0}, {1}, {2}".format(c_b_out.value, c_i_out.value, d_out))


if __name__ == '__main__':
    testReturnInt()
    testTakeArgEasy()
    testTakeArg()
    testTakeVarArgEasy()
    testTakeVarArg()
    
    print("Completed")
