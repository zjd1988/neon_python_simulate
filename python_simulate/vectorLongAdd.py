#-*- coding:utf-8 -*-
import numpy as np
import checkType

##################ARM neon intrinsics#################
##https://developer.arm.com/technologies/neon/intrinsics
#####################################################

############################
##In para:
##a.dtype == "int8x8"
##b.dtype == "int8x8"
##Out para:
##c.dtype == "int16x8"
############################
def vaddl_s8(a, b):
    if checkType.check_int8x8(a) == False or checkType.check_int8x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c.astype(np.int16)


############################
##In para:
##a.dtype == "int16x4"
##b.dtype == "int16x4"
##Out para:
##c.dtype == "int32x4"
############################
def vaddl_s16(a, b):
    if checkType.check_int16x4(a) == False or checkType.check_int16x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c.astype(np.int32)


############################
##In para:
##a.dtype == "int32x2"
##b.dtype == "int32x2"
##Out para:
##c.dtype == "int64x2"
############################
def vaddl_s32(a, b):
    if checkType.check_int32x2(a) == False or checkType.check_int32x2(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c.astype(np.int64)


############################
##In para:
##a.dtype == "uint8x8"
##b.dtype == "uint8x8"
##Out para:
##c.dtype == "uint16x8"
############################
def vaddl_u8(a, b):
    if checkType.check_uint8x8(a) == False or checkType.check_uint8x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c.astype(np.uint16)



############################
##In para:
##a.dtype == "uint16x4"
##b.dtype == "uint16x4"
##Out para:
##c.dtype == "uint32x4"
############################
def vaddl_u16(a, b):
    if checkType.check_uint16x4(a) == False or checkType.check_uint16x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c.astype(np.uint32)


############################
##In para:
##a.dtype == "uint32x2"
##b.dtype == "uint32x2"
##Out para:
##c.dtype == "uint64x2"
############################
def vaddl_u32(a, b):
    if checkType.check_uint32x2(a) == False or checkType.check_uint32x2(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c.astype(np.uint64)


############################
##In para:
##a.dtype == "int8x16"
##b.dtype == "int8x16"
##Out para:
##c.dtype == "int16x8"
############################
def vaddl_high_s8(a, b):
    if checkType.check_int8x16(a) == False or checkType.check_int8x16(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a.astype(np.int16) + b.astype(np.int16)
    return c[0, 0:8].reshape((1,8))


############################
##In para:
##a.dtype == "int16x8"
##b.dtype == "int16x8"
##Out para:
##c.dtype == "int32x4"
############################
def vaddl_high_s16(a, b):
    if checkType.check_int16x8(a) == False or checkType.check_int16x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a.astype(np.int32) + b.astype(np.int32)
    return c[0, 0:4].reshape((1,4))


############################
##In para:
##a.dtype == "int32x4"
##b.dtype == "int32x4"
##Out para:
##c.dtype == "int64x2"
############################
def vaddl_high_s32(a, b):
    if checkType.check_int32x4(a) == False or checkType.check_int32x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a.astype(np.int64) + b.astype(np.int64)
    return c[0, 0:2].reshape((1,2))


############################
##In para:
##a.dtype == "uint8x16"
##b.dtype == "uint8x16"
##Out para:
##c.dtype == "uint16x8"
############################
def vaddl_high_u8(a, b):
    if checkType.check_uint8x16(a) == False or checkType.check_uint8x16(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a.astype(np.uint16) + b.astype(np.uint16)
    return c[0, 0:8].reshape((1,8))


############################
##In para:
##a.dtype == "uint16x8"
##b.dtype == "uint16x8"
##Out para:
##c.dtype == "uint32x4"
############################
def vaddl_high_u16(a, b):
    if checkType.check_uint16x8(a) == False or checkType.check_uint16x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a.astype(np.uint32) + b.astype(np.uint32)
    return c[0, 0:4].reshape((1,4))


############################
##In para:
##a.dtype == "uint32x4"
##b.dtype == "uint32x4"
##Out para:
##c.dtype == "uint64x2"
############################
def vaddl_high_u32(a, b):
    if checkType.check_uint32x4(a) == False or checkType.check_uint32x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a.astype(np.uint64) + b.astype(np.uint64)
    return c[0, 0:2].reshape((1,2))


if __name__ == "__main__":
    length = 8
    a = np.arange(length).reshape(1, length)
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.int8)
    b = b.astype(np.int8)    
    c = vaddl_s8(a, b)
    print("test vaddl_s8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    length = 4
    a = np.arange(length).reshape(1, length)
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.int16)
    b = b.astype(np.int16)    
    c = vaddl_s16(a, b)
    print("test vaddl_s16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length = 2
    a = np.arange(length).reshape(1, length)
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.int32)
    b = b.astype(np.int32)
    c = vaddl_s32(a, b)
    print("test vaddl_s32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length = 8
    a = np.arange(length).reshape(1, length)
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.uint8)
    b = b.astype(np.uint8)    
    c = vaddl_u8(a, b)
    print("test vaddl_u8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length = 4
    a = np.arange(length).reshape(1, length)
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.uint16)
    b = b.astype(np.uint16)    
    c = vaddl_u16(a, b)
    print("test vaddl_u16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length = 2
    a = np.arange(length).reshape(1, length)
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.uint32)
    b = b.astype(np.uint32)
    c = vaddl_u32(a, b)
    print("test vaddl_u32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length = 16
    a = np.arange(length).reshape(1, length)
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.int8)
    b = b.astype(np.int8)    
    c = vaddl_high_s8(a, b)
    print("test vaddl_high_s8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length = 8
    a = np.arange(length).reshape(1, length)
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.int16)
    b = b.astype(np.int16)    
    c = vaddl_high_s16(a, b)
    print("test vaddl_high_s16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length = 4
    a = np.arange(length).reshape(1, length)
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.int32)
    b = b.astype(np.int32)
    c = vaddl_high_s32(a, b)
    print("test vaddl_high_s32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length = 16
    a = np.arange(length).reshape(1, length)
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.uint8)
    b = b.astype(np.uint8)    
    c = vaddl_high_u8(a, b)
    print("test vaddl_high_u8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length = 8
    a = np.arange(length).reshape(1, length)
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.uint16)
    b = b.astype(np.uint16)    
    c = vaddl_high_u16(a, b)
    print("test vaddl_high_u16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    length = 4
    a = np.arange(length).reshape(1, length)
    b = np.arange(length).reshape(1, length)
    a = a.astype(np.uint32)
    b = b.astype(np.uint32)
    c = vaddl_high_u32(a, b)
    print("test vaddl_high_u32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)