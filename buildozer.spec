[app]

# (必须修改) 你的应用的标题
title = by小磊

# (必须修改) 你的应用的包名，全小写，无特殊字符
package.name = byxiaolei

# (必须修改) 你的应用的域名，用于生成唯一的包ID
package.domain = org.demo

# 源文件目录，保持默认即可
source.dir = .

# 要包含的源文件扩展名，保持默认即可
source.include_exts = py,png,jpg,kv,atlas

# (可选) 应用的版本号
version = 0.1

# (必须修改) App运行所需要的Python库，用逗号隔开
# 对于我们的简单示例，只需要 python3 和 kivy
requirements = python3,kivy

# (可选) App在屏幕上的方向。可以是 landscape, portrait, all
orientation = portrait

# (可选) 应用图标的文件名
icon.filename = %(source.dir)s/data/icon.png

# (可选) 应用启动画面的文件名
presplash.filename = %(source.dir)s/data/presplash.png

# (可选) 启动时是否显示安卓加载动画
presplash.color = #FFFFFF

# (可选) 是否允许 App 备份
android.allow_backup = True

# (可选) 安卓权限。如果你的App需要访问网络、摄像头等，在这里声明
# 例如: android.permissions = INTERNET,CAMERA
android.permissions =

# (可选) 应用在最近任务列表中的窗口颜色
android.color = #FFFFFF

# (可选) 是否全屏
fullscreen = 0

# (可选) 安卓API级别。保持默认通常是安全的
android.api = 31

# (可选) 安卓最低API级别
android.minapi = 21

# (可选) 安卓SDK版本
android.sdk = 24

# (可选) 安卓NDK版本
android.ndk = 25b

# (可选) 安卓NDK路径
# android.ndk_path =

# (可选) 安卓SDK路径
# android.sdk_path =

# (可选) 安卓构建工具版本
# android.build_tools_version =

# (可选) Java JDK路径
# android.java_home =

# (可选) P4A (Python-for-Android) 的分支或版本
# p4a.branch = master


[buildozer]

# 日志输出级别。2 表示详细信息，对于调试很有用
log_level = 2

# 警告模式。0=无, 1=常规, 2=所有
warn_on_root = 1

# (可选) .buildozer 文件夹的路径
# build_dir = ./.buildozer

# (可选) 下载缓存的路径
# bin_dir = ./.buildozer/bin

