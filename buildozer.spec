[app]
title = NEAM PREMIUM CALCULATOR
package.name = neampremiumcalculator
package.domain = org.neamkhan
source.dir = .
source.include_exts = py
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.permissions = INTERNET
android.archs = arm64-v8a
