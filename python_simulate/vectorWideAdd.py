#-*- coding:utf-8 -*-
import numpy as np
import checkType

##################ARM neon intrinsics#################
##https://developer.arm.com/technologies/neon/intrinsics
#####################################################

############################
##In para:
##a.dtype == "int16x8"
##b.dtype == "int8x8"
##Out para:
##c.dtype == "int16x8"
############################
def vaddw_s8(a, b):
    if checkType.check_int16x8(a) == False or checkType.check_int8x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c.astype(np.int16)


############################
##In para:
##a.dtype == "int32x4"
##b.dtype == "int16x4"
##Out para:
##c.dtype == "int32x4"
############################
def vaddw_s16(a, b):
    if checkType.check_int32x4(a) == False or checkType.check_int16x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c.astype(np.int32)


############################
##In para:
##a.dtype == "int64x2"
##b.dtype == "int32x2"
##Out para:
##c.dtype == "int64x2"
############################
def vaddw_s32(a, b):
    if checkType.check_int64x2(a) == False or checkType.check_int32x2(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c.astype(np.int64)


############################
##In para:
##a.dtype == "uint16x8"
##b.dtype == "uint8x8"
##Out para:
##c.dtype == "uint16x8"
############################
def vaddw_u8(a, b):
    if checkType.check_uint16x8(a) == False or checkType.check_uint8x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c.astype(np.uint16)



############################
##In para:
##a.dtype == "uint32x4"
##b.dtype == "uint16x4"
##Out para:
##c.dtype == "uint32x4"
############################
def vaddw_u16(a, b):
    if checkType.check_uint32x4(a) == False or checkType.check_uint16x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c.astype(np.uint32)


############################
##In para:
##a.dtype == "uint64x2"
##b.dtype == "uint32x2"
##Out para:
##c.dtype == "uint64x2"
############################
def vaddw_u32(a, b):
    if checkType.check_uint64x2(a) == False or checkType.check_uint32x2(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c.astype(np.uint64)



############################
##In para:
##a.dtype == "int16x8"
##b.dtype == "int8x16"
##Out para:
##c.dtype == "int16x8"
############################
def vaddw_high_s8(a, b):
    if checkType.check_int16x8(a) == False or checkType.check_int8x16(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a.astype(np.int16) + b.astype(np.int16)[0, 0:8].reshape((1, 8))
    return c


############################
##In para:
##a.dtype == "int32x4"
##b.dtype == "int16x8"
##Out para:
##c.dtype == "int32x4"
############################
def vaddw_high_s16(a, b):
    if checkType.check_int32x4(a) == False or checkType.check_int16x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a.astype(np.int32) + b.astype(np.int32)[0, 0:4].reshape((1, 4))
    return c


############################
##In para:
##a.dtype == "int64x2"
##b.dtype == "int32x4"
##Out para:
##c.dtype == "int64x2"
############################
def vaddw_high_s32(a, b):
    if checkType.check_int64x2(a) == False or checkType.check_int32x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a.astype(np.int64) + b.astype(np.int64)[0, 0:2].reshape((1, 2))
    return c


############################
##In para:
##a.dtype == "uint16x8"
##b.dtype == "uint8x16"
##Out para:
##c.dtype == "uint16x8"
############################
def vaddw_high_u8(a, b):
    if checkType.check_uint16x8(a) == False or checkType.check_uint8x16(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a.astype(np.uint16) + b.astype(np.uint16)[0, 0:8].reshape((1, 8))
    return c


############################
##In para:
##a.dtype == "uint32x4"
##b.dtype == "uint16x8"
##Out para:
##c.dtype == "uint32x4"
############################
def vaddw_high_u16(a, b):
    if checkType.check_uint32x4(a) == False or checkType.check_uint16x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a.astype(np.uint32) + b.astype(np.uint32)[0, 0:4].reshape((1, 4))
    return c


############################
##In para:
##a.dtype == "uint64x2"
##b.dtype == "uint32x4"
##Out para:
##c.dtype == "uint64x2"
############################
def vaddw_high_u32(a, b):
    if checkType.check_uint64x2(a) == False or checkType.check_uint32x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a.astype(np.uint64) + b.astype(np.uint64)[0, 0:2].reshape((1, 2))
    return c



if __name__ == "__main__":
    length_a = 8
    length_b = 8
    a = np.arange(length_a).reshape(1, length_a)
    b = np.arange(length_b).reshape(1, length_b)
    a = a.astype(np.int16)
    b = b.astype(np.int8)  
    c = vaddw_s8(a, b)
    print("test vaddw_s8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    length_a = 4
    length_b = 4
    a = np.arange(length_a).reshape(1, length_a)
    b = np.arange(length_b).reshape(1, length_b)
    a = a.astype(np.int32)
    b = b.astype(np.int16)  
    c = vaddw_s16(a, b)
    print("test vaddw_s16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length_a = 2
    length_b = 2
    a = np.arange(length_a).reshape(1, length_a)
    b = np.arange(length_b).reshape(1, length_b)
    a = a.astype(np.int64)
    b = b.astype(np.int32)  
    c = vaddw_s32(a, b)
    print("test vaddw_s32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length_a = 8
    length_b = 8
    a = np.arange(length_a).reshape(1, length_a)
    b = np.arange(length_b).reshape(1, length_b)
    a = a.astype(np.uint16)
    b = b.astype(np.uint8)
    c = vaddw_u8(a, b)
    print("test vaddw_u8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    length_a = 4
    length_b = 4
    a = np.arange(length_a).reshape(1, length_a)
    b = np.arange(length_b).reshape(1, length_b)
    a = a.astype(np.uint32)
    b = b.astype(np.uint16)
    c = vaddw_u16(a, b)
    print("test vaddw_u16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length_a = 2
    length_b = 2
    a = np.arange(length_a).reshape(1, length_a)
    b = np.arange(length_b).reshape(1, length_b)
    a = a.astype(np.uint64)
    b = b.astype(np.uint32)  
    c = vaddw_u32(a, b)
    print("test vaddw_u32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length_a = 8
    length_b = 16
    a = np.arange(length_a).reshape(1, length_a)
    b = np.arange(length_b).reshape(1, length_b)
    a = a.astype(np.int16)
    b = b.astype(np.int8)    
    c = vaddw_high_s8(a, b)
    print("test vaddw_high_s8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length_a = 4
    length_b = 8
    a = np.arange(length_a).reshape(1, length_a)
    b = np.arange(length_b).reshape(1, length_b)
    a = a.astype(np.int32)
    b = b.astype(np.int16)    
    c = vaddw_high_s16(a, b)
    print("test vaddw_high_s16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length_a = 2
    length_b = 4
    a = np.arange(length_a).reshape(1, length_a)
    b = np.arange(length_b).reshape(1, length_b)
    a = a.astype(np.int64)
    b = b.astype(np.int32)    
    c = vaddw_high_s32(a, b)
    print("test vaddw_high_s32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length_a = 8
    length_b = 16
    a = np.arange(length_a).reshape(1, length_a)
    b = np.arange(length_b).reshape(1, length_b)
    a = a.astype(np.uint16)
    b = b.astype(np.uint8)
    c = vaddw_high_u8(a, b)
    print("test vaddw_high_u8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length_a = 4
    length_b = 8
    a = np.arange(length_a).reshape(1, length_a)
    b = np.arange(length_b).reshape(1, length_b)
    a = a.astype(np.uint32)
    b = b.astype(np.uint16)
    c = vaddw_high_u16(a, b)
    print("test vaddw_high_u16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length_a = 2
    length_b = 4
    a = np.arange(length_a).reshape(1, length_a)
    b = np.arange(length_b).reshape(1, length_b)
    a = a.astype(np.uint64)
    b = b.astype(np.uint32)    
    c = vaddw_high_u32(a, b)
    print("test vaddw_high_u32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

