[app]

# (str) 你的应用标题
title = My First App

# (str) 你的应用的包名 (全小写，无特殊字符)
package.name = myfirstapp

# (str) 你的应用的域名 (用于生成唯一的包ID)
package.domain = org.demo

# (str) 源码目录，main.py所在的位置
source.dir = .

# (list) 需要包含的源文件后缀
source.include_exts = py,png,jpg,kv,atlas

# (list) 使用模式匹配包含的文件
#source.include_patterns = assets/*,images/*.png

# (list) 需要排除的源文件后缀
#source.exclude_exts = spec

# (list) 需要排除的目录
#source.exclude_dirs = tests, bin, venv

# (list) 使用模式匹配排除的文件
#source.exclude_patterns = license,images/*/*.jpg

# (str) 应用版本
version = 0.1

# (list) 应用依赖的库
# 我们这里只需要 kivy, python3 会被自动包含
requirements = python3,kivy

# (str) 应用启动画面
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) 应用图标
#icon.filename = %(source.dir)s/data/icon.png

# (list) 支持的屏幕方向: landscape, portrait
orientation = portrait

# (list) 声明服务
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# Android Specific
#

# (bool) 是否全屏
fullscreen = 0

# (string) Presplash 背景颜色
#android.presplash_color = #FFFFFF

# (list) 安卓权限
#android.permissions = android.permission.INTERNET

# (int) 目标安卓 API 等级, 越高越好
#android.api = 31

# (int) 最低支持的安卓 API 等级
#android.minapi = 21

# (str) 安卓 NDK 版本
#android.ndk = 25b

# (str) 安卓 NDK 目录 (如果为空，会自动下载)
#android.ndk_path =

# (str) 安卓 SDK 目录 (如果为空，会自动下载)
#android.sdk_path =

# (bool) 自动接受SDK许可协议 (为解决打包问题而修改)
# -------- 这是关键修改之一 --------
android.accept_sdk_license = True

# (str) 安卓编译工具版本 (为解决打包问题而修改)
# -------- 这是关键修改之二 --------
android.build_tools_version = 34.0.0


# (list) 安卓架构, 逗号分隔. 可选项: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) 启用安卓自动备份功能
android.allow_backup = True


[buildozer]

# (int) 日志等级 (0 = 仅错误, 1 = 信息, 2 = 调试)
log_level = 2

# (int) 如果以 root 身份运行 buildozer 则显示警告
warn_on_root = 1

# (str) buildozer 工作目录的路径
# build_dir = ./.buildozer

# (str) 生成的 .apk/.aab 文件存放目录
# bin_dir = ./bin
