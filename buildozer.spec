[app]
title = Spin RNG
package.name = spinrng
package.domain = org.spinrng
source.dir = .
source.include_exts = py,png,jpg,jpeg,json
version = 1.0.0
requirements = python3==3.9.12,kivy==2.2.1,random,time,os,json,math
orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.accept_sdk_license = True
android.api = 33
android.ndk = 23b
p4a.branch = release-2022.12.20

[buildozer]
log_level = 2
