#-*- coding:utf-8 -*-
import numpy as np


############################
##dtype == "int8x8"
############################
def check_int8x8(input):
    if input.dtype != "int8" or input.shape != (1, 8):
        return False
    else:
        return True

############################
##dtype == "int8x16"
############################
def check_int8x16(input):
    if input.dtype != "int8" or input.shape != (1, 16):
        return False
    else:
        return True

############################
##dtype == "int16x4"
############################
def check_int16x4(input):
    if input.dtype != "int16" or input.shape != (1, 4):
        return False
    else:
        return True

############################
##dtype == "int16x8"
############################
def check_int16x8(input):
    if input.dtype != "int16" or input.shape != (1, 8):
        return False
    else:
        return True

############################
##dtype == "int32x2"
############################
def check_int32x2(input):
    if input.dtype != "int32" or input.shape != (1, 2):
        return False
    else:
        return True

############################
##dtype == "int32x4"
############################
def check_int32x4(input):
    if input.dtype != "int32" or input.shape != (1, 4):
        return False
    else:
        return True

############################
##dtype == "int64x1"
############################
def check_int64x1(input):
    if input.dtype != "int64" or input.shape != (1, 1):
        return False
    else:
        return True

############################
##dtype == "int64x2"
############################
def check_int64x2(input):
    if input.dtype != "int64" or input.shape != (1, 2):
        return False
    else:
        return True

############################
##dtype == "uint8x8"
############################
def check_uint8x8(input):
    if input.dtype != "uint8" or input.shape != (1, 8):
        return False
    else:
        return True

############################
##dtype == "uint8x16"
############################
def check_uint8x16(input):
    if input.dtype != "uint8" or input.shape != (1, 16):
        return False
    else:
        return True

############################
##dtype == "uint16x4"
############################
def check_uint16x4(input):
    if input.dtype != "uint16" or input.shape != (1, 4):
        return False
    else:
        return True

############################
##dtype == "uint16x8"
############################
def check_uint16x8(input):
    if input.dtype != "uint16" or input.shape != (1, 8):
        return False
    else:
        return True

############################
##dtype == "uint32x2"
############################
def check_uint32x2(input):
    if input.dtype != "uint32" or input.shape != (1, 2):
        return False
    else:
        return True

############################
##dtype == "uint32x4"
############################
def check_uint32x4(input):
    if input.dtype != "uint32" or input.shape != (1, 4):
        return False        
    else:
        return True

############################
##dtype == "uint64x1"
############################
def check_uint64x1(input):
    if input.dtype != "uint64" or input.shape != (1, 1):
        return False
    else:
        return True

############################
##dtype == "uint64x2"
############################
def check_uint64x2(input):
    if input.dtype != "uint64" or input.shape != (1, 2):
        return False       
    else:
        return True

############################
##dtype == "float32x2"
############################
def check_float32x2(input):
    if input.dtype != "float32" or input.shape != (1, 2):
        return False
    else:
        return True        

############################
##dtype == "float32x4"
############################
def check_float32x4(input):
    if input.dtype != "float32" or input.shape != (1, 4):
        return False
    else:
        return True        

############################
##dtype == "float64x1"
############################
def check_float64x1(input):
    if input.dtype != "float64" or input.shape != (1, 1):
        return False
    else:
        return True        

############################
##dtype == "float64x2"
############################
def check_float64x2(input):
    if input.dtype != "float64" or input.shape != (1, 2):
        return False
    else:
        return True

############################
##dtype == "int64"
############################
def check_int64(input):
    if input.dtype != "int64" or input.shape != (1, ):
        return False
    else:
        return True

############################
##dtype == "uint64"
############################
def check_uint64(input):
    if input.dtype != "uint64" or input.shape != (1, ):
        return False
    else:
        return True