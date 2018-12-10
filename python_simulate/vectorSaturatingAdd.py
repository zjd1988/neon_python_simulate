#-*- coding:utf-8 -*-
import numpy as np
import checkType

########################
##In para:
##a
##b
##Out para:
##c : 
# -1 :underflow 
# 0: not underflow or overflow 
# 1: overflow
#-2 : error occur
#########################
def addSaturation(a, b):
    if a.dtype != b.dtype:
        print("a's type is different from b's type!!!!")
        return -1
    if a.dtype == "int8":
        bit_count = 7
    elif a.dtype == "int16":
        bit_count = 15
    elif a.dtype == "int32":
        bit_count = 31
    elif a.dtype == "int64":
        bit_count = 63
    elif a.dtype == "uint8":
        bit_count = 8
    elif a.dtype == "uint16":
        bit_count = 16
    elif a.dtype == "uint32":
        bit_count = 32
    elif a.dtype == "uint64":
        bit_count = 64
    else:
        return -1
    
    max_value = 2 ** bit_count - 1
    type_info = a.dtype
    if type_info.name[0] == "u":
        min_value = 0
    else:
        min_value = -(2 ** bit_count)

    new_a = a.astype(np.float64)
    new_b = b.astype(np.float64)

    row,col = new_a.shape
    c = np.empty(new_a.shape)
    for row_index in range(row):
        for col_index in range(col):
            if new_a[row_index][col_index] + new_b[row_index][col_index] < min_value:
                c[row_index][col_index] = min_value
            elif new_a[row_index][col_index] + new_b[row_index][col_index] > max_value:
                c[row_index][col_index] = max_value
            else:
                c[row_index][col_index] = new_a[row_index][col_index] + new_b[row_index][col_index]
    c = c.astype(a.dtype)
    return c
#################### SQADD #########################################
#https://developer.arm.com/docs/ddi0596/a/a64-simd-and-floating-point-instructions-alphabetic-order/sqadd-signed-saturating-add
#Signed saturating Add. This instruction adds the values of corresponding 
# elements of the two source SIMD&FP registers, places the results into a 
# vector, and writes the vector to the destination SIMD&FP register.
#If overflow occurs with any of the results, those results are saturated.
#  If saturation occurs, the cumulative saturation bit FPSR.QC is set.
#################### SQADD #########################################

############################
##In para:
##a.dtype == "int8x8"
##b.dtype == "int8x8"
##Out para:
##c.dtype == "int8x8"
############################
def vqadd_s8 (a, b):
    if checkType.check_int8x8(a) == False or checkType.check_int8x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1

    return addSaturation(a, b)


############################
##In para:
##a.dtype == "int8x16"
##b.dtype == "int8x16"
##Out para:
##c.dtype == "int8x16"
############################
def vqaddq_s8 (a, b):
    if checkType.check_int8x16(a) == False or checkType.check_int8x16(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    
    return addSaturation(a, b)


############################
##In para:
##a.dtype == "int16x4"
##b.dtype == "int16x4"
##Out para:
##c.dtype == "int16x4"
############################
def vqadd_s16 (a, b):
    if checkType.check_int16x4(a) == False or checkType.check_int16x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    
    return addSaturation(a, b)


############################
##In para:
##a.dtype == "int16x8"
##b.dtype == "int16x8"
##Out para:
##c.dtype == "int16x8"
############################
def vqaddq_s16 (a, b):
    if checkType.check_int16x8(a) == False or checkType.check_int16x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    
    return addSaturation(a, b)


############################
##In para:
##a.dtype == "int32x2"
##b.dtype == "int32x2"
##Out para:
##c.dtype == "int32x2"
############################
def vqadd_s32 (a, b):
    if checkType.check_int32x2(a) == False or checkType.check_int32x2(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    
    return addSaturation(a, b)




############################
##In para:
##a.dtype == "int32x4"
##b.dtype == "int32x4"
##Out para:
##c.dtype == "int32x4"
############################
def vqaddq_s32 (a, b):
    if checkType.check_int32x4(a) == False or checkType.check_int32x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    
    return addSaturation(a, b)



############################
##In para:
##a.dtype == "int64x1"
##b.dtype == "int64x1"
##Out para:
##c.dtype == "int64x1"
############################
def vqadd_s64 (a, b):
    if checkType.check_int64x1(a) == False or checkType.check_int64x1(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    
    return addSaturation(a, b)



############################
##In para:
##a.dtype == "int64x2"
##b.dtype == "int64x2"
##Out para:
##c.dtype == "int64x2"
############################
def vqaddq_s64(a, b):
    if checkType.check_int64x2(a) == False or checkType.check_int64x2(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    
    return addSaturation(a, b)



######################## UQADD ###################################
#https://developer.arm.com/docs/ddi0596/a/a64-simd-and-floating-point-instructions-alphabetic-order/uqadd-unsigned-saturating-add
#Unsigned saturating Add. This instruction adds the values of corresponding
#elements of the two source SIMD&FP registers, places the results into a 
# vector, and writes the vector to the destination SIMD&FP register.
#If overflow occurs with any of the results, those results are saturated.
#If saturation occurs, the cumulative saturation bit FPSR.QC is set.


############################
##In para:
##a.dtype == "uint8x8"
##b.dtype == "uint8x8"
##Out para:
##c.dtype == "uint8x8"
############################
def vqadd_u8 (a, b):
    if checkType.check_uint8x8(a) == False or checkType.check_uint8x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    
    return addSaturation(a, b)   



############################
##In para:
##a.dtype == "uint8x16"
##b.dtype == "uint8x16"
##Out para:
##c.dtype == "uint8x16"
############################
def vqaddq_u8 (a, b):
    if checkType.check_uint8x16(a) == False or checkType.check_uint8x16(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    
    return addSaturation(a, b)




############################
##In para:
##a.dtype == "uint16x4"
##b.dtype == "uint16x4"
##Out para:
##c.dtype == "uint16x4"
############################
def vqadd_u16(a, b):
    if checkType.check_uint16x4(a) == False or checkType.check_uint16x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    
    return addSaturation(a, b)   




############################
##In para:
##a.dtype == "uint16x8"
##b.dtype == "uint16x8"
##Out para:
##c.dtype == "uint16x8"
############################
def vqaddq_u16(a, b):
    if checkType.check_uint16x8(a) == False or checkType.check_uint16x8(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    
    return addSaturation(a, b)      




############################
##In para:
##a.dtype == "uint32x2"
##b.dtype == "uint32x2"
##Out para:
##c.dtype == "uint32x2"
############################
def vqadd_u32(a, b):
    if checkType.check_uint32x2(a) == False or checkType.check_uint32x2(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    
    return addSaturation(a, b)





############################
##In para:
##a.dtype == "uint32x4"
##b.dtype == "uint32x4"
##Out para:
##c.dtype == "uint32x4"
############################
def vqaddq_u32(a, b):
    if checkType.check_uint32x4(a) == False or checkType.check_uint32x4(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    
    return addSaturation(a, b)   



############################
##In para:
##a.dtype == "uint64x1"
##b.dtype == "uint64x1"
##Out para:
##c.dtype == "uint64x1"
############################
def vqadd_u64(a, b):
    if checkType.check_uint64x1(a) == False or checkType.check_uint64x1(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    
    return addSaturation(a, b)





############################
##In para:
##a.dtype == "uint64x2"
##b.dtype == "uint64x2"
##Out para:
##c.dtype == "uint64x2"
############################
def vqaddq_u64(a, b):
    if checkType.check_uint64x2(a) == False or checkType.check_uint64x2(b) == False:
        print("input para type is wrong a's type is {} a's size is {} ; b's type is {} b's size is {}".format(a.dtype, a.shape, b.dtype, b.shape))
        return -1
    
    return addSaturation(a, b)





if __name__ == "__main__":
    bit_count = 8
    max_value = 2 ** (bit_count - 1) - 1
    num_count = 8
    a = np.random.randn(1, num_count) * max_value
    b = np.random.randn(1, num_count) * max_value
    a = a.astype(np.int8)
    b = b.astype(np.int8)    
    c = vqadd_s8(a, b)
    print("test vqadd_s8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)      

    bit_count = 8
    max_value = 2 ** (bit_count - 1) - 1
    num_count = 16
    a = np.random.randn(1, num_count) * max_value
    b = np.random.randn(1, num_count) * max_value
    a = a.astype(np.int8)
    b = b.astype(np.int8)
    c = vqaddq_s8(a, b)
    print("test vqaddq_s8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    bit_count = 16
    max_value = 2 ** (bit_count - 1) - 1
    num_count = 4
    a = np.random.randn(1, num_count) * max_value
    b = np.random.randn(1, num_count) * max_value
    a = a.astype(np.int16)
    b = b.astype(np.int16)    
    c = vqadd_s16(a, b)
    print("test vqadd_s16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)    


    bit_count = 16
    max_value = 2 ** (bit_count - 1) - 1
    num_count = 8
    a = np.random.randn(1, num_count) * max_value
    b = np.random.randn(1, num_count) * max_value
    a = a.astype(np.int16)
    b = b.astype(np.int16)    
    c = vqaddq_s16(a, b)
    print("test vqaddq_s16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)     



    bit_count = 32
    max_value = 2 ** (bit_count - 1) - 1
    num_count = 2
    a = np.random.randn(1, num_count) * max_value
    b = np.random.randn(1, num_count) * max_value
    a = a.astype(np.int32)
    b = b.astype(np.int32)    
    c = vqadd_s32(a, b)
    print("test vqadd_s32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)     



    bit_count = 32
    max_value = 2 ** (bit_count - 1) - 1
    num_count = 4
    a = np.random.randn(1, num_count) * max_value
    b = np.random.randn(1, num_count) * max_value
    a = a.astype(np.int32)
    b = b.astype(np.int32)    
    c = vqaddq_s32(a, b)
    print("test vqaddq_s32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)         


    bit_count = 64
    max_value = 2 ** (bit_count - 1) - 1
    num_count = 1
    a = np.random.randn(1, num_count) * max_value
    b = np.random.randn(1, num_count) * max_value
    a = a.astype(np.int64)
    b = b.astype(np.int64)    
    c = vqadd_s64(a, b)
    print("test vqadd_s64")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)       


    bit_count = 64
    max_value = 2 ** (bit_count - 1) - 1
    num_count = 2
    a = np.random.randn(1, num_count) * max_value
    b = np.random.randn(1, num_count) * max_value
    a = a.astype(np.int64)
    b = b.astype(np.int64)    
    c = vqaddq_s64(a, b)
    print("test vqaddq_s64")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)    



    #############################
    #############################



    bit_count = 8
    max_value = 2 ** bit_count - 1
    num_count = 8
    a = np.random.randn(1, num_count) * max_value
    b = np.random.randn(1, num_count) * max_value
    a = a.astype(np.uint8)
    b = b.astype(np.uint8)    
    c = vqadd_u8(a, b)
    print("test vqadd_u8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)      


    bit_count = 8
    max_value = 2 ** bit_count - 1
    num_count = 16
    a = np.random.randn(1, num_count) * max_value
    b = np.random.randn(1, num_count) * max_value
    a = a.astype(np.uint8)
    b = b.astype(np.uint8)    
    c = vqaddq_u8(a, b)
    print("test vqaddq_u8")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)


    bit_count = 16
    max_value = 2 ** bit_count - 1
    num_count = 4
    a = np.random.randn(1, num_count) * max_value
    b = np.random.randn(1, num_count) * max_value
    a = a.astype(np.uint16)
    b = b.astype(np.uint16)    
    c = vqadd_u16(a, b)
    print("test vqadd_u16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)    


    bit_count = 16
    max_value = 2 ** bit_count - 1
    num_count = 8
    a = np.random.randn(1, num_count) * max_value
    b = np.random.randn(1, num_count) * max_value
    a = a.astype(np.uint16)
    b = b.astype(np.uint16)    
    c = vqaddq_u16(a, b)
    print("test vqaddq_u16")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)     



    bit_count = 32
    max_value = 2 ** bit_count - 1
    num_count = 2
    a = np.random.randn(1, num_count) * max_value
    b = np.random.randn(1, num_count) * max_value
    a = a.astype(np.uint32)
    b = b.astype(np.uint32)    
    c = vqadd_u32(a, b)
    print("test vqadd_u32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)     



    bit_count = 32
    max_value = 2 ** bit_count - 1
    num_count = 4
    a = np.random.randn(1, num_count) * max_value
    b = np.random.randn(1, num_count) * max_value
    a = a.astype(np.uint32)
    b = b.astype(np.uint32)    
    c = vqaddq_u32(a, b)
    print("test vqaddq_u32")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)         


    bit_count = 64
    max_value = 2 ** bit_count - 1
    num_count = 1
    a = np.random.randn(1, num_count) * max_value
    b = np.random.randn(1, num_count) * max_value
    a = a.astype(np.uint64)
    b = b.astype(np.uint64)    
    c = vqadd_u64(a, b)
    print("test vqadd_u64")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)       


    bit_count = 64
    max_value = 2 ** bit_count - 1
    num_count = 2
    a = np.random.randn(1, num_count) * max_value
    b = np.random.randn(1, num_count) * max_value
    a = a.astype(np.uint64)
    b = b.astype(np.uint64)    
    c = vqaddq_u64(a, b)
    print("test vqaddq_u64")
    print(a, "shape:", a.shape, "dtype:", a.dtype)
    print(b, "shape:", b.shape, "dtype:", b.dtype)
    print(c, "shape:", c.shape, "dtype:", c.dtype)    