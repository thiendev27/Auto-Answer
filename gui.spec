# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:/a Python/My Project/Azota Answer Mixing/gui.py'],
    pathex=[],
    binaries=[],
    datas=[('D:/a Python/My Project/Azota Answer Mixing/help.py', '.'), ('D:/a Python/My Project/Azota Answer Mixing/process.py', '.'), ('D:/a Python/My Project/Azota Answer Mixing/Ubuntu.qss', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='gui',
)