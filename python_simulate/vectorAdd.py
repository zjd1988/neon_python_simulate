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
##c.dtype == "int8x8"
############################
def vadd_s8(a, b):
    if checkType.check_int8x8(a) == False or checkType.check_int8x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "int8x16"
##b.dtype == "int8x16"
##Out para:
##c.dtype == "int8x16"
############################
def vaddq_s8(a, b):
    if checkType.check_int8x16(a) == False or checkType.check_int8x16(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "int16x4"
##b.dtype == "int16x4"
##Out para:
##c.dtype == "int16x4"
############################
def vadd_s16(a, b):
    if checkType.check_int16x4(a) == False or checkType.check_int16x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "int16x8"
##b.dtype == "int16x8"
##Out para:
##c.dtype == "int16x8"
############################
def vaddq_s16(a, b):
    if checkType.check_int16x8(a) == False or checkType.check_int16x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "int32x2"
##b.dtype == "int32x2"
##Out para:
##c.dtype == "int32x2"
############################
def vadd_s32(a, b):
    if checkType.check_int32x2(a) == False or checkType.check_int32x2(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "int32x4"
##b.dtype == "int32x4"
##Out para:
##c.dtype == "int32x4"
############################
def vaddq_s32(a, b):
    if checkType.check_int32x4(a) == False or checkType.check_int32x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "int64x1"
##b.dtype == "int64x1"
##Out para:
##c.dtype == "int64x1"
############################
def vadd_s64(a, b):
    if checkType.check_int64x1(a) == False or checkType.check_int64x1(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "int64x2"
##b.dtype == "int64x2"
##Out para:
##c.dtype == "int64x2"
############################
def vaddq_s64(a, b):
    if checkType.check_int64x2(a) == False or checkType.check_int64x2(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "uint8x8"
##b.dtype == "uint8x8"
##Out para:
##c.dtype == "uint8x8"
############################
def vadd_u8(a, b):
    if checkType.check_uint8x8(a) == False or checkType.check_uint8x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "uint8x16"
##b.dtype == "uint8x16"
##Out para:
##c.dtype == "uint8x16"
############################
def vaddq_u8(a, b):
    if checkType.check_uint8x16(a) == False or checkType.check_uint8x16(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "uint16x4"
##b.dtype == "uint16x4"
##Out para:
##c.dtype == "uint16x4"
############################
def vadd_u16(a, b):
    if checkType.check_uint16x4(a) == False or checkType.check_uint16x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "uint16x8"
##b.dtype == "uint16x8"
##Out para:
##c.dtype == "uint16x8"
############################
def vaddq_u16(a, b):
    if checkType.check_uint16x8(a) == False or checkType.check_uint16x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "uint32x2"
##b.dtype == "uint32x2"
##Out para:
##c.dtype == "uint32x2"
############################
def vadd_u32(a, b):
    if checkType.check_uint32x2(a) == False or checkType.check_uint32x2(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "uint32x4"
##b.dtype == "uint32x4"
##Out para:
##c.dtype == "uint32x4"
############################
def vaddq_u32(a, b):
    if checkType.check_uint32x4(a) == False or checkType.check_uint32x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "uint64x1"
##b.dtype == "uint64x1"
##Out para:
##c.dtype == "uint64x1"
############################
def vadd_u64(a, b):
    if checkType.check_uint64x1(a) == False or checkType.check_uint64x1(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "uint64x2"
##b.dtype == "uint64x2"
##Out para:
##c.dtype == "uint64x2"
############################
def vaddq_u64(a, b):
    if checkType.check_uint64x2(a) == False or checkType.check_uint64x2(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "float32x2"
##b.dtype == "float32x2"
##Out para:
##c.dtype == "float32x2"
############################
def vadd_f32(a, b):
    if checkType.check_float32x2(a) == False or checkType.check_float32x2(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "float32x4"
##b.dtype == "float32x4"
##Out para:
##c.dtype == "float32x4"
############################
def vaddq_f32(a, b):
    if checkType.check_float32x4(a) == False or checkType.check_float32x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "float64x1"
##b.dtype == "float64x1"
##Out para:
##c.dtype == "float64x1"
############################
def vadd_f64(a, b):
    if checkType.check_float64x1(a) == False or checkType.check_float64x1(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "float64x2"
##b.dtype == "float64x2"
##Out para:
##c.dtype == "float64x2"
############################
def vaddq_f64(a, b):
    if checkType.check_float64x2(a) == False or checkType.check_float64x2(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c    

############################
##In para:
##a.dtype == "int64"
##b.dtype == "int64"
##Out para:
##c.dtype == "int64"
############################
def vaddd_s64(a, b):
    if checkType.check_int64(a) == False or checkType.check_int64(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c

############################
##In para:
##a.dtype == "uint64"
##b.dtype == "uint64"
##Out para:
##c.dtype == "uint64"
############################
def vaddd_u64(a, b):
    if checkType.check_uint64(a) == False or checkType.check_uint64(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    c = a + b
    return c



if __name__ == "__main__":
    a = np.arange(8).reshape(1, 8)
    b = np.arange(8).reshape(1, 8)
    a = a.astype(np.int8)
    b = b.astype(np.int8)    
    c = vadd_s8(a, b)
    print("test vadd_s8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(16).reshape(1, 16)
    b = np.arange(16).reshape(1, 16)
    a = a.astype(np.int8)
    b = b.astype(np.int8)    
    c = vaddq_s8(a, b)
    print("test vaddq_s8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(4).reshape(1, 4)
    b = np.arange(4).reshape(1, 4)
    a = a.astype(np.int16)
    b = b.astype(np.int16)
    c = vadd_s16(a, b)
    print("test vadd_s16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(8).reshape(1, 8)
    b = np.arange(8).reshape(1, 8)
    a = a.astype(np.int16)
    b = b.astype(np.int16)
    c = vaddq_s16(a, b)
    print("test vaddq_s16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(2).reshape(1, 2)
    b = np.arange(2).reshape(1, 2)
    a = a.astype(np.int32)
    b = b.astype(np.int32)
    c = vadd_s32(a, b)
    print("test vadd_s32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    a = np.arange(4).reshape(1, 4)
    b = np.arange(4).reshape(1, 4)
    a = a.astype(np.int32)
    b = b.astype(np.int32)
    c = vaddq_s32(a, b)
    print("test vaddq_s32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    a = np.arange(1).reshape(1, 1)
    b = np.arange(1).reshape(1, 1)
    a = a.astype(np.int64)
    b = b.astype(np.int64)
    c = vadd_s64(a, b)
    print("test vadd_s64")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(2).reshape(1, 2)
    b = np.arange(2).reshape(1, 2)
    a = a.astype(np.int64)
    b = b.astype(np.int64)
    c = vaddq_s64(a, b)
    print("test vaddq_s64")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(8).reshape(1, 8)
    b = np.arange(8).reshape(1, 8)
    a = a.astype(np.uint8)
    b = b.astype(np.uint8)
    c = vadd_u8(a, b)
    print("test vadd_u8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(16).reshape(1, 16)
    b = np.arange(16).reshape(1, 16)
    a = a.astype(np.uint8)
    b = b.astype(np.uint8)
    c = vaddq_u8(a, b)
    print("test vaddq_u16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(4).reshape(1, 4)
    b = np.arange(4).reshape(1, 4)
    a = a.astype(np.uint16)
    b = b.astype(np.uint16)
    c = vadd_u16(a, b)
    print("test vadd_u16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(8).reshape(1, 8)
    b = np.arange(8).reshape(1, 8)
    a = a.astype(np.uint16)
    b = b.astype(np.uint16)
    c = vaddq_u16(a, b)
    print("test vaddq_u16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(2).reshape(1, 2)
    b = np.arange(2).reshape(1, 2)
    a = a.astype(np.uint32)
    b = b.astype(np.uint32)
    c = vadd_u32(a, b)
    print("test vadd_u32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(4).reshape(1, 4)
    b = np.arange(4).reshape(1, 4)
    a = a.astype(np.uint32)
    b = b.astype(np.uint32)
    c = vaddq_u32(a, b)
    print("test vaddq_u32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(1).reshape(1, 1)
    b = np.arange(1).reshape(1, 1)
    a = a.astype(np.uint64)
    b = b.astype(np.uint64)
    c = vadd_u64(a, b)
    print("test vadd_u64")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(2).reshape(1, 2)
    b = np.arange(2).reshape(1, 2)
    a = a.astype(np.uint64)
    b = b.astype(np.uint64)
    c = vaddq_u64(a, b)
    print("test vaddq_u64")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    a = np.arange(2).reshape(1, 2)
    b = np.arange(2).reshape(1, 2)
    a = a.astype(np.float32)
    b = b.astype(np.float32)
    c = vadd_f32(a, b)
    print("test vadd_f32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(4).reshape(1, 4)
    b = np.arange(4).reshape(1, 4)
    a = a.astype(np.float32)
    b = b.astype(np.float32)
    c = vaddq_f32(a, b)
    print("test vaddq_f32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    a = np.arange(1).reshape(1, 1)
    b = np.arange(1).reshape(1, 1)
    a = a.astype(np.float64)
    b = b.astype(np.float64)
    c = vadd_f64(a, b)
    print("test vadd_f64")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(2).reshape(1, 2)
    b = np.arange(2).reshape(1, 2)
    a = a.astype(np.float64)
    b = b.astype(np.float64)
    c = vaddq_f64(a, b)
    print("test vaddq_f64")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(1).reshape((1, ))
    b = np.arange(1).reshape((1, ))
    a = a.astype(np.int64)
    b = b.astype(np.int64)
    c = vaddd_s64(a, b)
    print("test vaddd_s64")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)

    a = np.arange(1).reshape((1, ))
    b = np.arange(1).reshape((1, ))
    a = a.astype(np.uint64)
    b = b.astype(np.uint64)
    c = vaddd_u64(a, b)
    print("test vaddq_u64")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)