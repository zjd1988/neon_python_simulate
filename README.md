# neon_python_simulate

## 起因
   创建这个库的原因是想熟悉ARM neon各个内联指令的功能，同时总结一些好的并行算法。虽然有NEON_2_SSE这个在windows学习neon的利器，但是还是感觉调试和编写比较繁琐，因此才萌生了这个想法。
    
## 内容
 - 1、 内联指令的移植
 - 2、 并行算法的仿真实现
 - 3、 ncnn和ACL库中涉及的并行算法

## 实现
 - 1、 会参考这个链接（ https://developer.arm.com/technologies/neon/intrinsics ）中的内联指令进行移植
 - 2、 每个内联指令会包含参数说明、C语言示例、python示例
 - 3、 依赖numpy库


