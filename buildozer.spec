[app]
# 你的应用标题
title = My First App
# 你的应用的包名 (全小写，无特殊字符)
package.name = myfirstapp
# 你的应用的域名 (用于生成唯一的包ID)
package.domain = org.demo
# 源码目录
source.dir = .
# 需要包含的源文件后缀
source.include_exts = py,png,jpg,kv,atlas
# 应用版本
version = 0.1
# 应用依赖的库
requirements = python3,kivy
# 屏幕方向
orientation = portrait

# --- 安卓生产级配置 (最终稳定版) ---
# 目标安卓 API 等级
android.api = 33
# 最低支持的安卓 API 等级
android.minapi = 24
# 明确指定一个稳定版的编译工具
android.build_tools_version = 34.0.0
# 自动接受SDK许可协议
android.accept_sdk_license = True
# 仅编译 arm64-v8a 架构，速度更快，覆盖绝大多数现代手机
android.archs = arm64-v8a

[buildozer]
# 日志等级 (2=调试)
log_level = 2
# 如果以 root 身份运行 buildozer 则显示警告
warn_on_root = 1