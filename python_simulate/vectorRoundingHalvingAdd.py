#-*- coding:utf-8 -*-
import numpy as np
import checkType



#########################  SRHADD  ########################################
#https://developer.arm.com/docs/ddi0596/a/a64-simd-and-floating-point-instructions-alphabetic-order/srhadd-signed-rounding-halving-add
#Signed Halving Add. This instruction adds corresponding signed integer 
# values from the two source SIMD&FP registers, shifts each result right
#  one bit, places the results into a vector, and writes the vector to 
# the destination SIMD&FP register.
######################################################################


############################
##In para:
##a.dtype == "int8x8"
##b.dtype == "int8x8"
##Out para:
##c.dtype == "int8x8"
############################
def vrhadd_s8 (a, b):
    if checkType.check_int8x8(a) == False or checkType.check_int8x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = np.floor((a + b) / 2 + 0.5).astype(np.int8)
    return c

############################
##In para:
##a.dtype == "int8x16"
##b.dtype == "int8x16"
##Out para:
##c.dtype == "int8x16"
############################
def vrhaddq_s8(a, b):
    if checkType.check_int8x16(a) == False or checkType.check_int8x16(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = np.floor((a + b) / 2 + 0.5).astype(np.int8)
    return c


############################
##In para:
##a.dtype == "int16x4"
##b.dtype == "int16x4"
##Out para:
##c.dtype == "int16x4"
############################
def vrhadd_s16(a, b):
    if checkType.check_int16x4(a) == False or checkType.check_int16x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = np.floor((a + b) / 2 + 0.5).astype(np.int16)
    return c

############################
##In para:
##a.dtype == "int16x8"
##b.dtype == "int16x8"
##Out para:
##c.dtype == "int16x8"
############################
def vrhaddq_s16(a, b):
    if checkType.check_int16x8(a) == False or checkType.check_int16x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = np.floor((a + b) / 2 + 0.5).astype(np.int16)
    return c


############################
##In para:
##a.dtype == "int32x2"
##b.dtype == "int32x2"
##Out para:
##c.dtype == "int32x2"
############################
def vrhadd_s32(a, b):
    if checkType.check_int32x2(a) == False or checkType.check_int32x2(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = np.floor((a + b) / 2 + 0.5).astype(np.int32)
    return c

############################
##In para:
##a.dtype == "int32x4"
##b.dtype == "int32x4"
##Out para:
##c.dtype == "int32x4"
############################
def vrhaddq_s32(a, b):
    if checkType.check_int32x4(a) == False or checkType.check_int32x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = np.floor((a + b) / 2 + 0.5).astype(np.int32)
    return c



############################
##In para:
##a.dtype == "uint8x8"
##b.dtype == "uint8x8"
##Out para:
##c.dtype == "uint8x8"
############################
def vrhadd_u8 (a, b):
    if checkType.check_uint8x8(a) == False or checkType.check_uint8x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = np.floor((a + b) / 2 + 0.5).astype(np.uint8)
    return c

############################
##In para:
##a.dtype == "uint8x16"
##b.dtype == "uint8x16"
##Out para:
##c.dtype == "uint8x16"
############################
def vrhaddq_u8(a, b):
    if checkType.check_uint8x16(a) == False or checkType.check_uint8x16(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = np.floor((a + b) / 2 + 0.5).astype(np.uint8)
    return c


############################
##In para:
##a.dtype == "uint16x4"
##b.dtype == "uint16x4"
##Out para:
##c.dtype == "uint16x4"
############################
def vrhadd_u16(a, b):
    if checkType.check_uint16x4(a) == False or checkType.check_uint16x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = np.floor((a + b) / 2 + 0.5).astype(np.uint16)
    return c

############################
##In para:
##a.dtype == "uint16x8"
##b.dtype == "uint16x8"
##Out para:
##c.dtype == "uint16x8"
############################
def vrhaddq_u16(a, b):
    if checkType.check_uint16x8(a) == False or checkType.check_uint16x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = np.floor((a + b) / 2 + 0.5).astype(np.uint16)
    return c


############################
##In para:
##a.dtype == "int32x2"
##b.dtype == "int32x2"
##Out para:
##c.dtype == "int32x2"
############################
def vrhadd_u32(a, b):
    if checkType.check_uint32x2(a) == False or checkType.check_uint32x2(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = np.floor((a + b) / 2 + 0.5).astype(np.uint32)
    return c

############################
##In para:
##a.dtype == "int32x4"
##b.dtype == "int32x4"
##Out para:
##c.dtype == "int32x4"
############################
def vrhaddq_u32(a, b):
    if checkType.check_uint32x4(a) == False or checkType.check_uint32x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = np.floor((a + b) / 2 + 0.5).astype(np.uint32)
    return c



if __name__ == "__main__":
    length = 8
    a = np.arange(length).reshape(1, length) + 1
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.int8)
    b = b.astype(np.int8)
    c = vrhadd_s8(a, b)
    print("test vrhadd_s8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)    


    length = 16
    a = np.arange(length).reshape(1, length) + 1
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.int8)
    b = b.astype(np.int8)    
    c = vrhaddq_s8(a, b)
    print("test vrhaddq_s8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype) 


    length = 4
    a = np.arange(length).reshape(1, length) + 1
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.int16)
    b = b.astype(np.int16)    
    c = vrhadd_s16(a, b)
    print("test vrhadd_s16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)       


    length = 8
    a = np.arange(length).reshape(1, length) + 1
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.int16)
    b = b.astype(np.int16)    
    c = vrhaddq_s16(a, b)
    print("test vrhaddq_s16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)     



    length = 2
    a = np.arange(length).reshape(1, length) + 1
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.int32)
    b = b.astype(np.int32)    
    c = vrhadd_s32(a, b)
    print("test vrhadd_s32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)       


    length = 4
    a = np.arange(length).reshape(1, length) + 1
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.int32)
    b = b.astype(np.int32)    
    c = vrhaddq_s32(a, b)
    print("test vrhaddq_s32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)     



    length = 8
    a = np.arange(length).reshape(1, length) + 1
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.uint8)
    b = b.astype(np.uint8)    
    c = vrhadd_u8(a, b)
    print("test vrhadd_u8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)    


    length = 16
    a = np.arange(length).reshape(1, length) + 1
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.uint8)
    b = b.astype(np.uint8)    
    c = vrhaddq_u8(a, b)
    print("test vrhaddq_u8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype) 


    length = 4
    a = np.arange(length).reshape(1, length) + 1
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.uint16)
    b = b.astype(np.uint16)    
    c = vrhadd_u16(a, b)
    print("test vrhadd_u16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)       


    length = 8
    a = np.arange(length).reshape(1, length) + 1
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.uint16)
    b = b.astype(np.uint16)    
    c = vrhaddq_u16(a, b)
    print("test vrhaddq_u16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)     



    length = 2
    a = np.arange(length).reshape(1, length) + 1
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.uint32)
    b = b.astype(np.uint32)    
    c = vrhadd_u32(a, b)
    print("test vrhadd_u32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)       


    length = 4
    a = np.arange(length).reshape(1, length) + 1
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.uint32)
    b = b.astype(np.uint32)    
    c = vrhaddq_u32(a, b)
    print("test vrhaddq_u32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)       