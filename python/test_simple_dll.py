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
    d_array = np.array([3.0, 4.0])
    p_c_d_array = d_array.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    c_sz_d_in = ctypes.c_size_t(d_array.size)
    c_b_out = ctypes.c_bool(False)
    c_i_out = ctypes.c_int(0)
    i_array = np.array([3, 4], dtype=np.int)
    p_c_i_array = i_array.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
    c_sz_i_in = ctypes.c_size_t(i_array.size)
    p_c_b_out = ctypes.pointer(c_b_out)
    p_c_i_out = ctypes.pointer(c_i_out)
    print("Input = {0}, {1}".format(b_in, i_in))
    print("Ref (before) = {0}, {1}".format(i_array[0], i_array[1]))
    print("Ref (before) = {0}, {1}".format(d_array[0], d_array[1]))
    
    # Load a DLL file, get a function, and then call the function.
    lib1 = ctypes.WinDLL('SimpleDLL.dll')
    funcTakeArg = getattr(lib1, "TakeArg")
    funcTakeArg.argtypes = [ctypes.c_bool, ctypes.c_int, ctypes.c_double,
                            ctypes.POINTER(ctypes.c_double), ctypes.c_size_t,
                            ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_int),
                            ctypes.POINTER(ctypes.c_int), ctypes.c_size_t]
    funcTakeArg.restype = ctypes.c_double
    d_out = funcTakeArg(b_in, i_in, c_d_in, p_c_d_array, c_sz_d_in, p_c_b_out, p_c_i_out,
                        p_c_i_array, c_sz_i_in)
    
    # Check arguments again.
    print("Output = {0}, {1}, {2}".format(c_b_out.value, c_i_out.value, d_out))
    print("Ref (after) = {0}, {1}".format(i_array[0], i_array[1]))
    print("Ref (after) = {0}, {1}".format(d_array[0], d_array[1]))
    
    # Do it again with a 2-D array. It works without reshaping.
    d_array2D = np.array([[3.0, 4.0], [5.0, 6.0]])
    print("Ref (before) = {0}".format(d_array2D))
    p_c_d_array2 = d_array2D.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    c_sz_d_in = ctypes.c_size_t(d_array2D.size)
    d_out = funcTakeArg(b_in, i_in, c_d_in, p_c_d_array2, c_sz_d_in, p_c_b_out, p_c_i_out,
                        p_c_i_array, c_sz_i_in)
    print("Ref (after) = {0}".format(d_array2D))


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
    d_array = np.array([4.0, 5.0])
    p_c_d_array = d_array.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    i_array = np.array([3, 4], dtype=np.int)
    p_c_i_array = i_array.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
    c_b_out = ctypes.c_bool(False)
    c_i_out = ctypes.c_int(0)
    p_c_b_out = ctypes.pointer(c_b_out)
    p_c_i_out = ctypes.pointer(c_i_out)
    argvType = ctypes.c_void_p * 7
    argv = argvType()
    argv[0] = ctypes.cast(p_c_b_in, ctypes.c_void_p)
    argv[1] = ctypes.cast(p_c_i_in, ctypes.c_void_p)
    argv[2] = ctypes.cast(p_c_d_in, ctypes.c_void_p)
    argv[3] = ctypes.cast(p_c_d_array, ctypes.c_void_p)
    argv[4] = ctypes.cast(p_c_i_array, ctypes.c_void_p)
    argv[5] = ctypes.cast(p_c_b_out, ctypes.c_void_p)
    argv[6] = ctypes.cast(p_c_i_out, ctypes.c_void_p)    
#    for arg in argv:
#        print(arg)
    print("Input = {0}, {1}".format(c_b_in.value, c_i_in.value))
    print("Ref (before) = {0}, {1}".format(d_array[0], d_array[1]))
    print("Ref (before) = {0}, {1}".format(i_array[0], i_array[1]))

    # Load a DLL file, get a function, and then call the function.
    lib1 = ctypes.WinDLL('SimpleDLL.dll')
    funcTakeVarArg = getattr(lib1, "TakeVarArg")
    funcTakeVarArg.argtypes = [argvType]
    funcTakeVarArg.restype = ctypes.c_double
    d_out = funcTakeVarArg(argv)
    print("Output = {0}, {1}, {2}".format(c_b_out.value, c_i_out.value, d_out))
    print("Ref (after) = {0}, {1}".format(d_array[0], d_array[1]))
    print("Ref (after) = {0}, {1}".format(i_array[0], i_array[1]))


if __name__ == '__main__':
    testReturnInt()
    testTakeArgEasy()
    testTakeArg()
    testTakeVarArgEasy()
    testTakeVarArg()
    
    print("Completed")
